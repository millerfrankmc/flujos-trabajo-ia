import csv
import io
import unittest
from decimal import Decimal

from app.rendiciones import Rendicion, exportar_csv


class ExportarRendicionesTests(unittest.TestCase):
    def setUp(self):
        self.items = [
            Rendicion("ana", "2030-05-03", 'ACME, "Servicios"', "software", Decimal("120.5"), "USD"),
            Rendicion("luis", "2030-05-01", "Proveedor Sur", "transporte", Decimal("40"), "USD"),
            Rendicion("ana", "2030-05-02", "Proveedor Norte", "formacion", Decimal("75.25"), "USD"),
        ]

    def test_exporta_cabecera_y_formato_monetario(self):
        rows = list(csv.DictReader(io.StringIO(exportar_csv(self.items))))
        self.assertEqual(rows[0]["importe"], "40.00")
        self.assertEqual(rows[1]["importe"], "75.25")
        self.assertEqual(rows[2]["importe"], "120.50")
        self.assertEqual(list(rows[0]), ["empleado", "fecha", "proveedor", "categoria", "importe", "moneda"])

    def test_ordena_por_fecha(self):
        rows = list(csv.DictReader(io.StringIO(exportar_csv(self.items))))
        self.assertEqual([row["empleado"] for row in rows], ["luis", "ana", "ana"])

    def test_escapa_proveedor_csv(self):
        rows = list(csv.DictReader(io.StringIO(exportar_csv(self.items))))
        self.assertEqual(rows[2]["proveedor"], 'ACME, "Servicios"')

    def test_filtra_por_empleado(self):
        rows = list(csv.DictReader(io.StringIO(exportar_csv(self.items, empleado="ana"))))
        self.assertEqual(len(rows), 2)
        self.assertTrue(all(row["empleado"] == "ana" for row in rows))

    def test_rechaza_importe_negativo(self):
        with self.assertRaises(ValueError):
            Rendicion("ana", "2030-05-03", "Proveedor", "otra", Decimal("-1"), "USD")


if __name__ == "__main__":
    unittest.main()
