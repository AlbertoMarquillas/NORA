# Ficha Específica – `sensor_reloj.py`

## Nombre del archivo:
`sensor_reloj.py`

## Responsabilidad principal:
Gestionar la lectura de datos temporales a partir de un reloj de tiempo real (RTC), como el DS3231, para mantener la referencia horaria exacta del sistema NORA, incluso durante reinicios o cortes de energía.

## Entradas esperadas:
- Señales digitales de lectura de fecha y hora.
- Configuraciones dinámicas (frecuencia de actualización, sincronización NTP opcional).

## Salidas generadas:
- Datos de fecha y hora actuales.
- Eventos asociados:
  - `EVT_TIME_UPDATED`
  - `EVT_TIME_SYNC_REQUIRED`

## Funcionalidades principales:
- Lectura de fecha y hora desde el RTC DS3231 (I²C).
- Verificación de la coherencia temporal.
- Detección de desincronización o errores de reloj.
- Emisión de eventos de actualización horaria o alerta de fallo de sincronización.
- Sincronización opcional con servicios NTP si disponible.

## Dependencias técnicas:
- `smbus2` – Comunicación I²C con el RTC.
- `datetime` – Manejo de datos temporales.
- `ntplib` (opcional) – Sincronización horaria vía red.
- `json` – Formateo de eventos temporales.

