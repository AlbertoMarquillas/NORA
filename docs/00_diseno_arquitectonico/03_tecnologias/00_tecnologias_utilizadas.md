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

### Sistema

- **Tecnologías empleadas:**

  - `transitions`
  - `asyncio`
  - `queue`
  - `pyee`
  - `eventbus`

- **Justificación:**

  - `transitions`: permite gestionar de forma estructurada y eficiente la máquina de estados finita (FSM) que orquesta el comportamiento global de NORA.
  - `asyncio`: soporta la ejecución concurrente de tareas relacionadas con eventos y transiciones de estado en tiempo real.
  - `queue`: facilita la gestión interna de eventos y comandos mediante colas de mensajes seguras y asincrónicas.
  - `pyee`, `eventbus`: utilizados para el enrutamiento de eventos entre módulos y agentes, asegurando una comunicación robusta.

- **Instalación:**

  - `pip install transitions`

- **Alternativas:**

  - Implementación manual de FSM mediante clases y `asyncio`.
  - Uso de librerías más avanzadas como `Sismic` si en el futuro se requiere modelado visual de la FSM.


### Interfaz

- **Tecnologías empleadas:**

  - `rpi_ws281x`
  - `neopixel`
  - `RPi.GPIO`
  - `pigpio`
  - `Pillow`
  - `PyGame`
  - `PyQt5`
  - `tkinter`

- **Justificación:**

  - `rpi_ws281x`, `neopixel`: control de tiras LED WS2812 con alta precisión de temporización.
  - `RPi.GPIO`, `pigpio`: control directo de pines GPIO para LEDs y servomotores.
  - `Pillow`: creación de gráficos y animaciones para pantallas OLED/TFT.
  - `PyGame`, `PyQt5`, `tkinter`: opciones para implementación de interfaces gráficas y simuladores visuales.

- **Instalación:**

  - `pip install rpi_ws281x neopixel RPi.GPIO pigpio Pillow pygame pyqt5`

- **Alternativas:**

  - Uso de controladores LED SPI más avanzados como `DotStar` en lugar de WS2812 si se necesita mayor rendimiento.
  - Sustitución de `PyGame` o `tkinter` por `Kivy` para interfaces gráficas más dinámicas.

### Diálogo

- **Tecnologías empleadas:**

  - `transformers`
  - `sentence-transformers`
  - `nltk`
  - `spacy`
  - `json`

- **Justificación:**

  - `transformers`, `sentence-transformers`: permiten implementar modelos ligeros de NLU (Natural Language Understanding) y NLG (Natural Language Generation), optimizados para reconocimiento de intención y generación de texto.
  - `nltk`, `spacy`: herramientas de procesamiento de lenguaje natural para análisis sintáctico, corrección y normalización de texto.
  - `json`: formato ligero para gestionar la configuración dinámica de diálogos, respuestas predefinidas y estructuras de intención.

- **Instalación:**

  - `pip install transformers sentence-transformers nltk spacy`

- **Alternativas:**

  - Utilizar `Rasa NLU/NLG` para procesamiento conversacional si se requiere una solución embebida más estructurada.
  - Migrar en el futuro a `LLama.cpp` o implementaciones similares si se busca optimización en dispositivos ARM.

## Datos

- **Tecnologías empleadas:**

  - `sqlite3`
  - `dataset`
  - `SQLAlchemy`
  - `json`
  - `datetime`

- **Justificación:**

  - `sqlite3`, `dataset`, `SQLAlchemy`: gestión de bases de datos ligeras y persistencia estructurada de información en dispositivos locales.
  - `json`: almacenamiento flexible de configuraciones, registros de eventos y datos no relacionales.
  - `datetime`: gestión precisa de marcas de tiempo en historiales, rutinas, y registros de hábitos.

- **Instalación:**

  - `pip install dataset sqlalchemy`

- **Alternativas:**

  - Uso de `TinyDB` para almacenamiento JSON puro en sistemas extremadamente limitados.
  - Uso de `DuckDB` para consultas analíticas más complejas si el historial de datos crece considerablemente.

## Control

- **Tecnologías empleadas:**

  - `RPi.GPIO`
  - `gpiozero`
  - `smbus2`
  - `psutil`
  - `os`
  - `subprocess`
  - `logging`

- **Justificación:**

  - `RPi.GPIO`, `gpiozero`: gestión de entradas y salidas digitales (GPIO) para control de periféricos físicos.
  - `smbus2`: comunicación I2C con expansores de I/O y otros dispositivos.
  - `psutil`: monitorización avanzada de estado del sistema (CPU, memoria, redes).
  - `os`, `subprocess`: ejecución de comandos del sistema operativo para control de energía, red y tareas administrativas.
  - `logging`: registro estructurado de eventos de diagnóstico y operación.

- **Instalación:**

  - `pip install RPi.GPIO gpiozero smbus2 psutil`

- **Alternativas:**

  - Uso de `pigpio` en lugar de `RPi.GPIO` si se requiere control de PWM y gestión remota de GPIOs más precisa.
  - `supervisor` o `systemd` para gestionar demonios de control de procesos si se amplía el sistema.

## GUI

- **Tecnologías empleadas:**

  - `tkinter`
  - `PyQt5`
  - `PySide2`
  - `flask`
  - `dash`
  - `streamlit`

- **Justificación:**

  - `tkinter`, `PyQt5`, `PySide2`: creación de interfaces gráficas locales para control, diagnóstico y configuración del sistema NORA.
  - `flask`, `dash`, `streamlit`: exposición de la GUI vía servidor web local o remoto para administración distribuida.

- **Instalación:**

  - `pip install tkinter pyqt5 pyside2 flask dash streamlit`

- **Alternativas:**

  - Uso de `DearPyGui` o `Gradio` para interfaces más ligeras si se busca reducir la carga gráfica o simplificar el despliegue web.

## Models

- **Tecnologías empleadas:**

  - `TensorFlow`
  - `PyTorch`
  - `scikit-learn`
  - `MediaPipe`
  - `transformers`
  - `sentence-transformers`
  - `OpenCV`
  - `numpy`

- **Justificación:**

  - `TensorFlow`, `PyTorch`: gestión y ejecución de modelos de IA en visión, voz, emociones y hábitos.
  - `scikit-learn`: modelos ligeros de clasificación y análisis de hábitos o datos estructurados.
  - `MediaPipe`: detección de gestos, poses y reconocimiento facial de forma optimizada.
  - `transformers`, `sentence-transformers`: procesamiento avanzado de lenguaje natural para NLU y embeddings textuales.
  - `OpenCV`: preprocesamiento de imágenes para modelos de visión artificial.
  - `numpy`: manipulación de matrices y tensores de entrada y salida de modelos.

- **Instalación:**

  - `pip install tensorflow torch scikit-learn mediapipe transformers sentence-transformers opencv-python numpy`

- **Alternativas:**

  - Uso de `ONNX Runtime` para ejecutar modelos optimizados en dispositivos con recursos limitados.
  - Uso de `tflite` para optimizar modelos TensorFlow destinados a microcontroladores o Raspberry Pi.

## Utils

- **Tecnologías empleadas:**

  - `json`
  - `yaml`
  - `logging`
  - `math`
  - `datetime`
  - `os`
  - `random`
  - `numpy`

- **Justificación:**

  - `json`, `yaml`: gestión de configuraciones flexibles y estructuradas.
  - `logging`: registro estructurado de eventos y estados internos del sistema.
  - `math`, `numpy`: cálculos matemáticos, operaciones vectoriales y estadísticas básicas.
  - `datetime`: gestión de tiempos y marcas temporales.
  - `os`: gestión de rutas, archivos y operaciones del sistema operativo.
  - `random`: generación de decisiones estocásticas controladas.

- **Instalación:**

  - `pip install pyyaml numpy`

- **Alternativas:**

  - Uso de `configparser` para configuraciones más simples basadas en INI.
  - Uso de `pydantic` para validación estricta de configuraciones JSON en proyectos que requieran robustez adicional.

## Utils

- **Tecnologías empleadas:**

  - `json`
  - `yaml`
  - `logging`
  - `math`
  - `datetime`
  - `os`
  - `random`
  - `numpy`

- **Justificación:**

  - `json`, `yaml`: gestión de configuraciones flexibles y estructuradas.
  - `logging`: registro estructurado de eventos y estados internos del sistema.
  - `math`, `numpy`: cálculos matemáticos, operaciones vectoriales y estadísticas básicas.
  - `datetime`: gestión de tiempos y marcas temporales.
  - `os`: gestión de rutas, archivos y operaciones del sistema operativo.
  - `random`: generación de decisiones estocásticas controladas.

- **Instalación:**

  - `pip install pyyaml numpy`

- **Alternativas:**

  - Uso de `configparser` para configuraciones más simples basadas en INI.
  - Uso de `pydantic` para validación estricta de configuraciones JSON en proyectos que requieran robustez adicional.

## Tests

- **Tecnologías empleadas:**

  - `unittest`
  - `pytest`
  - `doctest`
  - `coverage`
  - `faker`
  - `mock`
  - `timeit`

- **Justificación:**

  - `unittest`, `pytest`: frameworks estándar y avanzados para pruebas unitarias y de integración.
  - `doctest`: validación de ejemplos embebidos en documentación.
  - `coverage`: análisis de cobertura de pruebas para garantizar calidad de software.
  - `faker`: generación de datos simulados realistas para escenarios de prueba.
  - `mock`: simulación de objetos y comportamientos para pruebas controladas.
  - `timeit`: medición precisa del tiempo de ejecución para evaluar rendimiento.

- **Instalación:**

  - `pip install pytest coverage faker`

- **Alternativas:**

  - `hypothesis` para pruebas basadas en propiedades en lugar de casos concretos.
  - Integración de herramientas de CI como `GitHub Actions` para ejecución automática de pruebas en pipelines de desarrollo.
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

> Actualización: Inclusión de dependencias de submódulos específicos de los módulos `vision/`, `voz/`, `sensores/`, `activacion/`, `agentes/`, `sistema/`, `interfaz/` y `dialogo/`.

