# Evidencia y límites del caso Laya

## Evidencia técnica

1. Laya se presenta como un motor de decisiones tipadas no autoregresivo, con tipos `choice`, `score` y `noul`, router multilingüe y confianza.

   Fuente: https://github.com/NandhaKishorM/laya

2. El repositorio documenta fine-tuning con decisiones propias y muestra un benchmark interno de typed decisions. Es evidencia del mecanismo y de la posibilidad de adaptación; no es evidencia de rendimiento en tributación peruana.

   Fuente: https://github.com/NandhaKishorM/laya

3. La evaluación de Laya acepta datasets JSONL con `state`, `questions`, `expected`, tags y lenguaje, y permite medir accuracy, calibración, umbrales y baselines.

   Fuente: https://raw.githubusercontent.com/NandhaKishorM/laya/main/docs/evals.md

## Evidencia de encaje empresarial

Cygnus comunica un módulo de rendición de gastos integrado con SAP Business One y Excel, con carga masiva, creación de documentos y conciliación.

Fuente: https://cygnus.com.pe/docs/rendicion-de-gastos/

Esto respalda la elección del proceso como hipótesis B2B. No demuestra que Laya o el clasificador tributario ya estén integrados.

## Evidencia normativa

La búsqueda de páginas oficiales no permitió recuperar una fuente normativa única y suficientemente detallada para etiquetar automáticamente los cuatro casos. Por eso el dataset se marca como `etiqueta_borrador` y no debe entrenarse para producción hasta que un contador peruano revise cada caso con la normativa aplicable, el régimen, el periodo y la evidencia documental.

Portal oficial de SUNAT: https://www.sunat.gob.pe/

## Qué se puede afirmar

- El caso usa un formato compatible con una evaluación de decisiones tipadas.
- La clasificación separa renta, IGV, evidencia y revisión.
- El flujo evita una afirmación binaria de «SUNAT acepta».
- La solución puede producir una cola de revisión y razones.

## Qué no se puede afirmar todavía

- Que las etiquetas sean jurídicamente correctas.
- Que Laya tenga accuracy útil en español tributario peruano.
- Que un gasto sea deducible solo por la predicción del modelo.
- Que el resultado reduzca horas o reparos.
- Que Cygnus tenga una integración de IA existente.
