# Ficha Específica – `decision_activacion.py`

## Nombre del archivo:
`decision_activacion.py`

## Responsabilidad principal:
Aplicar la lógica combinada de evaluación de múltiples fuentes de activación para determinar de manera robusta si el sistema NORA debe pasar a estado activo o permanecer en reposo.

## Entradas esperadas:
- Resultados parciales de submódulos de activación (presencia, atención, voz, NFC, botón).
- Configuraciones dinámicas (prioridades, pesos relativos de cada fuente, modo no molestar).

## Salidas generadas:
- Decisión final de activación (`confirmada` o `denegada`).
- Emisión de eventos asociados:
  - `EVT_ACTIVATION_CONFIRMED`
  - `EVT_ACTIVATION_DENIED`

## Funcionalidades principales:
- Evaluación ponderada de las señales de activación.
- Aplicación de reglas de activación flexible (cualquier fuente válida, combinación mínima de fuentes).
- Soporte para lógica de votación entre múltiples fuentes.
- Emisión de decisión final al `sistema/` y `agentes/`.

## Dependencias técnicas:
- `eventos_activacion.py` – Emisión de eventos normalizados.
- `datetime`, `json` – Registro opcional de decisiones de activación.

