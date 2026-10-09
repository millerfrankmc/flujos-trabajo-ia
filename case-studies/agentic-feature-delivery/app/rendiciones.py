from __future__ import annotations

import csv
import io
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from typing import Iterable


@dataclass(frozen=True)
class Rendicion:
    empleado: str
    fecha: str
    proveedor: str
    categoria: str
    importe: Decimal
    moneda: str

    def __post_init__(self) -> None:
        if not self.empleado.strip():
            raise ValueError("empleado no puede estar vacío")
        if not self.fecha.strip():
            raise ValueError("fecha no puede estar vacía")
        if not self.proveedor.strip():
            raise ValueError("proveedor no puede estar vacío")
        if self.importe < Decimal("0"):
            raise ValueError("importe no puede ser negativo")


def exportar_csv(
    rendiciones: Iterable[Rendicion],
    *,
    empleado: str | None = None,
) -> str:
    """Devuelve un CSV determinista sin mutar la colección recibida."""
    items = list(rendiciones)
    if empleado is not None:
        items = [item for item in items if item.empleado == empleado]

    items.sort(key=lambda item: (item.fecha, item.empleado, item.proveedor))

    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(["empleado", "fecha", "proveedor", "categoria", "importe", "moneda"])
    for item in items:
        try:
            amount = Decimal(item.importe).quantize(Decimal("0.01"))
        except (InvalidOperation, ValueError) as exc:
            raise ValueError("importe inválido") from exc
        writer.writerow(
            [
                item.empleado,
                item.fecha,
                item.proveedor,
                item.categoria,
                f"{amount:.2f}",
                item.moneda,
            ]
        )
    return output.getvalue()
