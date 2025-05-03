# Ficha Específica – `sensor_temperatura.py`

## Nombre del archivo:
`sensor_temperatura.py`

## Responsabilidad principal:
Gestionar la lectura periódica de sensores de temperatura y humedad conectados (como DHT22 o BME280), procesando las señales y generando eventos ambientales interpretados.

## Entradas esperadas:
- Señal analógica/digital de temperatura y humedad relativa.
- Configuraciones dinámicas (umbral de calor, humedad crítica, frecuencia de lectura).

## Salidas generadas:
- Valores de temperatura y humedad normalizados.
- Eventos asociados:
  - `EVT_ENV_HOT`
  - `EVT_ENV_HUMIDITY_HIGH`
  - `EVT_ENV_LOGGED`

## Funcionalidades principales:
- Lectura desde sensores tipo DHT22 (GPIO) o BME280 (I²C).
- Validación de la coherencia de los datos adquiridos.
- Conversión a unidades estándar (°C, %RH).
- Detección de condiciones críticas (calor extremo, humedad elevada).
- Emisión de eventos de alerta ambiental y registro de valores.

## Dependencias técnicas:
- `adafruit_dht`, `smbus2` – Lectura de sensores físicos.
- `gpiozero`, `board` – Acceso a pines GPIO o buses I²C.
- `datetime`, `json` – Formateo de datos para eventos.

