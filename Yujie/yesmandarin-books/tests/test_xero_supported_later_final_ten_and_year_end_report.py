import csv
import json
import unittest
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "workpapers/2026-09-08-xero-supported-later-final-ten-and-year-end-report.json"
WORKLIST = ROOT / "workpapers/2026-08-25-account-1913-reconciliation-worklist.csv"


class SupportedLaterFinalTenAndYearEndReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(AUDIT.read_text())
        with WORKLIST.open(newline="", encoding="utf-8-sig") as handle:
            cls.source = {int(row["source_row"]): row for row in csv.DictReader(handle)}

    def test_exact_supported_rows_and_source_facts(self):
        expected = [222, 223, 224, 227, 230, 233, 234, 243, 244, 245]
        actual = [row["source_row"] for row in self.data["transactions"]]
        self.assertEqual(actual, expected)
        for row in self.data["transactions"]:
            source = self.source[row["source_row"]]
            self.assertEqual(row["date"], source["date"])
            self.assertEqual(row["amount"], source["amount"])
            self.assertEqual(row["bank_description"], source["description"])
            self.assertEqual(row["tax_rate"], "BAS Excluded")
            self.assertEqual(row["transaction_type"], "Spend Money")

    def test_supported_totals_and_subtraction(self):
        rows = self.data["transactions"]
        total = sum(-Decimal(row["amount"]) for row in rows)
        self.assertEqual(total, Decimal("45.22"))
        controls = self.data["controls"]
        self.assertEqual(controls["batch_count"], 10)
        self.assertEqual(Decimal(controls["batch_debit_total"]), total)
        subtraction = controls["source_existing_posted_subtraction"]
        self.assertEqual(subtraction["supported_proposal_count"] - subtraction["previously_audited_posted_count"], 10)
        self.assertEqual(
            Decimal(subtraction["supported_proposal_debit_total"])
            - Decimal(subtraction["previously_audited_posted_debit_total"]),
            Decimal("45.22"),
        )
        self.assertEqual(subtraction["postwrite_supported_remaining_count"], 0)

    def test_queue_and_book_controls(self):
        controls = self.data["controls"]
        self.assertEqual(controls["before"]["unreconciled_statement_lines"], 24)
        self.assertEqual(controls["after"]["unreconciled_statement_lines"], 14)
        self.assertEqual(
            Decimal(controls["before"]["book_balance"])
            - Decimal(controls["batch_debit_total"]),
            Decimal(controls["after"]["book_balance"]),
        )
        checkpoints = controls["queue_and_book_after_each_post"]
        self.assertEqual([item["unreconciled_statement_lines"] for item in checkpoints], list(range(23, 13, -1)))
        self.assertEqual(checkpoints[-1]["book_balance"], "29731.99")
        self.assertEqual(controls["after"]["statement_balance"], "31016.85")

    def test_exact_remaining_unsupported_inventory(self):
        inventory = self.data["remaining_unsupported_later_inventory"]
        expected = [204, 212, 217, 226, 229, 232, 235, 237, 238, 242, 247, 248, 250, 251]
        self.assertEqual(inventory["source_rows"], expected)
        self.assertEqual(inventory["count"], 14)
        rows = inventory["transactions"]
        self.assertEqual([row["source_row"] for row in rows], expected)
        for row in rows:
            source = self.source[row["source_row"]]
            self.assertEqual(row["date"], source["date"])
            self.assertEqual(row["amount"], source["amount"])
            self.assertEqual(row["bank_description"], source["description"])
        debits = sum(-Decimal(row["amount"]) for row in rows if Decimal(row["amount"]) < 0)
        credits = sum(Decimal(row["amount"]) for row in rows if Decimal(row["amount"]) > 0)
        self.assertEqual(debits, Decimal(inventory["debit_total"]))
        self.assertEqual(credits, Decimal(inventory["credit_total"]))
        self.assertEqual(debits, Decimal("1221.94"))
        self.assertEqual(credits, Decimal("2506.80"))

    def test_postwrite_ax_contains_each_exact_row_once(self):
        evidence = ROOT / "workpapers/evidence/2026-09-08-supported-later-ten/account-transactions-ten-exact-ax.json"
        elements = json.loads(evidence.read_text())["elements"]
        visible = [
            element
            for element in elements
            if element.get("index", 10_000) < 700
            and element.get("bounds")
            and element["bounds"][0] > 0
            and element["bounds"][1] > 0
        ]
        groups = {}
        for element in visible:
            groups.setdefault(element["bounds"][1], set()).add(str(element.get("label", "")))
        expected = [
            ("11 Aug 2026", "Transport for NSW", "3.76"),
            ("11 Aug 2026", "Transport for NSW", "9.14"),
            ("11 Aug 2026", "Transport for NSW", "3.03"),
            ("4 Aug 2026", "Google Workspace", "12.98"),
            ("4 Aug 2026", "Commonwealth Bank", "0.25"),
            ("28 Jul 2026", "Commonwealth Bank", "2.08"),
            ("23 Jul 2026", "Commonwealth Bank", "0.39"),
            ("14 Jul 2026", "Transport for NSW", "2.31"),
            ("14 Jul 2026", "Transport for NSW", "3.76"),
            ("14 Jul 2026", "Transport for NSW", "7.52"),
        ]
        for date, contact, amount in expected:
            matches = [labels for labels in groups.values() if {date, contact, amount} <= labels]
            self.assertEqual(len(matches), 1, (date, contact, amount))

    def test_year_end_report_balances_exactly(self):
        report = self.data["year_end_bank_reconciliation_report"]
        self.assertEqual(report["report_date"], "2026-06-30")
        for key in (
            "bank_statement_ending_balance",
            "balance_in_xero",
            "statement_balance_calculated",
        ):
            self.assertEqual(Decimal(report[key]), Decimal("25086.17"))
        for key in (
            "outstanding_payments",
            "outstanding_receipts",
            "unreconciled_statement_lines",
            "calculated_balance_out_by",
        ):
            self.assertEqual(Decimal(report[key]), Decimal("0.00"))
        self.assertFalse(self.data["boundaries"]["tax_year_closed"])
        self.assertFalse(self.data["boundaries"]["present_day_complete"])
        self.assertEqual(self.data["boundaries"]["source_coverage_end"], "2026-08-17")
        evidence = ROOT / "workpapers/evidence/2026-09-08-supported-later-ten/reconciliation-report-30-june-2026-ax.json"
        labels = [str(element.get("label", "")) for element in json.loads(evidence.read_text())["elements"]]
        self.assertIn("As at 30 June 2026", labels)
        self.assertGreaterEqual(labels.count("25,086.17"), 3)
        self.assertIn("Plus unreconciled statement lines", labels)
        self.assertIn("Calculated balance out by", labels)

    def test_evidence_paths_exist(self):
        paths = list(self.data["evidence"])
        paths.extend(self.data["year_end_bank_reconciliation_report"]["evidence"])
        paths.extend(row["postwrite_evidence"] for row in self.data["transactions"])
        for relative in set(paths):
            self.assertTrue((ROOT / relative).is_file(), relative)


if __name__ == "__main__":
    unittest.main()
