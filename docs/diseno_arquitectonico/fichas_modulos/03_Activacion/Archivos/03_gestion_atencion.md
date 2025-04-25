# Ficha Específica – `gestion_atencion.py`

## Nombre del archivo:
`gestion_atencion.py`

## Responsabilidad principal:
Gestionar la evaluación de eventos de activación basados en la atención visual del usuario, determinando si el sistema NORA debe pasar a un estado activo a partir de señales de atención sostenida detectadas.

## Entradas esperadas:
- Eventos de detección de atención (`EVT_ATTENTION_GAINED`, `EVT_ATTENTION_LOST`).
- Configuraciones dinámicas (tiempo mínimo de atención, umbrales de estabilidad).

## Salidas generadas:
- Eventos de activación condicional basados en atención sostenida.
- Eventos asociados:
  - `EVT_ACTIVATION_CONFIRMED`
  - `EVT_ACTIVATION_DENIED`

## Funcionalidades principales:
- Validación de la atención visual sostenida durante un periodo de tiempo configurable.
- Filtrado de fluctuaciones breves o miradas accidentales.
- Confirmación robusta de intención de interactuar antes de activar el sistema.

## Dependencias técnicas:
- `eventos_activacion.py` – Emisión de eventos de activación.
- `datetime`, `time` – Control temporal para validación de atención.

