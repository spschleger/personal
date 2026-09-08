import csv
import json
import unittest
from datetime import datetime
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "workpapers/2026-09-08-xero-final-gift-and-next-supported-later-batch.json"
WORKLIST = ROOT / "workpapers/2026-08-25-account-1913-reconciliation-worklist.csv"


class FinalGiftAndNextSupportedLaterBatchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(AUDIT.read_text())
        cls.by_row = {item["source_row"]: item for item in cls.data["transactions"]}
        with WORKLIST.open(newline="") as handle:
            cls.source = {int(row["source_row"]): row for row in csv.DictReader(handle)}

    def test_batch_is_bounded_and_source_exact(self):
        expected_rows = [160, 210, 211, 213, 214, 218, 219, 220]
        self.assertEqual(list(self.by_row), expected_rows)
        self.assertEqual(self.data["status"], "completed_and_live_verified_bounded_eight_lines")
        for row in expected_rows:
            item = self.by_row[row]
            source = self.source[row]
            self.assertEqual(
                datetime.strptime(source["date"], "%d/%m/%Y").strftime("%Y-%m-%d"),
                item["date"],
            )
            self.assertEqual(Decimal(source["amount"]), Decimal(item["amount"]))
            self.assertEqual(source["description"], item["bank_description"])
            self.assertIn("posted", item["posting_status"])

    def test_gift_treatment_preserves_boundary(self):
        gift = self.by_row[160]
        self.assertEqual(gift["transaction_type"], "Spend Money")
        self.assertEqual(gift["account"], "429 - General Expenses")
        self.assertEqual(gift["tax_rate"], "BAS Excluded")
        self.assertEqual(
            gift["description"],
            "Client gift card - Mark Zheng; year-end deductibility review pending",
        )
        self.assertNotIn("entertainment", gift["account"].lower())
        self.assertIn("no tax-deductibility claim", gift["tax_boundary"])

    def test_later_seven_accounts_tax_and_total(self):
        later = [self.by_row[row] for row in [210, 211, 213, 214, 218, 219, 220]]
        self.assertEqual(-sum((Decimal(item["amount"]) for item in later), Decimal("0")), Decimal("44.48"))
        for item in later:
            self.assertEqual(item["tax_rate"], "BAS Excluded")
        self.assertEqual(self.by_row[213]["account"], "404 - Bank Fees")
        for row in [210, 211, 214, 218, 219, 220]:
            self.assertEqual(self.by_row[row]["account"], "493 - Travel - National")

    def test_live_checkpoint_and_subtraction(self):
        checkpoint = self.data["later_batch"]["checkpoint"]
        self.assertEqual(checkpoint["unreconciled_statement_lines"], 24)
        self.assertEqual(checkpoint["fy2025_26_unreconciled_source_rows"], 0)
        self.assertEqual(checkpoint["post_2026_06_30_unreconciled_lines"], 24)
        self.assertEqual(Decimal(checkpoint["book_balance"]), Decimal("29777.21"))
        self.assertEqual(Decimal(checkpoint["statement_balance"]), Decimal("31016.85"))
        self.assertEqual(
            Decimal(self.data["controls"]["before"]["book_balance"])
            + sum((Decimal(item["amount"]) for item in self.by_row.values()), Decimal("0")),
            Decimal(checkpoint["book_balance"]),
        )
        subtraction = self.data["later_batch"]["source_backposting_subtraction"]
        self.assertEqual(subtraction["starting_supported_rows"] - subtraction["posted_rows"], subtraction["remaining_rows"])
        self.assertEqual(
            Decimal(subtraction["starting_supported_debit_total"]) - Decimal(subtraction["posted_debit_total"]),
            Decimal(subtraction["remaining_debit_total"]),
        )

    def test_remaining_supported_inventory_is_exact(self):
        remaining = self.data["later_batch"]["remaining_supported_later_inventory"]
        expected_rows = [222, 223, 224, 227, 230, 233, 234, 243, 244, 245]
        self.assertEqual(remaining["source_rows"], expected_rows)
        self.assertEqual(remaining["count"], 10)
        total = -sum((Decimal(self.source[row]["amount"]) for row in expected_rows), Decimal("0"))
        self.assertEqual(total, Decimal("45.22"))
        self.assertEqual(total, Decimal(remaining["debit_total"]))

    def test_close_and_source_boundaries_remain_explicit(self):
        boundaries = self.data["boundaries"]
        self.assertFalse(boundaries["present_day_complete"])
        self.assertEqual(boundaries["source_coverage_end"], "2026-08-17")
        self.assertEqual(boundaries["year_end_bank_target"], "25086.17")
        self.assertIn("does not prove", boundaries["gift_completion_meaning"])
        self.assertEqual(boundaries["dated_30_june_reconciliation_report"]["status"], "not_captured")

    def test_all_named_evidence_paths_exist(self):
        evidence = list(self.data["boundaries"]["evidence"])
        evidence.extend(self.by_row[160]["evidence"])
        self.assertEqual([path for path in evidence if not (ROOT / path).is_file()], [])


if __name__ == "__main__":
    unittest.main()
