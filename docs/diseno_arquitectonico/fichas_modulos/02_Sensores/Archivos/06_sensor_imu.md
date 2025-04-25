# Ficha Específica – `sensor_imu.py`

## Nombre del archivo:
`sensor_imu.py`

## Responsabilidad principal:
Gestionar la lectura de sensores de movimiento inercial (IMU), como acelerómetros y giróscopos, para detectar inclinaciones, vibraciones o movimientos relevantes del sistema.

## Entradas esperadas:
- Datos de aceleración y rotación en tres ejes (X, Y, Z).
- Configuraciones dinámicas (umbrales de movimiento, tipo de eventos a detectar).

## Salidas generadas:
- Medidas normalizadas de aceleración y rotación.
- Eventos asociados:
  - `EVT_MOVEMENT_DETECTED`
  - `EVT_INCLINATION_DETECTED`

## Funcionalidades principales:
- Lectura de datos desde sensores IMU conectados (por ejemplo, MPU6050 vía I²C).
- Conversión y calibración de valores brutos.
- Detección de inclinaciones superiores a umbrales definidos.
- Detección de movimientos bruscos o vibraciones.
- Emisión de eventos internos relevantes para el sistema.

## Dependencias técnicas:
- `smbus2` – Comunicación I²C con sensores IMU.
- `numpy` – Procesamiento de vectores de movimiento.
- `datetime`, `json` – Registro y transmisión de eventos detectados.

