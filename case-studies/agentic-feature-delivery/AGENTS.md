# Instrucciones del agente para este caso

## Objetivo

Implementar únicamente el requerimiento de `requirements.md` y dejar evidencia verificable.

## Reglas

- Lee primero `requirements.md` y el código existente.
- No añadas dependencias externas.
- No cambies la API pública sin justificarlo en el plan.
- No conectes SAP, correo, almacenamiento ni servicios externos.
- No inventes requisitos fuera del documento.
- Usa `Decimal` para importes monetarios.
- Mantén funciones pequeñas y fáciles de probar.
- Escribe o actualiza pruebas antes de declarar completado el cambio.
- Ejecuta todas las pruebas.
- Reporta explícitamente cualquier requisito no implementado.

## Puerta de aprobación

El agente puede editar código dentro de este caso y ejecutar pruebas locales. No puede hacer merge, publicar, desplegar ni enviar datos externos. Una persona revisa el diff y el reporte.

## Formato del reporte

El reporte debe contener:

1. Archivos cambiados.
2. Requisitos implementados, con evidencia.
3. Pruebas ejecutadas y resultado.
4. Decisiones técnicas.
5. Límites y fuera de alcance.
6. Riesgos o preguntas pendientes.
