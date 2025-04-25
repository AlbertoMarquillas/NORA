# Ficha Funcional – Módulo de Sensores

## Nombre del módulo:
`sensores/`

## Responsabilidad principal:
Gestiona la lectura, conversión y validación de los sensores físicos conectados al sistema. Incluye sensores ambientales, de presencia, temporales y de identificación. Su objetivo es generar eventos contextualizados a partir de señales físicas.

## Entradas esperadas:
- Tipo de entrada: señales físicas y digitales de sensores
- Fuente: sensores conectados por GPIO, I²C, BLE o UART
- Formato o protocolo: valores analógicos/digitales normalizados, lectura periódica

## Salidas generadas:
- Tipo de salida: eventos de entorno, presencia, identificación o cronología
- Destinatario: `sistema/`, `agentes/`, `activacion/`, `datos/`
- Ejemplo de salida:
  - `EVT_PRESENCE_CONFIRMED`
  - `EVT_ENV_HOT`, `EVT_DARK_ENV`, `EVT_NFC_UID_DETECTED`
  - Datos persistibles para historial (`EVT_ENV_LOGGED`)

## Módulos relacionados:
- Entrada desde: sensores físicos (DHT22, BME280, TSL2561, CCS811, HC-SR04, DS3231, NFC, BLE)
- Salida hacia: `activacion/`, `sistema/`, `agentes/`, `datos/`
- Comunicación bidireccional con: `sistema/` (consultas activas), `agentes/` (filtrado o evaluación)

## Dependencias técnicas:
- Librerías externas: `gpiozero`, `smbus2`, `adafruit_dht`, `bleak`, `datetime`, `json`, `paho-mqtt`
- Hardware gestionado: todos los sensores físicos de entorno, presencia e identificación
- Protocolos: I²C, UART, GPIO, BLE

## Notas adicionales:
Es un módulo pasivo que genera eventos periódicos o reactivos. Su diseño permite desacoplar el acceso al hardware del resto del sistema, facilitando pruebas, simulación o extensión futura. Las funciones NFC pueden ser reutilizadas por `activacion/` y `datos/`.

## Archivos previstos del módulo:
Listado de archivos `.py` que se espera implementar dentro del directorio `sensores/` para estructurar sus funcionalidades.

- `sensores_main.py`: Punto de entrada del módulo, coordinación de lectura periódica.
- `sensor_temperatura.py`: Gestión de DHT22/BME280.
- `sensor_luminosidad.py`: Lectura desde TSL2561.
- `sensor_calidad_aire.py`: Lectura desde MQ135 o CCS811.
- `sensor_presencia.py`: Gestión del HC-SR04 y verificación de cercanía.
- `sensor_pir.py`: Detección de movimiento pasivo por infrarrojo (PIR).
- `sensor_imu.py`: Lectura de acelerómetro/giroscopio para detección de movimiento o inclinación.
- `sensor_reloj.py`: Interfaz con RTC DS3231.
- `sensor_nfc.py`: Lectura de identificadores desde PN532.
- `sensor_ble.py`: Detección de dispositivos cercanos por Bluetooth.
- `sensor_base.py`: Clase abstracta base para definir sensores compatibles con el sistema.
- `eventos_sensores.py`: Generación y publicación de eventos interpretados.
- `config_sensores.py`: Parámetros como frecuencia de lectura, umbrales de alerta, etc.
- `utils_sensores.py`: Funciones comunes (conversión de unidades, validación, normalización).