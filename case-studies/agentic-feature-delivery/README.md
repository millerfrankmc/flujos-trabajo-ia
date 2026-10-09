# Caso práctico — Del requerimiento a una funcionalidad verificable

## Objetivo

Mostrar un flujo de trabajo para programadores que usan agentes de IA:

```text
requerimiento de negocio
        ↓
plan técnico con preguntas y criterios
        ↓
implementación aislada
        ↓
pruebas automatizadas
        ↓
diff y reporte revisable
```

El caso simula una funcionalidad pequeña de un sistema de rendiciones de gastos: exportar registros a CSV para conciliación. Los datos son ficticios y la implementación no se conecta con SAP Business One ni con sistemas externos.

## Por qué este caso

- Es una necesidad reconocible en software administrativo.
- Produce un artefacto tangible: código + tests + CSV.
- No depende de corregir un error puntual.
- Permite demostrar contexto, diseño, criterios de aceptación, pruebas y revisión humana.
- Puede explicarse a un programador y también a un equipo B2B sin exponer datos reales.

## Ejecutar

Requiere Python 3.11 o superior:

```bash
cd case-studies/agentic-feature-delivery
python3 -m unittest discover -s tests -v
python3 -m app.demo
```

## Resultado esperado

- 5 pruebas pasando.
- Exportación determinista, ordenada y escapada correctamente.
- El reporte identifica qué se implementó y qué no se hizo: no hay conexión a ERP, no se envía el archivo y no se modifican datos externos.

## Qué demostraría un agente real

En una ejecución con un coding agent, el agente recibiría `requirements.md` y `AGENTS.md`, inspeccionaría el repositorio, propondría `workflow/01-plan.md`, implementaría `app/rendiciones.py`, ejecutaría las pruebas y produciría `workflow/02-implementation-report.md`.

Los archivos de este caso contienen el resultado preparado y reproducible. No se afirma que un modelo haya generado estos archivos: la ejecución del agente real debe registrarse aparte.
