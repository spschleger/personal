#!/usr/bin/env python3
"""Prepare a source-backed reconciliation worklist for CBA account 1913."""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timedelta
from decimal import Decimal
from pathlib import Path
from typing import Iterable, Sequence, Tuple


@dataclass(frozen=True)
class BankRow:
    date: str
    amount: str
    description: str


@dataclass(frozen=True)
class Invoice:
    number: str
    contact_name: str
    total: str
    date: str


@dataclass(frozen=True)
class Result:
    kind: str
    proposed_account: str
    status: str
    evidence: str
    candidate_invoice_numbers: Tuple[str, ...] = ()
    note: str = ""


TITLE_WORDS = {"dr", "mr", "mrs", "miss", "ms"}
ENTITY_WORDS = {"au", "australia", "ltd", "limited", "pty", "the"}


def words(value: str) -> Tuple[str, ...]:
    return tuple(re.findall(r"[a-z0-9]+", value.lower()))


def contact_tokens(value: str) -> Tuple[str, ...]:
    return tuple(
        token
        for token in words(value)
        if len(token) >= 3 and token not in TITLE_WORDS and token not in ENTITY_WORDS
    )


def token_matches(left: str, right: str) -> bool:
    minimum = 4
    return left == right or (
        len(left) >= minimum
        and len(right) >= minimum
        and (left.startswith(right[:minimum]) or right.startswith(left[:minimum]))
    )


def contact_appears(contact_name: str, description: str) -> bool:
    expected = contact_tokens(contact_name)
    observed = contact_tokens(description)
    if not expected:
        return False
    matched = sum(
        1 for token in expected if any(token_matches(token, seen) for seen in observed)
    )
    if len(expected) == 1:
        return matched == 1 and len(expected[0]) >= 5
    return matched >= 2


def invoice_references(description: str) -> Tuple[str, ...]:
    numbers = re.findall(r"\bINV[- ]?0*(\d+)\b", description, flags=re.IGNORECASE)
    return tuple(dict.fromkeys(f"INV-{int(number):04d}" for number in numbers))


def match_credit(row: BankRow, invoices: Sequence[Invoice]) -> Result:
    by_number = {invoice.number.upper(): invoice for invoice in invoices}
    references = tuple(
        number for number in invoice_references(row.description) if number in by_number
    )
    if references:
        exact_amount = all(
            Decimal(by_number[number].total) == Decimal(row.amount) for number in references
        )
        return Result(
            kind="invoice_payment_candidate",
            proposed_account="Accounts receivable",
            status="candidate" if exact_amount else "review",
            evidence="explicit_invoice_reference",
            candidate_invoice_numbers=references,
            note="Reference is identity evidence; review any amount difference or partial payment.",
        )

    bank_date = datetime.strptime(row.date, "%d/%m/%Y").date()
    candidates = tuple(
        invoice.number
        for invoice in invoices
        if Decimal(invoice.total) == Decimal(row.amount)
        and contact_appears(invoice.contact_name, row.description)
        and datetime.strptime(invoice.date, "%d/%m/%Y").date()
        <= bank_date + timedelta(days=14)
    )
    if len(candidates) == 1:
        return Result(
            kind="invoice_payment_candidate",
            proposed_account="Accounts receivable",
            status="candidate",
            evidence="contact_name_and_exact_amount",
            candidate_invoice_numbers=candidates,
        )
    if len(candidates) > 1:
        return Result(
            kind="invoice_payment_candidate",
            proposed_account="Accounts receivable",
            status="review",
            evidence="contact_name_and_exact_amount_multiple_invoices",
            candidate_invoice_numbers=candidates,
            note="Contact and amount agree, but more than one invoice remains possible.",
        )
    return Result(
        kind="unresolved_credit",
        proposed_account="",
        status="unresolved",
        evidence="none",
        note="Do not treat amount alone as transaction identity.",
    )


def contains_any(text: str, needles: Iterable[str]) -> bool:
    return any(needle in text for needle in needles)


def classify_row(row: BankRow, invoices: Sequence[Invoice]) -> Result:
    text = row.description.lower()
    amount = Decimal(row.amount)

    if amount > 0:
        if "yesmandarin-4xgspm" in text:
            return Result(
                kind="processor_payout",
                proposed_account="Stripe clearing",
                status="candidate",
                evidence="stripe_payout_trace_and_amount",
                note="Payout is not revenue; tie it to the separate Stripe account ledger.",
            )
        if "shane" in text and contains_any(text, ("repay", "reimburse", "amazon")):
            return Result(
                kind="owner_or_related_party_funds",
                proposed_account="Owner contribution or reimbursement",
                status="review",
                evidence="payer_and_bank_reference",
                note="Not invoice income; confirm reimbursement treatment.",
            )
        if text.startswith("refund purchase"):
            return Result(
                kind="expense_refund",
                proposed_account="Match original expense account",
                status="review",
                evidence="bank_description",
            )
        return match_credit(row, invoices)

    if "9316" in text:
        return Result(
            kind="transfer_to_personal_account",
            proposed_account="Related-party transfer",
            status="blocked_awaiting_9316",
            evidence="destination_account_last4",
            note="Felicity's personal account; match the other side before treatment.",
        )
    if contains_any(text, ("teaching service payment",)):
        return Result("contractor_payment", "Contractor costs", "review", "bank_description")
    if "office rent" in text or "rent for the ofice" in text:
        return Result("expense", "Rent", "candidate", "recurring_payee_and_reference")
    if contains_any(text, ("microsoft", "google workspace", "digital pacific", "xero au")):
        return Result("expense", "Software subscriptions", "candidate", "merchant_identity")
    if contains_any(text, ("transportfornsw", "tfnsw opal")):
        return Result("expense", "Travel", "candidate", "merchant_identity")
    if contains_any(text, ("taobao", "alipay", "alp*taobao", "international transaction fee")):
        return Result("expense", "Teaching materials or supplies", "review", "merchant_identity")
    if contains_any(text, ("amazon", "big w", "kmart", "jb hi fi", "kogan", "dollar avenue")):
        return Result("expense", "Equipment or supplies", "review", "merchant_identity")
    if contains_any(text, ("covau",)):
        return Result("expense", "Utilities", "candidate", "merchant_identity")
    if contains_any(text, ("kinokuniya", "books shipping fee")):
        return Result("expense", "Teaching materials", "candidate", "merchant_identity")
    if "client gift card" in text:
        return Result("expense", "Client gifts", "review", "bank_reference")
    if "printer" in text:
        return Result("expense", "Equipment", "review", "bank_reference")
    return Result(
        "expense",
        "Business expense - account to confirm",
        "review",
        "owner_confirmation_business_account_use",
    )


def load_invoices(path: Path) -> list[Invoice]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        rows = csv.DictReader(handle)
        return [
            Invoice(row["InvoiceNumber"], row["ContactName"], row["Total"], row["InvoiceDate"])
            for row in rows
            if row["InvoiceNumber"]
        ]


def load_bank(path: Path) -> list[BankRow]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        rows = csv.DictReader(handle)
        return [BankRow(row["Date"], row["Amount"], row["Description"]) for row in rows]


def write_outputs(
    bank_rows: Sequence[BankRow], invoices: Sequence[Invoice], output_csv: Path, summary_json: Path
) -> dict:
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    records = []

    for source_row, row in enumerate(bank_rows, 1):
        result = classify_row(row, invoices)
        records.append(
            {
                "source_row": source_row,
                "date": row.date,
                "amount": row.amount,
                "description": row.description,
                "kind": result.kind,
                "proposed_account": result.proposed_account,
                "status": result.status,
                "evidence": result.evidence,
                "candidate_invoice_numbers": ";".join(result.candidate_invoice_numbers),
                "note": result.note,
            }
        )

    candidate_usage: Counter[str] = Counter(
        invoice_number
        for record in records
        if record["kind"] == "invoice_payment_candidate"
        for invoice_number in record["candidate_invoice_numbers"].split(";")
        if invoice_number
    )
    for record in records:
        candidate_number = record["candidate_invoice_numbers"]
        if (
            record["status"] == "candidate"
            and record["evidence"] == "contact_name_and_exact_amount"
            and candidate_usage[candidate_number] > 1
        ):
            record["status"] = "review"
            record["note"] = "The same invoice is a candidate for multiple bank rows."

    status_counts = Counter(record["status"] for record in records)
    kind_counts = Counter(record["kind"] for record in records)
    signed_totals: defaultdict[str, Decimal] = defaultdict(Decimal)
    for record in records:
        signed_totals[record["kind"]] += Decimal(record["amount"])

    fieldnames = list(records[0])
    with output_csv.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(records)

    summary = {
        "source_rows": len(bank_rows),
        "status_counts": dict(sorted(status_counts.items())),
        "kind_counts": dict(sorted(kind_counts.items())),
        "signed_totals_by_kind": {
            key: f"{value:.2f}" for key, value in sorted(signed_totals.items())
        },
        "controls": {
            "credits": f"{sum((Decimal(row.amount) for row in bank_rows if Decimal(row.amount) > 0), Decimal()):.2f}",
            "debits": f"{sum((Decimal(row.amount) for row in bank_rows if Decimal(row.amount) < 0), Decimal()):.2f}",
            "net_movement": f"{sum((Decimal(row.amount) for row in bank_rows), Decimal()):.2f}",
        },
        "rules": [
            "Amount alone never creates an invoice candidate.",
            "Candidate is not reconciliation approval.",
            "Personal-account transfers stay blocked until account 9316 evidence is supplied.",
        ],
    }
    summary_json.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bank", type=Path, required=True)
    parser.add_argument("--invoices", type=Path, required=True)
    parser.add_argument("--output-csv", type=Path, required=True)
    parser.add_argument("--summary-json", type=Path, required=True)
    args = parser.parse_args()

    summary = write_outputs(
        load_bank(args.bank),
        load_invoices(args.invoices),
        args.output_csv,
        args.summary_json,
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
