import importlib.util
import csv
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "prepare_1913_reconciliation_worklist.py"
SPEC = importlib.util.spec_from_file_location("prepare_1913_reconciliation_worklist", SCRIPT)
assert SPEC is not None
assert SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class CandidateMatchingTests(unittest.TestCase):
    def test_explicit_invoice_reference_is_evidence_when_amount_differs(self):
        invoices = [
            MODULE.Invoice("INV-0017", "Megan Steindlberger", "448.00", "23/09/2025")
        ]

        result = MODULE.match_credit(
            MODULE.BankRow(
                "01/10/2025",
                "449.00",
                "Fast Transfer From M JANDA Megan Steindlberger Mandarin Class INV-0017",
            ),
            invoices,
        )

        self.assertEqual(result.candidate_invoice_numbers, ("INV-0017",))
        self.assertEqual(result.evidence, "explicit_invoice_reference")
        self.assertEqual(result.status, "review")

    def test_name_and_exact_amount_produce_candidate(self):
        invoices = [
            MODULE.Invoice("INV-0084", "Bianca Wong", "588.00", "07/08/2026"),
            MODULE.Invoice("INV-0085", "Aidan Lam", "588.00", "07/08/2026"),
        ]

        result = MODULE.match_credit(
            MODULE.BankRow(
                "16/08/2026",
                "588.00",
                "Fast Transfer From BIANCA WONG Bianca - Chinese class",
            ),
            invoices,
        )

        self.assertEqual(result.candidate_invoice_numbers, ("INV-0084",))
        self.assertEqual(result.evidence, "contact_name_and_exact_amount")
        self.assertEqual(result.status, "candidate")

    def test_same_amount_without_name_is_not_identity(self):
        invoices = [
            MODULE.Invoice("INV-0084", "Bianca Wong", "588.00", "07/08/2026"),
            MODULE.Invoice("INV-0085", "Aidan Lam", "588.00", "07/08/2026"),
        ]

        result = MODULE.match_credit(
            MODULE.BankRow("16/08/2026", "588.00", "Fast Transfer From UNKNOWN PAYER"),
            invoices,
        )

        self.assertEqual(result.candidate_invoice_numbers, ())
        self.assertEqual(result.evidence, "none")
        self.assertEqual(result.status, "unresolved")

    def test_later_invoice_is_not_offered_for_earlier_payment(self):
        invoices = [
            MODULE.Invoice("INV-0085", "Aidan Lam", "588.00", "07/08/2026")
        ]

        result = MODULE.match_credit(
            MODULE.BankRow(
                "27/01/2026",
                "588.00",
                "Fast Transfer From Lam A Aidan Lam mandarin",
            ),
            invoices,
        )

        self.assertEqual(result.candidate_invoice_numbers, ())
        self.assertEqual(result.status, "unresolved")

    def test_partial_payment_with_reference_stays_for_review(self):
        invoices = [
            MODULE.Invoice("INV-0047", "Jack Anderson", "665.00", "17/03/2026")
        ]

        result = MODULE.match_credit(
            MODULE.BankRow(
                "07/05/2026",
                "332.00",
                "Fast Transfer From JACK ANDERSON INV-0047",
            ),
            invoices,
        )

        self.assertEqual(result.candidate_invoice_numbers, ("INV-0047",))
        self.assertEqual(result.status, "review")


class ClassificationTests(unittest.TestCase):
    def test_stripe_payout_is_not_revenue(self):
        result = MODULE.classify_row(
            MODULE.BankRow(
                "03/03/2026",
                "660.10",
                "Direct Credit 158824 YESMANDARIN YESMANDARIN-4XGSPM",
            ),
            [],
        )

        self.assertEqual(result.kind, "processor_payout")
        self.assertEqual(result.proposed_account, "Stripe clearing")
        self.assertEqual(result.status, "candidate")

    def test_owner_reimbursement_is_not_invoice_income(self):
        result = MODULE.classify_row(
            MODULE.BankRow(
                "11/07/2025",
                "309.55",
                "Fast Transfer From MR SHANE PHONSE SCHLE Repay amazon purchases Shane Schleger",
            ),
            [],
        )

        self.assertEqual(result.kind, "owner_or_related_party_funds")
        self.assertEqual(result.status, "review")

    def test_transfer_to_personal_account_is_isolated(self):
        result = MODULE.classify_row(
            MODULE.BankRow(
                "14/07/2025",
                "-2000.00",
                "Transfer to xx9316 CommBank app Borrowed money",
            ),
            [],
        )

        self.assertEqual(result.kind, "transfer_to_personal_account")
        self.assertEqual(result.status, "blocked_awaiting_9316")

    def test_recurring_software_expense_gets_proposal_not_final_treatment(self):
        result = MODULE.classify_row(
            MODULE.BankRow(
                "08/08/2026",
                "-6.93",
                "Microsoft-G175386947 Sydney AU Card xx7902",
            ),
            [],
        )

        self.assertEqual(result.kind, "expense")
        self.assertEqual(result.proposed_account, "Software subscriptions")
        self.assertEqual(result.status, "candidate")


class WorklistTests(unittest.TestCase):
    def test_reused_invoice_candidate_is_downgraded_for_review(self):
        invoices = [
            MODULE.Invoice("INV-0007", "Terry Tran", "620.00", "19/07/2025")
        ]
        bank_rows = [
            MODULE.BankRow("22/07/2025", "620.00", "Fast Transfer From TERRY TRAN"),
            MODULE.BankRow("26/10/2025", "620.00", "Fast Transfer From TERRY TRAN"),
        ]

        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "worklist.csv"
            summary = Path(directory) / "summary.json"
            MODULE.write_outputs(bank_rows, invoices, output, summary)
            with output.open(newline="", encoding="utf-8") as handle:
                records = list(csv.DictReader(handle))

        self.assertEqual([record["status"] for record in records], ["review", "review"])
        self.assertTrue(all("multiple bank rows" in record["note"] for record in records))

    def test_name_candidate_is_downgraded_when_another_row_has_explicit_reference(self):
        invoices = [
            MODULE.Invoice("INV-0066", "Daniel Lie", "650.00", "11/05/2026")
        ]
        bank_rows = [
            MODULE.BankRow("13/05/2026", "650.00", "Fast Transfer From DANIEL LIE INV-0066"),
            MODULE.BankRow("27/07/2026", "650.00", "Fast Transfer From DANIEL LIE Term 3"),
        ]

        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "worklist.csv"
            summary = Path(directory) / "summary.json"
            MODULE.write_outputs(bank_rows, invoices, output, summary)
            with output.open(newline="", encoding="utf-8") as handle:
                records = list(csv.DictReader(handle))

        self.assertEqual(records[0]["status"], "candidate")
        self.assertEqual(records[1]["status"], "review")


if __name__ == "__main__":
    unittest.main()
