# Flujos de trabajo con IA

Material gratuito de Frank Miller, consultor SAP con más de 10 años de experiencia.

Este repositorio contiene ejemplos ficticios para aprender a diseñar flujos de trabajo asistidos por IA con entradas, límites y revisión humana.

> **Aviso:** los datos son sintéticos. No contienen información de clientes de Cygnus Consulting ni deben utilizarse para enviar mensajes, aprobar solicitudes o modificar sistemas reales.

## Qué aprenderás

- Definir una tarea concreta antes de elegir una herramienta.
- Separar fuentes de instrucciones.
- Preparar borradores sin inventar datos faltantes.
- Comparar propuestas frente a requisitos explícitos.
- Separar acuerdos, ideas y preguntas pendientes.
- Diseñar una revisión humana antes de cualquier acción externa.

## Contenido

- `GUIA.md` — guía práctica.
- `datos/` — casos ficticios.
- `instrucciones/` — instrucciones reutilizables.
- `fichas/` — plantillas para diseñar tu propio flujo.
- `demo/` — procedimientos, resultados de referencia y registros de ejecución.
- `src/flujos_ia/` — motor ejecutable de las demos.
- `tests/` — pruebas automatizadas.
- `demo/results/` — salidas generadas por el motor offline.

## Ejecutar el proyecto

Requiere Python 3.11 o superior. El comando `python` de algunos sistemas puede apuntar a Python 2; utiliza `python3`.

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
PYTHONPATH=src python3 -m flujos_ia --demo all
```

Las salidas se generan en `demo/results/`:

- `demo-1-organizar-solicitudes.md`
- `demo-2-comparar-propuestas.md`

El modo actual es **offline y determinista**: las reglas de control y la revisión son reproducibles sin API. Esto permite probar los límites antes de añadir un modelo externo. La capa LLM, cuando se incorpore, no debe aprobar, comprar, enviar ni modificar sistemas; solo puede preparar una propuesta que pase por el mismo control humano.

## Límites

Este repositorio no incluye una integración con SAP Business One, Pi, n8n, correo, CRM ni otros sistemas. Tampoco promete automatización autónoma, precisión total o ahorro de tiempo. Las conexiones a sistemas reales requieren permisos, pruebas y una propuesta técnica independiente.

## Formación

Taller práctico: «De la tarea al flujo: IA aplicada al trabajo real».

Próximas fechas tentativas: 5 y 7 de noviembre de 2026, 19:00 America/Lima.

La convocatoria, precio, requisitos y condiciones se publicarán antes de aceptar pagos:

- Guía y ejemplos: https://github.com/millerfrankmc/flujos-trabajo-ia
- Taller: `PENDIENTE — se añadirá el checkout de Hotmart`
- Formación para empresas: https://www.cygnus.com.pe

## Autor

Frank Miller — fmiller@cygnus.com.pe

Cygnus Consulting es una firma peruana especializada en SAP Business One, consultoría, desarrollo, integraciones y capacitación. Más información: https://www.cygnus.com.pe

## Licencia de los materiales

Antes de publicar, definir la licencia que permitirá usar y adaptar los ejemplos sin autorizar la reventa del material formativo como propio. No copiar código o materiales de terceros sin verificar sus licencias.
