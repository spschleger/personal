import json
import unittest
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "workpapers/2026-09-08-xero-final3-and-first-later-supported-batch.json"


class FinalThreeAndLaterBatchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(AUDIT.read_text())
        cls.by_row = {item["source_row"]: item for item in cls.data["transactions"]}

    def test_batch_is_bounded_and_exact(self):
        self.assertEqual(list(self.by_row), [163, 171, 203, 205, 206, 207, 208, 209])
        self.assertEqual(self.data["batch_totals"]["line_count"], 8)
        self.assertEqual(self.data["batch_totals"]["later_period_debit_count"], 6)
        self.assertEqual(Decimal(self.data["batch_totals"]["later_period_debit_total"]), Decimal("283.62"))
        self.assertEqual(Decimal(self.data["batch_totals"]["net_movement"]), Decimal("381.94"))

    def test_exact_account_and_tax_treatments(self):
        expected = {
            163: ("Courtney Mc Millan", "680.00", "200 - Sales"),
            171: ("Order Lemon", "-14.44", "420 - Entertainment"),
            203: ("Transport for NSW", "-7.52", "493 - Travel - National"),
            205: ("Covau Energy", "-239.67", "445 - Light, Power, Heating"),
            206: ("Transport for NSW", "-12.17", "493 - Travel - National"),
            207: ("Transport for NSW", "-3.76", "493 - Travel - National"),
            208: ("Google Workspace", "-12.98", "485 - Subscriptions"),
            209: ("Transport for NSW", "-7.52", "493 - Travel - National"),
        }
        for row, (contact, amount, account) in expected.items():
            item = self.by_row[row]
            self.assertEqual(item["contact"], contact)
            self.assertEqual(item["amount"], amount)
            self.assertEqual(item["account"], account)
            self.assertEqual(item["tax_rate"], "BAS Excluded")
            self.assertIn("posted", item["posting_status"])

    def test_queue_and_balance_controls(self):
        before = self.data["controls"]["before"]
        after = self.data["controls"]["after"]
        self.assertEqual(before["unreconciled_statement_lines"], 40)
        self.assertEqual(after["unreconciled_statement_lines"], 32)
        self.assertEqual(after["fy2025_26_unreconciled_lines"], 1)
        self.assertEqual(after["post_2026_06_30_unreconciled_lines"], 31)
        self.assertEqual(Decimal(after["statement_balance"]), Decimal("31016.85"))
        self.assertEqual(Decimal(after["book_balance"]), Decimal("30121.69"))
        self.assertEqual(
            Decimal(after["book_balance"]) - Decimal(before["book_balance"]),
            Decimal("381.94"),
        )
        remaining = self.data["controls"]["remaining_supported_later_batch"]
        self.assertEqual(remaining["line_count"], 17)
        self.assertEqual(Decimal(remaining["debit_total"]), Decimal("89.70"))

    def test_mark_zheng_remains_held_with_existing_account_proposal(self):
        held = self.data["held_fy2025_26"]
        proposal = held["existing_account_proposal"]
        self.assertEqual(held["status"], "held_not_posted")
        self.assertEqual(proposal["account"], "429 - General Expenses")
        self.assertEqual(proposal["actual_xero_description"], "General expenses related to the running of the business.")
        self.assertNotIn("Entertainment", proposal["account"])
        self.assertIn("approval", proposal["reason"].lower())

    def test_boundaries_remain_explicit(self):
        boundaries = self.data["boundaries_and_remaining_work"]
        self.assertEqual(boundaries["year_end_bank_target"], "25086.17")
        self.assertEqual(boundaries["source_coverage_end"], "2026-08-17")
        self.assertIn("not closed", boundaries["fy2025_26_not_closed"])
        self.assertIn("does not claim present-day completeness", boundaries["present_day_constraint"])
        self.assertIn("Stripe", boundaries["stripe_controls"])

    def test_all_named_evidence_paths_exist(self):
        paths = []
        paths.extend(self.data["controls"]["evidence"])
        for item in self.data["transactions"]:
            evidence = item.get("evidence", [])
            paths.extend([evidence] if isinstance(evidence, str) else evidence)
        paths.extend(self.data["held_fy2025_26"]["chart_evidence"])
        self.assertEqual([path for path in paths if not (ROOT / path).is_file()], [])


if __name__ == "__main__":
    unittest.main()
