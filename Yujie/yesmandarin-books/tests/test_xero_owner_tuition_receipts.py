import json
import unittest
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "workpapers/2026-09-08-xero-owner-tuition-receipts.json"


class OwnerTuitionReceiptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(AUDIT.read_text())
        cls.by_row = {item["source_row"]: item for item in cls.data["transactions"]}

    def test_completed_batch_is_exactly_four(self):
        self.assertEqual(list(self.by_row), [164, 178, 193, 196])
        self.assertEqual(self.data["pending_in_this_batch"], [])
        self.assertEqual(
            sum((Decimal(item["amount"]) for item in self.data["transactions"]), Decimal("0")),
            Decimal("2633.00"),
        )

    def test_all_four_have_direct_sales_treatment(self):
        for item in self.data["transactions"]:
            self.assertEqual(item["transaction_type"], "Receive Money")
            self.assertEqual(item["account"], "200 - Sales")
            self.assertEqual(item["tax_rate"], "BAS Excluded")
            self.assertEqual(item["amounts_tax_basis"], "Tax Exclusive")
            self.assertIn("posted", item["posting_status"])
            self.assertIn("live_verified", item["posting_status"])

    def test_alexander_exact_readback(self):
        alexander = self.by_row[193]
        self.assertEqual(alexander["date"], "2026-06-23")
        self.assertEqual(alexander["amount"], "558.00")
        self.assertEqual(alexander["contact"], "Alexander O'Neill")
        self.assertEqual(
            alexander["bank_description"],
            "Fast Transfer From O'Neill A F ALEXANDER O'NEILL",
        )
        for exact_text in (
            "Receive money",
            "200 - Sales",
            "BAS Excluded",
            "Tax Exclusive",
            "Reconciled by Felicity Cao on 8 Sep 2026 at 12:59PM",
            "Credit payment on 23 June 2026 for 558.00",
        ):
            self.assertIn(exact_text, alexander["verification"])

    def test_jen_exact_readback(self):
        jen = self.by_row[196]
        self.assertEqual(jen["date"], "2026-06-26")
        self.assertEqual(jen["amount"], "618.00")
        self.assertEqual(jen["contact"], "Jen Rollins")
        self.assertEqual(jen["bank_description"], "Fast Transfer From Rollins J E Jen Rollins")
        for exact_text in (
            "Receive money",
            "200 - Sales",
            "BAS Excluded",
            "Tax Exclusive",
            "Reconciled by Felicity Cao on 8 Sep 2026 at 13:17PM",
            "Credit payment on 26 June 2026 for 618.00",
        ):
            self.assertIn(exact_text, jen["verification"])

    def test_queue_and_balance_controls(self):
        before = self.data["controls"]["before"]
        after = self.data["controls"]["after_all_four"]
        self.assertEqual(before["unreconciled_statement_lines"], 44)
        self.assertEqual(after["unreconciled_statement_lines"], 40)
        self.assertEqual(after["fy2025_26_unreconciled_lines"], 3)
        self.assertEqual(after["post_2026_06_30_unreconciled_lines"], 37)
        self.assertEqual(Decimal(after["statement_balance"]), Decimal("31016.85"))
        self.assertEqual(Decimal(after["book_balance"]), Decimal("29739.75"))
        self.assertEqual(
            Decimal(after["book_balance"]) - Decimal(before["book_balance"]),
            Decimal("2633.00"),
        )

    def test_evidence_paths_exist(self):
        paths = []
        for item in self.data["transactions"]:
            paths.extend(item["evidence"])
        paths.extend(
            [
                self.data["controls"]["after_first_pair"]["evidence"],
                self.data["controls"]["after_first_three"]["evidence"],
                self.data["controls"]["after_all_four"]["evidence"],
            ]
        )
        self.assertEqual([path for path in paths if not (ROOT / path).is_file()], [])

    def test_held_items_stay_explicit(self):
        held = " ".join(self.data["held"])
        self.assertIn("Courtney McMillan $680", held)
        self.assertIn("Mark Zheng $300", held)
        self.assertIn("Order Lemon $14.44", held)


if __name__ == "__main__":
    unittest.main()
