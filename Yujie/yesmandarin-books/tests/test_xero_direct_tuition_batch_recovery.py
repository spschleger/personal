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
        self.assertEqual(attr["this_recovery_run_posted_count"], 2)
        self.assertEqual(Decimal(attr["this_recovery_run_posted_total"]), Decimal("963.00"))
        self.assertEqual([row["posting_attribution"] for row in self.rows[:4]], ["prior_interrupted_run"] * 4)
        self.assertEqual([row["posting_attribution"] for row in self.rows[4:]], ["this_recovery_run"] * 2)

    def test_exact_source_population_and_descriptions(self):
        self.assertEqual([row["source_row"] for row in self.rows], [69, 71, 125, 126, 183, 198])
        source = {row["source_row"]: row for row in self.inventory["credit_inventory"]}
        for row in self.rows:
            original = source[row["source_row"]]
            self.assertEqual(row["date"], original["date"])
            self.assertEqual(Decimal(row["amount"]), Decimal(original["amount"]))
            self.assertEqual(row["bank_description"], original["bank_description"])

    def test_posting_fields_and_control_arithmetic(self):
        self.assertEqual(sum(Decimal(row["amount"]) for row in self.rows), Decimal("3314.00"))
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
        final = control["after_two_recovery_run_posts"]
        self.assertEqual(after["unreconciled_statement_lines"] - final["unreconciled_statement_lines"], 2)
        self.assertEqual(Decimal(final["book_balance"]) - Decimal(after["book_balance"]), Decimal("963.00"))
        self.assertEqual(final["fy2025_26_unreconciled_lines"], 15)
        self.assertEqual(final["post_2026_06_30_unreconciled_lines"], 37)

    def test_bounded_holds_are_preserved(self):
        held = self.audit["held_or_pending"]
        self.assertIn("Held", held["row_163_courtney_mcmillan_680"])
        self.assertNotIn("row_183_maria_john_345", held)
        self.assertNotIn("row_198_jenny_bisset_618", held)
        self.assertIn("No previously posted row was reposted.", self.audit["guardrails"])

    def test_recovery_evidence_files_exist(self):
        for row in self.rows[4:]:
            self.assertGreaterEqual(len(row["evidence"]), 6)
            for evidence in row["evidence"]:
                self.assertTrue((ROOT / evidence).is_file(), evidence)

    def test_anthony_repair_distinguishes_old_inference_from_fresh_detail(self):
        anthony = next(row for row in self.rows if row["source_row"] == 126)
        self.assertIn("Fresh visible-Chrome readback", anthony["verification"])
        self.assertIn("anthony-postwrite.png", anthony["verification"])
        self.assertIn("was not exact posted-detail evidence", anthony["verification"])
        self.assertIn("2:39AM", anthony["verification"])
        for evidence in anthony["evidence"]:
            self.assertTrue((ROOT / evidence).is_file(), evidence)
        self.assertTrue(
            any(evidence.endswith("anthony-posted-detail-fresh.png") for evidence in anthony["evidence"])
        )

    def test_jenny_fresh_posted_detail_is_preserved(self):
        jenny = next(row for row in self.rows if row["source_row"] == 198)
        self.assertIn("3:36AM", jenny["verification"])
        self.assertIn("Tax Exclusive", jenny["verification"])
        self.assertIn(
            "workpapers/evidence/2026-09-08-direct-tuition-batch/jenny-posted-detail.png",
            jenny["evidence"],
        )


if __name__ == "__main__":
    unittest.main()
