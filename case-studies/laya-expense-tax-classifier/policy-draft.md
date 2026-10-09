# Política preliminar de etiquetas — requiere contador peruano

## Estado

**Borrador técnico, no criterio tributario aprobado.**

Antes de entrenar Laya, un contador peruano debe revisar cada fila y confirmar, para el periodo y régimen aplicables, qué evidencia y reglas corresponden. La política debe registrar versión, fecha, fuente normativa y responsable de aprobación.

## Ejes separados

### `renta_tratamiento`

- `probable_deducible`: evidencia preliminar de relación con el negocio y documentación suficiente; no es aprobación fiscal.
- `probable_reparable`: se registra como gasto contable, pero la hipótesis de trabajo indica que podría requerir adición o ajuste tributario.
- `condicionado`: depende de límites, causalidad, uso, sustento u otros hechos que faltan.
- `insuficiente_evidencia`: no hay información suficiente para una conclusión.

### `igv_credito`

- `probable_creditable`: hipótesis preliminar para revisión del crédito fiscal.
- `probable_no_creditable`: hipótesis preliminar de que no corresponde utilizarlo.
- `condicionado`: requiere verificar uso, comprobante, requisitos y contexto.
- `insuficiente_evidencia`: faltan datos o el comprobante no permite concluir.

### `documentacion`

- `completa`: los campos necesarios para el prototipo están presentes; no significa validez legal.
- `incompleta`: faltan campos o evidencia.
- `inconsistente`: hay contradicciones o señales que requieren revisión.

### `revision`

- `estandar`: revisión humana normal antes del registro.
- `contador`: debe revisarlo un profesional por riesgo o incertidumbre.
- `bloqueada`: no continuar hasta corregir o completar evidencia.

## Reglas de seguridad

1. No usar la frase «SUNAT acepta» como salida del modelo.
2. No producir una decisión fiscal solo a partir del texto OCR.
3. Separar extracción de hechos y clasificación.
4. Guardar evidencia de cada campo utilizado.
5. Abstenerse cuando falte información crítica.
6. No registrar automáticamente un asiento o crédito fiscal.
7. Versionar la política por periodo tributario.
8. Revisar cambios normativos antes de reutilizar el dataset.
9. Mantener datos personales y comprobantes fuera del repositorio público.
10. Cualquier integración SAP requiere pruebas y autorización separadas.

## Campos que el contador debe revisar

- régimen tributario y tipo de contribuyente;
- causalidad y relación con generación de renta;
- tipo y validez del comprobante;
- proveedor y RUC;
- uso empresarial o mixto;
- medio de pago y bancarización cuando corresponda;
- límites o condiciones especiales;
- periodo y devengo;
- detracciones, retenciones o percepciones cuando correspondan;
- documentación adicional exigible;
- tratamiento contable frente al tributario.
