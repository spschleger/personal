#!/usr/bin/env python3
"""Preserve and combine CommBank exports for native Xero import."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from pathlib import Path


@dataclass(frozen=True)
class Row:
    date: str
    amount: str
    description: str
    balance: str

    @property
    def identity(self) -> tuple[str, str, str, str]:
        return (self.date, self.amount, self.description, self.balance)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse(path: Path) -> list[Row]:
    rows: list[Row] = []
    with path.open(newline="", encoding="utf-8-sig") as handle:
        for line_number, fields in enumerate(csv.reader(handle), 1):
            if len(fields) != 4:
                raise ValueError(f"{path}:{line_number}: expected 4 columns, got {len(fields)}")
            date, amount, description, balance = fields
            datetime.strptime(date, "%d/%m/%Y")
            Decimal(amount)
            Decimal(balance)
            rows.append(Row(date, amount, description, balance))
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--older", type=Path, required=True)
    parser.add_argument("--newer", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    source_paths = [args.older, args.newer]
    preserved = [
        args.out_dir / "2025-07-01-to-2025-12-09-cba-business-account-1913.csv",
        args.out_dir / "2025-12-09-to-2026-08-17-cba-business-account-1913.csv",
    ]
    for source, destination in zip(source_paths, preserved):
        shutil.copyfile(source, destination)

    # CommBank exports newest-first. Start with the newer export so the
    # overlap row is retained once, then reverse the exact bank order for Xero.
    rows = [row for path in reversed(source_paths) for row in parse(path)]
    unique: dict[tuple[str, str, str, str], Row] = {}
    for row in rows:
        unique.setdefault(row.identity, row)

    combined = list(reversed(unique.values()))
    continuity_breaks: list[dict[str, str]] = []
    for older, newer in zip(combined, combined[1:]):
        if Decimal(older.balance) + Decimal(newer.amount) != Decimal(newer.balance):
            continuity_breaks.append({"older": older.date, "newer": newer.date})

    import_path = args.out_dir / "2025-07-01-to-2026-08-17-xero-bank-import.csv"
    with import_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["Date", "Amount", "Description", "Balance"])
        for row in combined:
            writer.writerow([row.date, row.amount, row.description, row.balance])

    oldest = combined[0]
    newest = combined[-1]
    credits = sum((Decimal(row.amount) for row in combined if Decimal(row.amount) > 0), Decimal())
    debits = sum((Decimal(row.amount) for row in combined if Decimal(row.amount) < 0), Decimal())
    opening_balance = Decimal(oldest.balance) - Decimal(oldest.amount)
    summary = {
        "account": "CBA Business Account ending 1913",
        "source_files": [
            {"file": path.name, "sha256": sha256(path), "rows": len(parse(path))}
            for path in preserved
        ],
        "combined": {
            "file": import_path.name,
            "sha256": sha256(import_path),
            "rows": len(combined),
            "overlap_rows_removed": len(rows) - len(combined),
            "oldest_date": oldest.date,
            "newest_date": newest.date,
            "opening_balance": f"{opening_balance:.2f}",
            "closing_balance": f"{Decimal(newest.balance):.2f}",
            "credits": f"{credits:.2f}",
            "debits": f"{debits:.2f}",
            "net_movement": f"{credits + debits:.2f}",
            "continuity_breaks": continuity_breaks,
        },
    }
    summary_path = args.out_dir / "2026-08-25-control-summary.json"
    summary_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
