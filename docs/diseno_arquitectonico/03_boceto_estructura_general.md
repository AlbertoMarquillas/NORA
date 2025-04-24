───────────────────────────────
      BLOQUES DE HARDWARE
───────────────────────────────

[1] Dispositivos de Entrada Directa (Interacción Humana)
 ├── Micrófono USB
 ├── Cámara CSI o USB
 ├── Sensor ultrasónico HC-SR04
 ├── Módulo NFC PN532
 ├── Módulo Bluetooth (HC-05 / BLE)
 └── Botón físico (GPIO)

[2] Sensores Ambientales (Contexto del entorno)
 ├── Sensor de temperatura y humedad (DHT22 / BME280)
 ├── Sensor de luminosidad (TSL2561)
 ├── Sensor de calidad del aire (MQ-135 / CCS811)
 └── Reloj en tiempo real (RTC DS3231)

[3] Dispositivos de Salida y Expresión
 ├── Altavoz + Amplificador (audio)
 ├── Pantalla OLED o TFT SPI (rostro visual)
 ├── LEDs RGB WS2812 y LEDs indicadores (señalización)
 └── Servomotores SG90 / MG90 (movimiento físico)

[4] Infraestructura Técnica
 ├── Raspberry Pi 4 Model B (núcleo computacional)
 ├── Fuente de alimentación 5V 3A (USB-C)
 ├── Almacenamiento externo USB (SSD / HDD)
 ├── Expansor I/O PCF8574 (extensión GPIO vía I²C)
 └── Módulo WiFi externo (ESP8266 / NodeMCU) — para control de dispositivos IoT

────────────────────────────────────────────
       BLOQUES DE SOFTWARE – SISTEMA NORA
────────────────────────────────────────────

[1] Módulos de Entrada Sensorial
 ├── `voz/`           → Reconocimiento de voz (ASR), síntesis (TTS), análisis emocional
 ├── `vision/`        → Detección facial, atención, postura, gestos, emociones visuales
 ├── `sensores/`      → Lectura y validación de sensores físicos ambientales
 └── `activacion/`    → Gestión de activación multisensorial (hotword, NFC, botón, etc.)

[2] Módulo de Coordinación Inteligente
 └── `agentes/`       → Evaluación contextual, modulación emocional, decisiones perceptivas

[3] Núcleo Lógico del Sistema
 └── `sistema/`       → FSM de control general, coordinación intermodular, respuestas globales

[4] Módulos de Salida y Expresión
 ├── `interfaz/`      → Control de LEDs, pantalla, servos (expresión física y visual)
 ├── `voz/`           → Generación de audio hablado (respuesta al usuario)
 └── `dialogo/`       → NLU, gestión de contexto y generación de texto conversacional

[5] Módulo de Persistencia de Información
 └── `datos/`         → Rutinas, notas, perfiles, historial emocional, agenda, hábitos

[6] Módulo de Control del Sistema
 └── `control/`       → Inicialización hardware, GPIO, RTC, WiFi externo, logs, energía

[7] Interfaz Técnica para el Desarrollador
 └── `gui/`           → Panel de eventos, pruebas, configuración, monitoreo

[8] Módulos de Soporte
 ├── `models/`        → Modelos IA (visión, voz, diálogo, hábitos, emociones)
 ├── `utils/`         → Funciones auxiliares: parsers, logging, cálculos
 └── `tests/`         → Pruebas unitarias, integración, validación de hardware

──────────────────────────────────────────────────────────────
       RELACIÓN ENTRE HARDWARE Y MÓDULOS DE SOFTWARE
──────────────────────────────────────────────────────────────

[Micrófono USB]             → `voz/`
[Cámara CSI o USB]          → `vision/`
[Sensor ultrasónico HC-SR04] → `sensores/` (lectura de distancia) + `control/` (detecta presencia física para activar el sistema)
[Botón físico (GPIO)]       → `activacion/` ← usa eventos de `sensores/`
[Módulo NFC PN532]          → `sensores/` → eventos para `activacion/`
[Módulo Bluetooth]          → `sensores/` → eventos para `activacion/`

[Sensor T/H DHT22/BME280]   → `sensores/`
[Sensor luz TSL2561]        → `sensores/`
[Sensor aire MQ-135/CCS811] → `sensores/`
[RTC DS3231]                → `sensores/` + `control/` (sincronización)

[Altavoz + Amplificador]    → `voz/` (salida TTS)
[Pantalla OLED/TFT SPI]     → `interfaz/`
[LEDs RGB / indicadores]    → `interfaz/`
[Servomotores SG90/MG90]    → `interfaz/`

[Raspberry Pi 4 Model B]    → Plataforma base (todos los módulos)
[Alimentación 5V 3A]        → No gestionado por software
[Almacenamiento externo USB]→ `datos/`
[Expansor I/O PCF8574]      → `control/`
[Módulo WiFi externo ESP8266] → `control/` (comunicación IoT, MQTT/HTTP)

──────────────────────────────────────────────────────────────

