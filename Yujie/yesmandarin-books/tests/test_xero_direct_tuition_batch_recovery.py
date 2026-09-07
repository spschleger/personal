import json
import unittest
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "workpapers/2026-09-08-xero-direct-tuition-batch-recovery.json"
INVENTORY = ROOT / "workpapers/2026-09-08-fy2025-26-credit-evidence-inventory.json"


class DirectTuitionBatchRecoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.audit = json.loads(AUDIT.read_text())
        cls.inventory = json.loads(INVENTORY.read_text())
        cls.rows = cls.audit["transactions"]

    def test_run_attribution_is_unambiguous(self):
        attr = self.audit["run_attribution"]
        self.assertEqual(attr["prior_interrupted_run_posted_count"], 4)
        self.assertEqual(Decimal(attr["prior_interrupted_run_posted_total"]), Decimal("2351.00"))
        self.assertEqual(attr["this_recovery_run_posted_count"], 0)
        self.assertEqual(Decimal(attr["this_recovery_run_posted_total"]), Decimal("0.00"))
        self.assertTrue(all(row["posting_attribution"] == "prior_interrupted_run" for row in self.rows))

    def test_exact_source_population_and_descriptions(self):
        self.assertEqual([row["source_row"] for row in self.rows], [69, 71, 125, 126])
        source = {row["source_row"]: row for row in self.inventory["credit_inventory"]}
        for row in self.rows:
            original = source[row["source_row"]]
            self.assertEqual(row["date"], original["date"])
            self.assertEqual(Decimal(row["amount"]), Decimal(original["amount"]))
            self.assertEqual(row["bank_description"], original["bank_description"])

    def test_posting_fields_and_control_arithmetic(self):
        self.assertEqual(sum(Decimal(row["amount"]) for row in self.rows), Decimal("2351.00"))
        self.assertTrue(all(row["transaction_type"] == "Receive Money" for row in self.rows))
        self.assertTrue(all(row["account"] == "200 - Sales" for row in self.rows))
        self.assertTrue(all(row["tax_rate"] == "BAS Excluded" for row in self.rows))
        control = self.audit["controls"]
        before = control["before_prior_interrupted_run"]
        after = control["after_four_prior_interrupted_run_posts"]
        self.assertEqual(before["unreconciled_statement_lines"] - after["unreconciled_statement_lines"], 4)
        self.assertEqual(Decimal(after["book_balance"]) - Decimal(before["book_balance"]), Decimal("2351.00"))
        self.assertEqual(after["fy2025_26_unreconciled_lines"], 17)
        self.assertEqual(after["post_2026_06_30_unreconciled_lines"], 37)

    def test_bounded_holds_are_preserved(self):
        held = self.audit["held_or_pending"]
        self.assertIn("Held", held["row_163_courtney_mcmillan_680"])
        self.assertIn("Pending", held["row_183_maria_john_345"])
        self.assertIn("Pending", held["row_198_jenny_bisset_618"])
        self.assertIn("No previously posted row was reposted.", self.audit["guardrails"])


if __name__ == "__main__":
    unittest.main()
