# Caso Laya — Clasificador asistido de rendiciones

## Objetivo

Usar Laya como motor de decisiones tipadas para clasificar rendiciones de gastos en varias dimensiones independientes:

- tipo de gasto;
- tratamiento preliminar para Impuesto a la Renta;
- tratamiento preliminar del crédito fiscal de IGV;
- calidad de la evidencia documental;
- nivel de riesgo y necesidad de revisión.

## Advertencia profesional

Este repositorio es un prototipo educativo con casos sintéticos. No determina si SUNAT aceptará un gasto, no reemplaza a un contador y no debe conectarse a SAP Business One ni utilizarse para presentar declaraciones.

La palabra «reparable» se mantiene separada de «gasto contable». El resultado no usa una etiqueta única de «aceptado por SUNAT», porque deducibilidad de renta, crédito fiscal de IGV, validez documental y evidencia del negocio son decisiones relacionadas pero distintas.

Las etiquetas del dataset son **preliminares y requieren aprobación de un contador peruano**. La versión actual sirve para probar el formato de datos y el flujo de evaluación de Laya, no para afirmar una regla tributaria.

## Por qué Laya

Laya está diseñado para decisiones tipadas y permite fine-tuning en decisiones de dominio. Su formato de evaluación usa `state`, `questions` y `expected`, que encaja con un comprobante más contexto de negocio y varias clasificaciones simultáneas.

Repositorio oficial de Laya:

https://github.com/NandhaKishorM/laya

## Arquitectura propuesta

```text
PDF/imagen del comprobante
        ↓
OCR y extracción de campos
        ↓
validación documental determinista
        ↓
Laya: decisiones tipadas y confianza
        ↓
reglas contables/tributarias versionadas
        ↓
cola de revisión profesional
        ↓
exportación preparada para SAP Business One
```

Laya no debe recibir autoridad para aprobar pagos, registrar asientos, declarar impuestos o modificar SAP. Su salida es una recomendación estructurada con evidencia y abstención cuando faltan datos.

## Validar el dataset sin instalar Laya

Desde este directorio:

```bash
python3 scripts/validate_dataset.py
```

## Evaluar con Laya

Después de instalar y configurar Laya en un entorno separado, la primera validación debe ser:

```bash
laya-evals validate dataset/expense_decisions.jsonl
```

Para puntuar un checkpoint, primero se requiere una revisión profesional de las etiquetas y un baseline:

```bash
laya-evals run dataset/expense_decisions.jsonl \
  --model english \
  --min-accuracy 0.80 \
  --max-ece 0.10 \
  --json reports/baseline.json \
  --markdown reports/baseline.md
```

Los umbrales son placeholders de diseño, no resultados conseguidos ni criterios legales. No entrenar hasta aprobar las etiquetas.

## Caso empresarial

Cygnus ya comunica un módulo de rendición de gastos integrado con SAP Business One y Excel:

https://cygnus.com.pe/docs/rendicion-de-gastos/

Este caso puede convertirse en un laboratorio B2B: clasificar rendiciones, explicar faltantes y enviar casos dudosos a revisión. La integración con el ERP queda fuera de este prototipo.
