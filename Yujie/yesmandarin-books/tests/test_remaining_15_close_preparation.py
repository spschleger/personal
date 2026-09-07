import csv
import json
import unittest
from datetime import datetime
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "workpapers/2026-09-08-fy2025-26-remaining-15-close-preparation.json"
WORKLIST = ROOT / "workpapers/2026-08-25-account-1913-reconciliation-worklist.csv"


class RemainingFifteenClosePreparationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(INVENTORY.read_text())
        cls.credits = cls.data["remaining_credits"]
        cls.debits = cls.data["remaining_debits"]
        with WORKLIST.open(newline="") as handle:
            cls.worklist = {int(row["source_row"]): row for row in csv.DictReader(handle)}

    def test_checkpoint_is_exact(self):
        checkpoint = self.data["checkpoint"]
        self.assertEqual(checkpoint["unreconciled_statement_lines"], 52)
        self.assertEqual(checkpoint["fy2025_26_unreconciled_lines"], 15)
        self.assertEqual(checkpoint["post_2026_06_30_unreconciled_lines"], 37)
        self.assertEqual(Decimal(checkpoint["book_balance"]), Decimal("25610.57"))

    def test_exact_seven_credit_population_includes_courtney(self):
        self.assertEqual(len(self.credits), 7)
        self.assertEqual(
            [row["source_row"] for row in self.credits],
            [156, 163, 164, 178, 192, 193, 196],
        )
        self.assertEqual(sum(Decimal(row["amount"]) for row in self.credits), Decimal("5171.00"))
        courtney = next(row for row in self.credits if row["payer"] == "Courtney McMillan")
        self.assertEqual(courtney["amount"], "680.00")
        self.assertIn("student", courtney["bank_description"].lower())
        self.assertIsNone(courtney["genuine_missing_fact"])

    def test_exact_eight_debit_population(self):
        self.assertEqual(len(self.debits), 8)
        self.assertEqual(
            [row["source_row"] for row in self.debits],
            [24, 133, 142, 160, 168, 171, 172, 174],
        )
        self.assertEqual(-sum(Decimal(row["amount"]) for row in self.debits), Decimal("676.26"))

    def test_all_fifteen_rows_agree_exactly_to_bank_source(self):
        for row in self.credits + self.debits:
            source = self.worklist[row["source_row"]]
            self.assertEqual(
                datetime.strptime(source["date"], "%d/%m/%Y").strftime("%Y-%m-%d"),
                row["date"],
            )
            self.assertEqual(Decimal(source["amount"]), Decimal(row["amount"]))
            self.assertEqual(source["description"], row["bank_description"])

    def test_declared_controls_recompute(self):
        controls = self.data["controls"]
        self.assertEqual(controls["remaining_count"], len(self.credits) + len(self.debits))
        self.assertEqual(controls["credit_count"], len(self.credits))
        self.assertEqual(controls["debit_count"], len(self.debits))
        self.assertEqual(Decimal(controls["credit_total"]), sum(Decimal(row["amount"]) for row in self.credits))
        debit_total = -sum(Decimal(row["amount"]) for row in self.debits)
        self.assertEqual(Decimal(controls["debit_total"]), debit_total)
        self.assertEqual(Decimal(controls["net_movement"]), Decimal(controls["credit_total"]) - debit_total)

    def test_questions_are_grouped_and_do_not_repeat_business_use(self):
        questions = self.data["concise_unresolved_factual_questions"]
        self.assertEqual(len(questions), 7)
        rendered = " ".join(questions)
        for amount in ("$1,300", "$177", "$1,280", "$558", "$618", "$17.47", "$31.93", "$6.88", "$25.54", "$200", "$300", "$14.44"):
            self.assertIn(amount, rendered)
        self.assertNotIn("business use", rendered.lower())
        self.assertNotIn("printer model", rendered.lower())

    def test_kogan_and_printer_boundaries_are_honest(self):
        kogan = next(row for row in self.debits if row["source_row"] == 133)
        self.assertIn("makes service/prepaid credit plausible", kogan["source_evidence"])
        self.assertIn("does not prove", kogan["source_evidence"])
        printer = next(row for row in self.debits if row["source_row"] == 142)
        self.assertIsNone(printer["genuine_missing_fact"])
        self.assertIn("not automatically needed", printer["why_no_question"])
        self.assertIn("No account or tax treatment", self.data["guardrails"][1])

    def test_fresh_read_only_evidence_exists(self):
        verification = self.data["fresh_read_only_xero_verification"]
        self.assertIn("No Xero form was submitted", verification["method"])
        for name in ("anthony_dengate", "jenny_bisset"):
            evidence = verification[name]["evidence"]
            paths = evidence if isinstance(evidence, list) else [evidence]
            for path in paths:
                self.assertTrue((ROOT / path).is_file(), path)


if __name__ == "__main__":
    unittest.main()
