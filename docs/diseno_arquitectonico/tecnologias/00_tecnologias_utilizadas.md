# Tecnologías y Librerías utilizadas en NORA

## Introducción

Este documento recoge las tecnologías, librerías y entornos de ejecución utilizados en el proyecto **NORA**, un sistema embebido inteligente que combina visión artificial, procesamiento de voz, expresividad física y coordinación basada en agentes. El objetivo es proporcionar una referencia técnica clara y mantenible, permitiendo futuras extensiones o actualizaciones tecnológicas de manera sistemática.

La información está organizada por **módulo funcional**, indicando las tecnologías empleadas, su justificación técnica, forma de instalación y alternativas relevantes.

---

## Tecnologías por Módulo Funcional

### Visión

- **Tecnologías empleadas:**
  - `OpenCV`
  - `MediaPipe`
  - `TensorFlow` / `TensorFlow Lite` / `PyTorch` (modelos avanzados)
  - `NumPy`
  - `asyncio` (para procesamiento no bloqueante)
  - `os`, `pathlib` (manejo de rutas y archivos locales)
  - `datetime`, `json`, `math`, `copy`, `yaml`, `collections` (gestión de eventos, configuraciones, cálculos auxiliares y estructuras de datos)
  - `utils_datos.py` (módulo interno para gestión de usuarios)

- **Justificación:**
  - `OpenCV`: captura eficiente de vídeo en tiempo real en Raspberry Pi.
  - `MediaPipe`: detección facial, postural y de gestos optimizada para dispositivos de bajo consumo.
  - `TensorFlow`/`TensorFlow Lite`/`PyTorch`: soporte de modelos personalizados de reconocimiento visual, análisis emocional y secuencias gestuales.
  - `NumPy`: procesamiento matricial para análisis geométrico y tensores de inferencia.
  - `asyncio`: permite la ejecución cooperativa de tareas en ciclos de procesamiento de frames.
  - `os` y `pathlib`: gestión robusta y multiplataforma de rutas y archivos de modelos.
  - `datetime`, `json`, `math`, `copy`, `yaml`, `collections`: soporte estructurado para emisión de eventos, serialización de datos, cálculos geométricos, normalización y gestión eficiente de datos temporales.
  - `utils_datos.py`: acceso y gestión local de perfiles de usuario registrados.

- **Instalación:**
  - `pip install opencv-python mediapipe numpy tensorflow torch pyyaml`

- **Alternativas:**
  - `dlib`, `face_recognition` para identificación facial offline.
  - `YOLOv5` entrenado específicamente para tareas ligeras.

### Voz

- **Tecnologías empleadas:**

  - `Vosk`
  - `Whisper` (pequeño modelo para offline)
  - `pyttsx3`
  - `webrtcvad`
  - `pyaudio`
  - `numpy`
  - `scipy`
  - `spacy`
  - `nltk`
  - `transformers`
  - `pyee` o `eventbus`
  - `librosa`
  - `unidecode`
  - `tensorflow`
  - `torch`

- **Justificación:**

  - `Vosk` y `Whisper`: reconocimiento de voz offline, manteniendo privacidad y reduciendo latencia.
  - `pyttsx3`: síntesis de voz sin necesidad de conexión.
  - `webrtcvad`: detección robusta de actividad vocal mediante análisis de energía y espectro.
  - `pyaudio`: captura y reproducción de audio en formato PCM.
  - `numpy`: procesamiento eficiente de señales de audio (arrays PCM).
  - `scipy`: análisis espectral, detección de pausas, métricas de energía y frecuencia.
  - `spacy` y `nltk`: procesamiento de lenguaje natural para extracción de comandos e interpretación de intenciones.
  - `transformers`: implementación de modelos avanzados para comprensión y clasificación de texto.
  - `pyee` o `eventbus`: gestión estructurada de eventos internos relacionados con el reconocimiento y síntesis de voz.
  - `librosa`: extracción avanzada de características acústicas como tono, ritmo y volumen para análisis emocional de la voz.
  - `unidecode`: normalización ortográfica de texto, eliminación de acentos y caracteres especiales para mejorar procesamiento ASR y TTS.
  - `tensorflow` y `torch`: entrenamiento adaptativo offline de modelos de ASR personalizados y mejora de vocabulario.

- **Instalación:**

  - `pip install vosk pyttsx3 webrtcvad pyaudio numpy scipy spacy nltk transformers pyee librosa unidecode tensorflow torch`

- **Alternativas:**

  - `SpeechRecognition` + `PocketSphinx` como stack más ligero.
  - `Silero VAD` como alternativa a WebRTC VAD.
  - `snowboy` o `porcupine` para detección especializada de hotword ("oye NORA").
### Sensores

- **Tecnologías empleadas:**

  - `gpiozero`
  - `smbus2`
  - `adafruit_dht`
  - `adafruit_tsl2561`
  - `bleak`
  - `paho-mqtt`
  - `ntplib`
  - `pyserial`
  - `pyyaml`

- **Justificación:**

  - `gpiozero`: abstracción de GPIOs para lectura de sensores físicos en Raspberry Pi.
  - `smbus2`: comunicación I²C para sensores ambientales, de calidad de aire y RTC.
  - `adafruit_dht`: gestión de sensores de temperatura y humedad como DHT22.
  - `adafruit_tsl2561`: gestión de sensores de luminosidad ambiental mediante I²C.
  - `bleak`: conexión BLE (Bluetooth Low Energy) para detección de dispositivos cercanos.
  - `paho-mqtt`: soporte para eventos distribuidos y comunicación ligera basada en MQTT.
  - `ntplib`: sincronización de fecha y hora mediante servidores NTP.
  - `pyserial`: comunicación UART para lectura de datos de sensores NFC u otros dispositivos serie.
  - `pyyaml`: carga y gestión de configuraciones externas en formato YAML.

- **Instalación:**

  - `pip install gpiozero smbus2 adafruit-circuitpython-dht adafruit-circuitpython-tsl2561 bleak paho-mqtt ntplib pyserial pyyaml`

- **Alternativas:**

  - `RPi.GPIO` para control manual de GPIOs.
  - Implementación nativa de protocolos BLE usando `bluepy` en entornos limitados.
  - Manejo manual de sensores I²C a través de `python-periphery`.
### Activación

- **Tecnologías empleadas:**

  - `gpiozero`
  - `pyee` o `eventbus`

- **Justificación:**

  - `gpiozero`: lectura de pulsadores físicos conectados a GPIO para activación manual del sistema.
  - `pyee` o `eventbus`: gestión de eventos internos de activación de manera estructurada y eficiente.

- **Instalación:**

  - `pip install gpiozero pyee`

- **Alternativas:**

  - `RPi.GPIO` como alternativa para control manual de pulsadores.
  - Sistemas de eventos personalizados utilizando `asyncio` puro para entornos ligeros.

### Agentes

- **Tecnologías empleadas:**

  - `pyee`
  - `eventbus`
  - `asyncio`
  - `mediapipe`
  - `opencv-python`
  - `vosk`
  - `whisper`
  - `pyttsx3`
  - `webrtcvad`
  - `tensorflow`
  - `torch`
  - `dlib`
  - `face_recognition`
  - `pandas`
  - `paho-mqtt`

- **Justificación:**

  - `pyee` y `eventbus`: gestión de eventos internos entre agentes para coordinación inteligente.
  - `asyncio`: programación asíncrona eficiente para la ejecución concurrente de agentes perceptivos, expresivos y de decisión.
  - `mediapipe`: procesamiento visual avanzado para la detección de rostros, poses y gestos que nutren la toma de decisiones de agentes perceptivos.
  - `opencv-python`: procesamiento de imágenes y apoyo en tareas de análisis visual avanzado.
  - `vosk`: motor ligero de reconocimiento de voz offline.
  - `whisper`: modelo de transcripción de voz basado en deep learning.
  - `pyttsx3`: síntesis de voz offline sin necesidad de servicios externos.
  - `webrtcvad`: detección eficiente de actividad vocal en señales de audio.
  - `tensorflow`: modelos de deep learning para clasificación y análisis emocional.
  - `torch`: soporte para modelos adaptativos de aprendizaje profundo.
  - `dlib`: detección de rostros y características faciales.
  - `face_recognition`: extracción y análisis de emociones faciales.
  - `pandas`: análisis de patrones de hábitos del usuario y procesamiento de datos históricos.
  - `paho-mqtt`: comunicación en tiempo real con sistemas externos de monitoreo de seguridad.

- **Instalación:**

  - `pip install pyee mediapipe opencv-python vosk whisper pyttsx3 webrtcvad tensorflow torch dlib face_recognition pandas paho-mqtt`

- **Alternativas:**

  - Implementación de un sistema propio de enrutamiento de eventos usando colas `asyncio.Queue`.
  - Uso de `OpenPose` o `DeepFace` para tareas específicas de detección visual y reconocimiento emocional.
  - Empleo de servicios cloud para reconocimiento y síntesis de voz (Google Speech-to-Text, Amazon Polly) si se admite conectividad.
  - Alternativas a `pandas`: `Polars` para procesamiento de datos más eficiente en ciertos entornos.

### Interacción y Expresividad

- **Tecnologías empleadas:**

  - `rpi_ws281x`, `neopixel` (control LEDs WS2812)
  - `RPi.GPIO`, `gpiozero`, `pigpio` (PWM para servos)
  - `Pillow`, `PyGame` (visualización facial)

- **Justificación:**

  - Librerías optimizadas para Raspberry Pi.
  - Control simultáneo de múltiples salidas expresivas (luz, pantalla, movimiento).

- **Instalación:**

  - `pip install rpi_ws281x neopixel RPi.GPIO gpiozero pigpio pillow pygame`

- **Alternativas:**

  - `PyQt5` para visualización más avanzada.
  - `Adafruit CircuitPython` para unificación de control de LEDs y servos.

### Control General

- **Tecnologías empleadas:**

  - `psutil`, `os`, `subprocess`, `logging`
  - `flask` o `websocket` (opcional para control remoto)

- **Justificación:**

  - Supervisión del sistema operativo y hardware mediante librerías ligeras.
  - Opcionalmente exponer control técnico vía navegador.

- **Instalación:**

  - `pip install psutil flask websocket-client`

- **Alternativas:**

  - `dash`, `streamlit` para paneles de control rápidos.

### Activación NFC

- **Tecnologías empleadas:**

  - `Adafruit_PN532` (librería de comunicación NFC)

- **Justificación:**

  - Soporte directo para Raspberry Pi y múltiples protocolos (I2C, UART, SPI).

- **Instalación:**

  - `pip install adafruit-circuitpython-pn532`

- **Alternativas:**

  - Implementación manual del protocolo NFC en Python usando `smbus2`.

### Almacenamiento Local

- **Tecnologías empleadas:**

  - `sqlite3`
  - `dataset` (ORM opcional)

- **Justificación:**

  - `sqlite3` está integrado en Python, sin necesidad de servicios externos.
  - `dataset` simplifica el acceso estructurado a bases de datos pequeñas.

- **Instalación:**

  - `pip install dataset`

- **Alternativas:**

  - `SQLAlchemy` para bases de datos más complejas o migraciones.

---

## Entorno de Desarrollo General

- **Lenguaje:** Python 3.9+
- **Sistema operativo:** Raspberry Pi OS Lite (basado en Debian)
- **Herramientas adicionales:**
  - `pytest`, `coverage` para pruebas unitarias y análisis de cobertura.
  - `draw.io`, `mkdocs` para documentación técnica.
  - `git`, `pre-commit` para control de versiones y calidad de código.

---

## Conclusiones y Justificación Técnica General

El stack tecnológico seleccionado para **NORA** prioriza:

- **Ejecución offline:** procesamiento local de voz, visión y datos para preservar privacidad y garantizar funcionamiento autónomo.
- **Compatibilidad embebida:** todas las librerías y herramientas son ejecutables en una Raspberry Pi 4 sin necesidad de aceleradores externos.
- **Eficiencia y soporte:** se utilizan tecnologías ampliamente documentadas, con alta disponibilidad de actualizaciones y soluciones comunitarias.
- **Flexibilidad y modularidad:** la arquitectura desacoplada permite sustituir componentes tecnológicos de manera fácil en el futuro.

**Riesgos identificados:**

- Dependencia de librerías específicas que podrían quedar obsoletas (ej. `vosk`, `rpi_ws281x`).
- Cambios de versiones de TensorFlow/PyTorch que puedan afectar la compatibilidad.

**Planes de mitigación:**

- Diseño modular que facilita el reemplazo de tecnologías.
- Documentación constante de versiones probadas y recomendaciones de migración.
- Validación periódica de compatibilidad en nuevas versiones de Raspberry Pi OS.

---

> Documento ubicado en `docs/arquitectura_sistema/tecnologias/tecnologias_utilizadas.md`

> Versión inicial: 26 Abril 2025.

> Actualización: Inclusión de dependencias de submódulos específicos de los módulos `vision/`, `voz/`, `sensores/`, `activacion/` y `agentes/`.

