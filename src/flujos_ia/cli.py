from __future__ import annotations

import argparse
from pathlib import Path

from .fixtures import PROPOSALS, REQUESTS, REQUIREMENTS, RULES
from .render import render_comparison, render_requests
from .workflows import compare_proposals, organize_requests


def main() -> int:
    parser = argparse.ArgumentParser(description="Ejecuta demos offline de flujos de trabajo con IA")
    parser.add_argument("--demo", choices=("1", "2", "all"), default="all")
    parser.add_argument("--output-dir", type=Path, default=Path("demo/results"))
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    if args.demo in ("1", "all"):
        result = organize_requests(REQUESTS, RULES)
        path = args.output_dir / "demo-1-organizar-solicitudes.md"
        path.write_text(render_requests(result), encoding="utf-8")
        print(f"Demo 1: {path}")

    if args.demo in ("2", "all"):
        result = compare_proposals(REQUIREMENTS, PROPOSALS)
        path = args.output_dir / "demo-2-comparar-propuestas.md"
        path.write_text(render_comparison(result), encoding="utf-8")
        print(f"Demo 2: {path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
