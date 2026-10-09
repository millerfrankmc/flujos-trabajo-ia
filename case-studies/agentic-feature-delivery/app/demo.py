from decimal import Decimal

from .rendiciones import Rendicion, exportar_csv


RENDICIONES = [
    Rendicion("ana", "2030-05-03", 'ACME, "Servicios"', "software", Decimal("120.5"), "USD"),
    Rendicion("luis", "2030-05-01", "Proveedor Sur", "transporte", Decimal("40"), "USD"),
    Rendicion("ana", "2030-05-02", "Proveedor Norte", "formacion", Decimal("75.25"), "USD"),
]


if __name__ == "__main__":
    print("CSV completo:")
    print(exportar_csv(RENDICIONES))
    print("CSV filtrado para ana:")
    print(exportar_csv(RENDICIONES, empleado="ana"))
