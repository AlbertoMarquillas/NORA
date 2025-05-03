# Ficha Específica – `gestion_hotword.py`

## Nombre del archivo:
`gestion_hotword.py`

## Responsabilidad principal:
Gestionar la evaluación de eventos de activación basados en la detección de una palabra clave (hotword), permitiendo que el usuario active el sistema NORA mediante un comando de voz específico.

## Entradas esperadas:
- Eventos de detección de hotword (`EVT_WAKEWORD_DETECTED`).
- Configuraciones dinámicas (lista de hotwords válidas, sensibilidad de detección).

## Salidas generadas:
- Eventos de activación inmediata basados en hotword.
- Eventos asociados:
  - `EVT_ACTIVATION_CONFIRMED`

## Funcionalidades principales:
- Validación del evento de detección de hotword.
- Confirmación opcional basada en condiciones adicionales (presencia, atención visual).
- Emisión inmediata de evento de activación al reconocer la palabra clave correcta.

## Dependencias técnicas:
- `eventos_activacion.py` – Emisión de eventos normalizados.
- `datetime` – Registro opcional de detecciones de hotword.

