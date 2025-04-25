# Ficha Específica – `sensor_pir.py`

## Nombre del archivo:
`sensor_pir.py`

## Responsabilidad principal:
Gestionar la detección de movimiento mediante sensores de infrarrojo pasivo (PIR), registrando cambios de presencia basados en la variación de calor en el entorno inmediato.

## Entradas esperadas:
- Señales digitales de activación PIR.
- Configuraciones dinámicas (sensibilidad de detección, filtros de estabilidad).

## Salidas generadas:
- Detecciones binarizadas de movimiento: `movimiento detectado` o `sin movimiento`.
- Eventos asociados:
  - `EVT_PRESENCE_MOTION_DETECTED`
  - `EVT_PRESENCE_MOTION_ENDED`

## Funcionalidades principales:
- Lectura directa del estado de sensores PIR conectados a GPIO.
- Debouncing y filtrado temporal para evitar falsas detecciones.
- Confirmación de patrones de movimiento relevantes.
- Emisión de eventos para el sistema de presencia general.

## Dependencias técnicas:
- `gpiozero`, `RPi.GPIO` – Lectura de señales digitales.
- `time` – Control de debouncing y estabilidad de señales.
- `datetime`, `json` – Formateo y transmisión de eventos de movimiento.

