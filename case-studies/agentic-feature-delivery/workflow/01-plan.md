# Plan técnico — resultado de referencia

> Plan redactado para el caso. No se afirma que un modelo lo haya generado.

## Entendimiento

Una aplicación local necesita exportar una colección de rendiciones a CSV para conciliación. La primera versión no modifica datos externos ni conoce SAP Business One.

## Diseño

- Crear un tipo inmutable `Rendicion`.
- Validar empleado, fecha, proveedor e importe no negativo.
- Implementar `exportar_csv` con una colección iterable.
- Copiar la colección a una lista para no mutar la entrada.
- Aplicar filtro opcional por empleado.
- Ordenar por fecha, empleado y proveedor.
- Usar `csv.writer` para escapar valores correctamente.
- Normalizar el importe a dos decimales con `Decimal`.

## Archivos

- `app/rendiciones.py`: dominio y exportación.
- `app/demo.py`: ejemplo ejecutable.
- `tests/test_rendiciones.py`: aceptación automatizada.

## Criterios de aceptación trazados

- Columnas y cabecera: pruebas de exportación.
- Orden estable: `test_ordena_por_fecha`.
- Comas y comillas: `test_escapa_proveedor_csv`.
- Filtro: `test_filtra_por_empleado`.
- Importe negativo: `test_rechaza_importe_negativo`.
- No mutación: la implementación copia antes de ordenar.
- Fuera de alcance: no existen conectores ni escrituras externas.

## Preguntas pendientes

- ¿Qué formato de fecha exige el sistema consumidor?
- ¿Debe admitirse una moneda por archivo o varias?
- ¿Qué estado de aprobación debe tener una rendición antes de exportarse?

Estas preguntas no bloquean la demo local, pero sí una integración de producción.
