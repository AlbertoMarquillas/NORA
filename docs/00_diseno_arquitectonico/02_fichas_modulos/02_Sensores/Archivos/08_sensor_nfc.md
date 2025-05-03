# Ficha Específica – `sensor_nfc.py`

## Nombre del archivo:
`sensor_nfc.py`

## Responsabilidad principal:
Gestionar la lectura de identificadores NFC desde dispositivos compatibles (como PN532), permitiendo la detección y validación de presencia o identificación de usuarios a través de tarjetas o etiquetas NFC.

## Entradas esperadas:
- Señales de comunicación NFC (UIDs detectados).
- Configuraciones dinámicas (modo lectura, tiempo de espera entre lecturas).

## Salidas generadas:
- UID del dispositivo NFC detectado.
- Eventos asociados:
  - `EVT_NFC_UID_DETECTED`
  - `EVT_NFC_AUTH_SUCCESS`
  - `EVT_NFC_AUTH_FAILURE`

## Funcionalidades principales:
- Inicialización y gestión de la comunicación NFC (I²C o UART).
- Detección de dispositivos NFC en rango.
- Lectura y validación de UID contra bases de datos locales.
- Emisión de eventos de detección o validación de identificadores.
- Gestión de timeout o reintentos en detección NFC.

## Dependencias técnicas:
- `adafruit_pn532`, `smbus2` – Comunicación NFC.
- `serial` (opcional) – Comunicación UART.
- `json` – Almacenamiento y validación de UIDs autorizados.

