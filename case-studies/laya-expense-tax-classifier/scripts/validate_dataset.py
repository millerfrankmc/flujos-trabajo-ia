from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "dataset" / "expense_decisions.jsonl"
ALLOWED = {
    "renta_tratamiento": {"probable_deducible", "probable_reparable", "condicionado", "insuficiente_evidencia"},
    "igv_credito": {"probable_creditable", "probable_no_creditable", "condicionado", "insuficiente_evidencia"},
    "documentacion": {"completa", "incompleta", "inconsistente"},
    "revision": {"estandar", "contador", "bloqueada"},
}


def main() -> int:
    rows = [json.loads(line) for line in DATASET.read_text(encoding="utf-8").splitlines() if line.strip()]
    assert len(rows) == 4, f"se esperaban 4 casos sintéticos, encontrados {len(rows)}"
    for index, row in enumerate(rows, start=1):
        assert isinstance(row["state"], str) and row["state"]
        assert set(row["questions"]) == set(row["expected"]), f"caso {index}: questions/expected no coinciden"
        assert row["language"] == "es"
        assert "etiqueta_borrador" in row["tags"]
        for key, choices in ALLOWED.items():
            assert row["expected"][key] in choices, f"caso {index}: etiqueta inválida para {key}"
        for key, question in row["questions"].items():
            assert question["type"] == "choice", f"caso {index}: {key} debe ser choice"
            assert set(question["criteria"]) >= {row["expected"][key]}, f"caso {index}: expected ausente en criteria"
    print(f"Dataset válido: {len(rows)} casos sintéticos; etiquetas preliminares.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
