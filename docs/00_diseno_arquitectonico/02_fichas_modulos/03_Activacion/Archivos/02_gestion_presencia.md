# Ficha Específica – `gestion_presencia.py`

## Nombre del archivo:
`gestion_presencia.py`

## Responsabilidad principal:
Gestionar la evaluación de eventos de activación basados en la detección de presencia física, utilizando sensores ultrasónicos o PIR para confirmar la proximidad de un usuario al sistema NORA.

## Entradas esperadas:
- Eventos de detección de presencia (`EVT_PRESENCE_CONFIRMED`, `EVT_PRESENCE_MOTION_DETECTED`).
- Configuraciones dinámicas (sensibilidad, tiempo de confirmación).

## Salidas generadas:
- Eventos de activación basados en presencia física.
- Eventos asociados:
  - `EVT_ACTIVATION_CONFIRMED`

## Funcionalidades principales:
- Validación de la detección de presencia mediante verificación cruzada de múltiples sensores si están disponibles.
- Gestión de tiempos mínimos de presencia para evitar falsos positivos.
- Confirmación robusta de presencia antes de emitir evento de activación.

## Dependencias técnicas:
- `eventos_activacion.py` – Emisión de eventos normalizados.
- `datetime`, `time` – Control de tiempos de confirmación de presencia.

