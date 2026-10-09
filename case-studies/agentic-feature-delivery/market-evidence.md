# Evidencia de relevancia del caso

## Conclusión

Hay evidencia de que el flujo que enseñamos corresponde a una capacidad real y a un problema relevante: delegar trabajo de desarrollo a agentes, manteniendo planificación, herramientas, pruebas y revisión.

Esto **no demuestra** que exista disposición a pagar por este curso concreto ni que el caso de rendiciones sea el mejor nicho comercial. Esa validación requiere alumnos o un piloto B2B.

## Evidencia primaria

### 1. GitHub: delegar tareas de código desde GitHub

GitHub describe su coding agent como una forma de explorar repositorios, planificar cambios y delegar tareas de código desde GitHub.com.

Fuente: https://docs.github.com/copilot/concepts/agents/coding-agent/about-coding-agent

**Qué respalda en nuestro caso:** el punto de partida «requerimiento → plan → código» es una categoría de trabajo reconocida por la propia plataforma.

**Qué no respalda:** que nuestro motor offline sea un coding agent o que los alumnos paguen por aprenderlo.

### 2. Microsoft Learn: formación específica sobre coding agents

Microsoft Learn ofrece un módulo para desarrolladores, DevOps engineers, administradores y solution architects sobre cómo delegar tareas al GitHub Copilot cloud agent.

Fuente: https://learn.microsoft.com/en-us/training/modules/github-copilot-code-agent/

**Qué respalda:** existe una necesidad educativa alrededor de delegar trabajo de desarrollo a agentes, no solo de escribir prompts.

**Qué no respalda:** una ventaja competitiva automática para nuestro curso; el contenido debe aportar un caso reproducible y criterio transferible.

### 3. Stack Overflow Developer Survey 2025

La sección de IA de la encuesta indica que más desarrolladores desconfían de la precisión de las herramientas de IA que los que confían en ella: 46% frente a 33%; solo 3% declara confiar mucho.

Fuente: https://survey.stackoverflow.co/2025/ai

**Qué respalda:** pruebas, revisión humana y reportes de límites son una parte comercialmente relevante del problema.

**Qué no respalda:** una cifra de productividad ni una tasa de conversión para nuestra oferta.

### 4. OpenAI: componentes de un agente

La documentación de OpenAI describe agentes mediante instrucciones, guardrails y acceso a herramientas.

Fuente: https://developers.openai.com/tracks/building-agents

**Qué respalda:** nuestro diseño separa reglas de negocio, acciones bloqueadas y ejecución controlada, en vez de presentar un prompt aislado como sistema completo.

**Qué no respalda:** que este caso necesite un agente autónomo; para la primera versión, un flujo determinista es más fácil de probar.

## Relación con el caso

El caso de exportación de rendiciones no intenta competir con una integración ERP terminada. Enseña el tramo que suele ser difícil de revisar:

```text
petición ambigua
→ alcance y criterios
→ código limitado
→ pruebas
→ reporte de lo que NO se implementó
```

El caso es especialmente útil para demostrar que el agente no debe inventar integración con SAP, enviar archivos ni declarar éxito fuera de lo comprobado.

## Próxima validación comercial

Para comprobar valor pagable:

1. Mostrar el video de la ejecución a cinco programadores.
2. Preguntar qué parte podrían reutilizar en su trabajo.
3. Ofrecer un laboratorio de USD 49–99.
4. Medir pagos, no solo comentarios.
5. Preguntar si prefieren el caso de rendiciones, otro dominio o un repositorio de software más cercano a su trabajo.

Hasta completar esos pasos, la evidencia es de **relevancia del problema**, no de demanda pagada.
