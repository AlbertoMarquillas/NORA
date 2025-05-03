# Ficha Específica – `activacion_main.py`

## Nombre del archivo:
`activacion_main.py`

## Responsabilidad principal:
Coordinar la lógica general del módulo `activacion/`. Gestiona la escucha de eventos provenientes de múltiples fuentes de activación (presencia, NFC, atención visual, hotword, botón físico) y aplica la lógica combinada para decidir la activación o reposo del sistema.

## Entradas esperadas:
- Eventos internos de activación desde `sensores/`, `vision/`, `voz/` y GPIO.
- Configuraciones dinámicas (prioridad de fuentes, tiempos de espera, modo no molestar).

## Salidas generadas:
- Eventos de activación o reposo:
  - `EVT_ACTIVATION_CONFIRMED`
  - `EVT_ACTIVATION_DENIED`
  - `EVT_REST_MODE_TRIGGERED`

## Funcionalidades principales:
- Escucha y recepción de múltiples eventos de activación.
- Coordinación de submódulos de evaluación (`gestion_nfc.py`, `gestion_presencia.py`, `gestion_atencion.py`, etc.).
- Aplicación de lógica combinada mediante `decision_activacion.py`.
- Emisión de eventos al sistema en función del resultado de la evaluación.
- Gestión del estado de activación actual (activo, en reposo).

## Dependencias técnicas:
- `pyee`, `eventbus` – Gestión de eventos internos.
- Submódulos de `activacion/`.
- `config_activacion.py` – Parámetros de activación configurables.

