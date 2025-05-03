# Ficha Específica – `sensor_ble.py`

## Nombre del archivo:
`sensor_ble.py`

## Responsabilidad principal:
Gestionar la detección de dispositivos Bluetooth Low Energy (BLE) cercanos al sistema NORA, permitiendo la identificación pasiva de usuarios o dispositivos a través de escaneos periódicos.

## Entradas esperadas:
- Señales de identificación BLE (direcciones MAC, identificadores de servicio).
- Configuraciones dinámicas (frecuencia de escaneo, dispositivos conocidos, RSSI mínimo aceptado).

## Salidas generadas:
- Lista de dispositivos detectados (MACs, RSSI, servicios).
- Eventos asociados:
  - `EVT_BLE_DEVICE_DETECTED`
  - `EVT_BLE_KNOWN_DEVICE_PRESENT`

## Funcionalidades principales:
- Escaneo periódico de dispositivos BLE en proximidad.
- Filtrado de dispositivos por intensidad de señal (RSSI) y listas de permitidos.
- Emisión de eventos de detección y presencia basada en dispositivos conocidos.
- Gestión de reconexiones o pérdidas de dispositivos BLE detectados.

## Dependencias técnicas:
- `bleak` – Librería de comunicación BLE multiplataforma.
- `asyncio` – Gestión de escaneos y eventos de forma no bloqueante.
- `json` – Almacenamiento y gestión de listas de dispositivos autorizados.

