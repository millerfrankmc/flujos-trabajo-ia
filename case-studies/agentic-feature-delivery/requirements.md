# Requerimiento de negocio — Exportación de rendiciones

## Contexto

El equipo administrativo revisa rendiciones de gastos y necesita entregar un archivo CSV al proceso de conciliación. La primera versión debe ser local y determinista; no debe conectarse a SAP Business One ni enviar archivos.

## Solicitud

Añadir una función que exporte rendiciones a CSV.

## Requisitos obligatorios

1. Recibir una colección de rendiciones.
2. Exportar las columnas: empleado, fecha, proveedor, categoría, importe y moneda.
3. Incluir una fila de cabecera.
4. Ordenar por fecha, empleado y proveedor.
5. Representar los importes con dos decimales.
6. Escapar correctamente proveedores con comas, comillas o saltos de línea.
7. Permitir filtrar por empleado.
8. No mutar la colección original.
9. Rechazar importes negativos.
10. Cubrir el comportamiento con pruebas automatizadas.

## Fuera de alcance

- Lectura de SAP Business One.
- Escritura en bases de datos.
- Envío por correo.
- Subida a almacenamiento externo.
- Aprobación contable.
- Cálculo de impuestos.
- Autenticación y autorización.

## Criterios de aceptación

- Una rendición simple produce cabecera y una fila válida.
- Varias rendiciones se ordenan de forma estable.
- Un proveedor con coma o comillas se exporta como CSV válido.
- El filtro por empleado excluye el resto.
- Un importe negativo genera un error explícito.
- Las pruebas pasan con `python3 -m unittest discover -s tests -v`.
- El reporte declara expresamente las integraciones que no existen.
