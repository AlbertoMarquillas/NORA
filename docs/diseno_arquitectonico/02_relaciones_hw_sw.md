# 03 – Relaciones entre Hardware y Módulos de Software – Sistema NORA

Este documento define las correspondencias funcionales entre los elementos físicos (hardware) y los módulos de software que los gestionan dentro de la arquitectura de NORA. Incluye, cuando es relevante, la mediación de los agentes (`/agentes/`) en la interpretación, modulación o decisión sobre estos dispositivos. Esta relación es clave para la construcción del grafo conceptual general del sistema.

---

## Tabla 1: Hardware → Módulos de software

| Componente Hardware                     | Módulo Software que lo gestiona        | Agente(s) implicado(s)                           |
|-----------------------------------------|----------------------------------------|--------------------------------------------------|
| Cámara (CSI o USB)                      | `vision/`                              | Visual                                           |
| Micrófono (USB o analógico)             | `voz/`                                 | Auditivo, Emocional                              |
| Altavoz (jack, USB, + amplificador)     | `voz/`                                 | Expresivo                                        |
| Pantalla facial animada (OLED/TFT SPI)  | `interfaz/`                            | Expresivo                                        |
| LEDs RGB WS2812                         | `interfaz/`                            | Expresivo, Estado                                |
| LEDs indicadores (5mm, RGB)             | `interfaz/`                            | Estado                                           |
| Servomotores SG90/MG90                  | `interfaz/`                            | Expresivo, Orientación                           |
| Sensor de presencia ultrasónico HC-SR04 | `sensores/` → `activacion/`            | Activación, Entorno                              |
| Sensor temperatura/humedad DHT22/BME280 | `sensores/`                            | Ambiental, Confort                               |
| Sensor de luminosidad TSL2561           | `sensores/`                            | Contexto visual                                  |
| Sensor de calidad del aire MQ135/CCS811 | `sensores/`                            | Ambiental, Salud                                 |
| Reloj RTC externo DS3231                | `sensores/` → `sistema/`               | Cronología                                       |
| Módulo NFC PN532                        | `sensores/` → `activacion/`            | Identificación, Activación                       |
| Módulo Bluetooth (HC-05 / BLE)          | `sensores/`                            | Proximidad, Activación                           |
| Botón físico GPIO                       | `activacion/`                          | Activación                                       |
| Módulo WiFi adicional (ESP8266)         | `control/`                             | Conectividad                                     |
| Expansor I/O PCF8574                    | `control/`                             | Gestión GPIO                                     |
| Fuente de alimentación (5V 3A)          | — (sin gestión directa por software)   | —                                                |
| Chasis físico / carcasa impresa         | — (estructura pasiva, sin control)     | —                                                |
| Almacenamiento externo (USB SSD/HDD)    | `datos/`                               | Datos persistentes, Perfiles, Multimedia         |

---

## Tabla 2: Módulos de software → Hardware gestionado

| Módulo Software     | Componentes Hardware gestionados                                                                                        |
|---------------------|-------------------------------------------------------------------------------------------------------------------------|
| `vision/`           | Cámara CSI/USB                                                                                                          |
| `voz/`              | Micrófono, Altavoz + Amplificador                                                                                       |
| `interfaz/`         | Pantalla facial animada, LEDs RGB WS2812, LEDs indicadores, Servomotores                                                |
| `datos/`            | Almacenamiento externo (HDD/SSD), sin control físico directo sobre el medio                                             |
| `sistema/`          | RTC (via `sensores/`), lógica FSM, estados emocionales (actúa sobre `interfaz/`, `voz/`)                                |
| `activacion/`       | Botón físico, eventos desde NFC, presencia ultrasónica, Bluetooth (todos vía `sensores/`)                               |
| `gui/`              | No accede a hardware directamente. Supervisa e interactúa indirectamente con `control/`, `sistema/`, `voz/`, `interfaz/`|
| `models/`           | Sin acceso a hardware. Requiere hardware para inferencias, pero se accede a través de `vision/`, `voz/`, `dialogo/`     |
| `utils/`            | Sin acceso a hardware. Proporciona funciones de soporte matemático, temporización, eventos.                             |
| `tests/`            | Accede a todos los componentes hardware durante pruebas. Valida comunicación y respuesta mediante scripts específicos.  |
| `control/`          | GPIOs físicos, expansor I/O PCF8574, fuente WiFi adicional, supervisión de estado de sistema embebido                   |
| `sensores/`         | Todos los sensores ambientales: DHT22/BME280, MQ135/CCS811, TSL2561, HC-SR04, NFC PN532, RTC, módulo Bluetooth          |
| `dialogo/`          | Sin hardware propio. Genera texto que se convierte en audio (`voz/`), o en expresiones (`interfaz/`).                   |
| `agentes/`          | Sin acceso directo a hardware. Coordina decisiones y modula salidas de `interfaz/`, `voz/`, `sistema/`                  |