# Ficha Específica – `sensor_calidad_aire.py`

## Nombre del archivo:
`sensor_calidad_aire.py`

## Responsabilidad principal:
Gestionar la lectura periódica de sensores de calidad del aire (como MQ135 o CCS811), midiendo la concentración de gases contaminantes y generando eventos ambientales basados en los niveles detectados.

## Entradas esperadas:
- Señales de concentración de gases (CO₂, VOCs, compuestos orgánicos volátiles).
- Configuraciones dinámicas (umbrales de calidad aceptable, frecuencia de lectura).

## Salidas generadas:
- Valores normalizados de calidad de aire.
- Eventos asociados:
  - `EVT_ENV_AIR_QUALITY_POOR`
  - `EVT_ENV_AIR_QUALITY_GOOD`

## Funcionalidades principales:
- Lectura de datos de sensores CCS811 (I²C) o MQ135 (analogread).
- Conversión de señales a concentraciones estándar.
- Detección de mala calidad del aire basada en umbrales configurados.
- Emisión de eventos de alerta ambiental.
- Registro opcional de condiciones de calidad de aire para histórico.

## Dependencias técnicas:
- `smbus2`, `adafruit_ccs811` – Lectura de sensores de calidad de aire.
- `gpiozero`, `ADC` (si analógico) – Lectura de sensores MQ135.
- `datetime`, `json` – Registro y transmisión de eventos.

