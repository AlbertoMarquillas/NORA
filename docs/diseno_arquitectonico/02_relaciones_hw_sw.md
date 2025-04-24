# Relaciones entre Hardware y Módulos de Software – Sistema NORA

Este documento establece las conexiones funcionales directas entre cada componente físico (hardware) y los módulos de software que los gestionan. Sirve como referencia base para el diseño del diagrama conceptual global.

## Tabla 1: Hardware → Módulos de software

| Componente Hardware                      | Módulo Software que lo gestiona          |
|-----------------------------------------|------------------------------------------|
| Cámara (CSI o USB)                      | `vision/`                                 |
| Micrófono (USB o analógico)             | `voz/`                                    |
| Altavoz (jack, USB, + amplificador)     | `voz/`                                    |
| Pantalla facial animada (OLED/TFT SPI) | `interfaz/`                               |
| LEDs RGB WS2812                         | `interfaz/`                               |
| LEDs indicadores (5mm, RGB)             | `interfaz/`                               |
| Servomotores SG90/MG90                  | `interfaz/`                               |
| Sensor de presencia ultrasónico HC-SR04 | `sensores/`                               |
| Sensor temperatura/humedad DHT22/BME280 | `sensores/`                               |
| Sensor de luminosidad TSL2561           | `sensores/`                               |
| Sensor de calidad del aire MQ135/CCS811 | `sensores/`                               |
| Reloj RTC externo DS3231                | `sensores/` → `sistema/` (sincronización) |
| Módulo NFC PN532                        | `sensores/` → `activacion/`               |
| Módulo Bluetooth (HC-05 / BLE)          | `sensores/`                               |
| Botón físico GPIO                       | `activacion/`                             |
| Expansor I/O PCF8574                    | `control/`                                |
| Fuente de alimentación (5V 3A)          | — (sin gestión directa por software)     |
| Chasis físico / carcasa impresa         | — (estructura pasiva, sin control)        |
| Base de datos SQLite                    | `datos/`                                  |

## Tabla 2: Módulos de software → Hardware gestionado

| Módulo Software     | Componentes Hardware gestionados                                                          |
|---------------------|-------------------------------------------------------------------------------------------|
| `vision/`           | Cámara                                                                                    |
| `voz/`              | Micrófono, Altavoz                                                                        |
| `interfaz/`         | Pantalla facial, LEDs RGB, LEDs indicadores, Servos                                      |
| `datos/`            | Base de datos SQLite (sin hardware físico)                                               |
| `sistema/`          | RTC (sin acceso físico directo, vía `sensores/`)                                         |
| `activacion/`       | Eventos de NFC, botón físico, presencia, atención visual, hotword (no accede a hardware) |
| `gui/`              | (No controla hardware directamente, usa `sistema/`, `datos/`, `interfaz/`)               |
| `models/`           | (No aplica – módulo lógico para modelos de IA)                                           |
| `utils/`            | (No aplica – funciones auxiliares)                                                       |
| `tests/`            | (Accede a todos los dispositivos para validación)                                        |
| `control/`          | Expansor I/O PCF8574, comandos de GPIO, estado del sistema                               |
| `sensores/`         | Todos los sensores físicos: temperatura, luz, calidad del aire, presencia, NFC, RTC, BLE |

