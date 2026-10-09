import json
import unittest
from pathlib import Path


DATASET = Path(__file__).parents[1] / "dataset" / "expense_decisions.jsonl"


class DatasetTests(unittest.TestCase):
    def test_dataset_has_synthetic_draft_cases(self):
        rows = [json.loads(line) for line in DATASET.read_text(encoding="utf-8").splitlines() if line.strip()]
        self.assertEqual(len(rows), 4)
        for row in rows:
            self.assertEqual(row["language"], "es")
            self.assertIn("etiqueta_borrador", row["tags"])
            self.assertEqual(set(row["questions"]), set(row["expected"]))

    def test_tax_axes_are_separate(self):
        row = json.loads(DATASET.read_text(encoding="utf-8").splitlines()[0])
        self.assertIn("renta_tratamiento", row["expected"])
        self.assertIn("igv_credito", row["expected"])
        self.assertNotIn("sunat_acepta", row["expected"])


if __name__ == "__main__":
    unittest.main()
