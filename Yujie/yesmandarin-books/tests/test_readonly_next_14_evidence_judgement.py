import csv
import json
import unittest
from datetime import datetime
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "workpapers/2026-09-08-readonly-next-14-evidence-judgement-and-draft-tax-pack.json"
WORKLIST = ROOT / "workpapers/2026-08-25-account-1913-reconciliation-worklist.csv"
EVIDENCE = ROOT / "workpapers/evidence/2026-09-08-readonly-next-14-and-draft-tax-pack"
EXPECTED_ROWS = [204, 212, 217, 226, 229, 232, 235, 237, 238, 242, 247, 248, 250, 251]


class ReadonlyNext14EvidenceJudgementTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(AUDIT.read_text())
        with WORKLIST.open(newline="", encoding="utf-8-sig") as handle:
            cls.source = {int(row["source_row"]): row for row in csv.DictReader(handle)}

    def test_exact_inventory_order_and_count(self):
        self.assertEqual(self.data["controls"]["exact_source_rows"], EXPECTED_ROWS)
        self.assertEqual(self.data["controls"]["row_count"], 14)
        self.assertEqual([row["source_row"] for row in self.data["rows"]], EXPECTED_ROWS)
        self.assertEqual(len({row["source_row"] for row in self.data["rows"]}), 14)

    def test_every_row_matches_bank_worklist(self):
        for row in self.data["rows"]:
            source = self.source[row["source_row"]]
            expected_date = datetime.strptime(source["date"], "%d/%m/%Y").date().isoformat()
            self.assertEqual(row["date"], expected_date)
            self.assertEqual(Decimal(row["amount"]), Decimal(source["amount"]))
            self.assertEqual(row["bank_description"], source["description"])
            self.assertGreater(row["date"], "2026-06-30")

    def test_exact_debit_credit_and_net_totals(self):
        amounts = [Decimal(row["amount"]) for row in self.data["rows"]]
        debits = sum(-amount for amount in amounts if amount < 0)
        credits = sum(amount for amount in amounts if amount > 0)
        self.assertEqual(debits, Decimal("1221.94"))
        self.assertEqual(credits, Decimal("2506.80"))
        self.assertEqual(credits - debits, Decimal("1284.86"))
        controls = self.data["controls"]
        self.assertEqual(
            Decimal(controls["source_statement_balance_through_17_august_2026"])
            - Decimal(controls["xero_book_balance_at_14_row_checkpoint"]),
            Decimal("1284.86"),
        )

    def test_judgements_are_proposals_not_writes(self):
        for row in self.data["rows"]:
            self.assertTrue(row["evidence_judgement"])
            self.assertTrue(row["proposed_treatment"])
        actions = self.data["actions_taken"]
        self.assertEqual(actions["xero_writes"], 0)
        self.assertEqual(actions["matches_selected"], 0)
        self.assertEqual(actions["permissions_changed"], 0)
        self.assertEqual(actions["outbound_actions"], 0)

    def test_taobao_scope_is_one_combined_confirmation(self):
        taobao = [row for row in self.data["rows"] if row["source_row"] in {212, 226, 229, 232}]
        self.assertEqual(sum(-Decimal(row["amount"]) for row in taobao), Decimal("113.94"))
        for row in taobao:
            self.assertIn("scope", row["missing_fact"].lower())
            self.assertNotIn("what item", row["missing_fact"].lower())
        self.assertIn("one combined scope-extension confirmation", taobao[0]["proposed_treatment"])

    def test_distinct_maria_receipt_and_contractors(self):
        by_row = {row["source_row"]: row for row in self.data["rows"]}
        self.assertIn("distinct receipt", by_row[235]["evidence_judgement"])
        self.assertIn("INV-0078", by_row[235]["evidence_judgement"])
        self.assertIsNone(by_row[235]["missing_fact"])
        for source_row in (237, 238):
            self.assertIn("No local supplier invoice", by_row[source_row]["evidence_judgement"])
            self.assertIn("existing suitable account", by_row[source_row]["proposed_treatment"])

    def test_year_end_control_is_not_tax_close(self):
        bank = self.data["controls"]["fy2025_26_bank_control"]
        self.assertEqual(bank["status"], "complete")
        for key in ("xero_balance", "calculated_statement_balance", "bank_statement_ending_balance"):
            self.assertEqual(Decimal(bank[key]), Decimal("25086.17"))
        for key in ("outstanding_payments", "outstanding_receipts", "unreconciled_statement_lines"):
            self.assertEqual(Decimal(bank[key]), Decimal("0.00"))
        self.assertEqual(self.data["controls"]["tax_close"]["status"], "not_complete")
        self.assertIn("Stripe", self.data["report_artifacts"]["provisional_label"])

    def test_actual_exports_and_visible_balance_sheet_evidence_exist(self):
        reports = self.data["report_artifacts"]
        for key in ("profit_and_loss_pdf", "bank_reconciliation_pdf"):
            path = ROOT / reports[key]["path"]
            self.assertTrue(path.is_file(), path)
            self.assertTrue(path.read_bytes().startswith(b"%PDF"), path)
        self.assertEqual(reports["balance_sheet"]["pdf_status"], "not_exported")
        balance_ax = ROOT / reports["balance_sheet"]["visible_report_evidence"]
        labels = [str(element.get("label", "")) for element in json.loads(balance_ax.read_text())["elements"]]
        self.assertIn("Balance Sheet", labels)
        self.assertIn("30 June 2026", labels)

    def test_live_find_match_no_result_evidence(self):
        files_and_queries = {
            "find-match-suguru-no-results-ax.json": "Suguru",
            "find-match-nitchakan-no-results-ax.json": "Nitchakan",
            "find-match-matthew-harvey-no-results-ax.json": "Matthew Harvey",
            "find-match-ruthy-no-results-ax.json": "Ruthy",
        }
        for filename, query in files_and_queries.items():
            labels = [
                str(element.get("label", ""))
                for element in json.loads((EVIDENCE / filename).read_text())["elements"]
            ]
            self.assertIn(query, labels)
            self.assertTrue(
                any(label.startswith("Your search returned no results") for label in labels),
                filename,
            )


if __name__ == "__main__":
    unittest.main()
