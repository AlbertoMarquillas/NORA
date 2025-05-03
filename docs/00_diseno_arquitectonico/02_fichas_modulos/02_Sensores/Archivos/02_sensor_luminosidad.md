# Ficha Específica – `sensor_luminosidad.py`

## Nombre del archivo:
`sensor_luminosidad.py`

## Responsabilidad principal:
Gestionar la lectura periódica del sensor de luminosidad (como TSL2561), interpretando el nivel de iluminación ambiental y generando eventos que reflejan las condiciones de luz del entorno.

## Entradas esperadas:
- Señal de medición de luz en lux.
- Configuraciones dinámicas (umbral de baja luminosidad, frecuencia de lectura).

## Salidas generadas:
- Nivel de luminosidad en lux.
- Eventos asociados:
  - `EVT_DARK_ENV`
  - `EVT_BRIGHT_ENV`

## Funcionalidades principales:
- Lectura de datos de lux desde sensores tipo TSL2561 (vía I²C).
- Conversión y validación de valores de iluminación.
- Detección de condiciones de baja iluminación o exceso de brillo.
- Emisión de eventos de alerta o cambio ambiental de luz.
- Registro opcional de historial de condiciones lumínicas.

## Dependencias técnicas:
- `smbus2`, `adafruit_tsl2561` – Comunicación con sensores de luminosidad.
- `gpiozero` – Alternativamente, integración GPIO para otros sensores simples.
- `datetime`, `json` – Formateo y transmisión de eventos.

