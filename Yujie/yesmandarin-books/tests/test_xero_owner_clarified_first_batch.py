import json
from decimal import Decimal
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "workpapers/2026-09-08-xero-owner-clarified-first-batch.json"


class OwnerClarifiedFirstBatchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(AUDIT.read_text())

    def test_exact_bounded_population(self):
        rows = [item["source_row"] for item in self.data["transactions"]]
        self.assertEqual(rows, [156, 192, 24, 168, 172, 174, 133, 142])
        self.assertEqual(len(rows), 8)
        self.assertEqual(len(rows), len(set(rows)))

    def test_amount_and_queue_controls(self):
        credits = sum(
            Decimal(item["amount"])
            for item in self.data["transactions"]
            if Decimal(item["amount"]) > 0
        )
        debits = -sum(
            Decimal(item["amount"])
            for item in self.data["transactions"]
            if Decimal(item["amount"]) < 0
        )
        self.assertEqual(credits, Decimal("1858.00"))
        self.assertEqual(debits, Decimal("361.82"))
        self.assertEqual(credits - debits, Decimal("1496.18"))
        controls = self.data["controls"]
        self.assertEqual(controls["before"]["unreconciled_statement_lines"], 52)
        self.assertEqual(controls["after"]["unreconciled_statement_lines"], 44)
        self.assertEqual(
            Decimal(controls["after"]["book_balance"])
            - Decimal(controls["before"]["book_balance"]),
            Decimal("1496.18"),
        )

    def test_accounts_tax_and_invoice_matches(self):
        by_row = {item["source_row"]: item for item in self.data["transactions"]}
        self.assertEqual(by_row[156]["existing_invoice"], "INV-0070")
        self.assertEqual(by_row[192]["existing_invoice"], "INV-0076")
        self.assertEqual(by_row[133]["account"], "489 - Telephone & Internet")
        for row in (24, 168, 172, 174, 142):
            self.assertEqual(by_row[row]["account"], "453 - Office Expenses")
        self.assertTrue(all(item["tax_rate"] == "BAS Excluded" for item in by_row.values()))

    def test_evidence_paths_exist(self):
        paths = []
        for item in self.data["transactions"]:
            evidence = item["evidence"]
            paths.extend(evidence if isinstance(evidence, list) else [evidence])
        paths.append(self.data["controls"]["evidence"])
        missing = [path for path in paths if not (ROOT / path).is_file()]
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
