# Bloques de Software del Sistema NORA

Este documento define los módulos funcionales principales que componen la lógica del asistente físico inteligente NORA. Cada módulo responde a una responsabilidad específica, permitiendo una arquitectura desacoplada y escalable.

## 1. `vision/` – Módulo de percepción visual
**Función:** Gestión de la entrada visual mediante cámara: detección de presencia, rostro y orientación del usuario. Este módulo sirve como entrada sensorial primaria para determinar si el asistente debe activarse o responder.

### Subfunciones:

1. **Detección facial:**
   - Localiza el rostro en el campo visual.
   - Genera `EVT_FACE_DETECTED`, con bounding box y coordenadas relativas.
   - Opcional: cálculo del centroide y distancia estimada (con escala aproximada).

2. **Estimación de postura:**
   - Opcional en versión avanzada: identifica si el usuario está de pie, sentado, inclinado, etc.
   - Puede activar estados como `EVT_POSTURE_ALERT` (ej: usuario encorvado).

3. **Seguimiento de atención (orientación del rostro):**
   - Estima si el usuario está mirando hacia el asistente.
   - Genera `EVT_ATTENTION_GAINED` / `EVT_ATTENTION_LOST`.

4. **Detección de presencia:**
   - Mecanismo ligero (por cambio de fondo o detección de movimiento) para saber si hay alguien delante.
   - Evento `EVT_PRESENCE_DETECTED`, activador de standby.

5. **Reconocimiento de objetos (Object Detection):**
   - Identifica elementos del entorno relevantes (personas, mobiliario, dispositivos).
   - Permite el comando: “¿Qué es eso?” o interacciones contextuales.
   - Evento: `EVT_OBJECT_RECOGNIZED`.

6. **Reconocimiento de gestos simbólicos:**
   - Detecta gestos como señalar, levantar la mano o saludar.
   - Soporta interacciones como “mira allí” o “ven aquí”.
   - Eventos: `EVT_GESTURE_POINT_LEFT`, `EVT_GESTURE_WAVE`, etc.

7. **Reconocimiento de lenguaje de signos básico:**
   - Detección de signos preentrenados en LSE o ASL para usuarios mudos.
   - Evento: `EVT_SIGN_RECOGNIZED` con payload.

8. **Análisis de emociones (emociones faciales):**
   - Estima el estado emocional del usuario: feliz, enfadado, triste, neutral.
   - Afecta la modulación de respuestas y expresividad del sistema.
   - Evento: `EVT_EMOTION_CHANGED`.


### Entradas:
- Vídeo en tiempo real desde cámara CSI o USB (formato OpenCV).
- Parámetros configurables desde `config.json` o sistema de preferencias (`FPS`, `ROI`, `limites de atención`, etc.).

### Salidas:
- Eventos internos al sistema:  
  `EVT_FACE_DETECTED`, `EVT_ATTENTION_GAINED`, `EVT_PRESENCE_DETECTED`, `EVT_POSTURE_ALERT`, etc.
- Diccionario de datos para `EventManager` o módulo `sistema/`.

### Dependencias externas:

- `OpenCV` para captura y análisis de vídeo.
- `MediaPipe` para detección facial, pose y seguimiento de orientación.
- `TensorFlow` o `PyTorch` para cargar modelos de reconocimiento de gestos, signos, objetos y emociones.
- Modelos preentrenados compatibles: `YOLOv5/YOLOv8`, `Teachable Machine`, `OpenPose`.
- `NumPy` para manipulación de matrices de imagen y cálculos geométricos.
- `scikit-learn` (opcional) para clasificación emocional ligera.
- `dlib` o `face_recognition` (opcional) si se desea identificación de usuarios por rostro.


## 2. `voz/` – Módulo de procesamiento de voz

**Función:** Permite la comunicación natural entre el usuario y NORA mediante reconocimiento de voz (ASR) y síntesis hablada (TTS). Este módulo transforma la voz en comandos interpretables y genera respuestas vocales adaptadas al contexto.

### Subfunciones:

1. **Reconocimiento automático del habla (ASR):**
   - Transcribe el audio del usuario a texto.
   - Utiliza modelos offline para preservar la privacidad y evitar latencia.
   - Eventos generados: `EVT_SPEECH_RECOGNIZED`, `EVT_COMMAND_PARSED`.

2. **Síntesis de voz (TTS):**
   - Convierte respuestas generadas por el sistema en voz natural.
   - Permite variaciones de tono y velocidad.
   - Genera salida de audio por altavoz.

3. **Gestión del turno conversacional:**
   - Detecta el final del habla (VAD) y controla los tiempos de escucha y respuesta.
   - Coordina el flujo del diálogo junto al módulo `sistema/`.

4. **Análisis de intención básica (parsing de comandos):**
   - Identifica palabras clave o patrones definidos (sin necesidad de IA compleja).
   - Extrae comandos estructurados para otros módulos.

5. **Reconocimiento emocional en la voz:**
   - Analiza tono, volumen y ritmo para inferir emociones básicas.
   - Aporta contexto emocional a las respuestas o expresividad de NORA.
   - Eventos: `EVT_EMOTION_VOICE_HAPPY`, `EVT_EMOTION_VOICE_SAD`, etc.

6. **Interrupción de respuesta (barge-in):**
   - Permite detectar si el usuario habla durante una respuesta del asistente.
   - Detiene la síntesis actual para dar prioridad al nuevo input.
   - Mejora el dinamismo y la naturalidad de la conversación.

7. **Entrenamiento adaptativo del vocabulario:**
   - Memoriza nombres propios o expresiones recurrentes del usuario.
   - Mejora la tasa de reconocimiento en futuras interacciones.
   - Opcional: integración con SQLite o almacenamiento local.

8. **Reconocimiento de palabra clave (hotword):**
   - Activa el sistema mediante frases como "NORA" o "oye NORA".
   - Funciona en segundo plano y lanza `EVT_WAKEWORD`.
   - Puede sustituir o complementar al módulo `activacion/`.



- Señal de audio del micrófono.
- Configuración local: idioma, sensibilidad, duración máxima, vocabulario clave.

### Salidas:

- Texto reconocido.
- Eventos semánticos derivados (comandos).
- Audio sintetizado para reproducción.

### Tecnologías:
- **Reconocimiento de voz (ASR):** `Vosk`, `Whisper` (offline).
- **Síntesis de voz (TTS):** `pyttsx3`, con motores TTS configurables (español).
- **VAD (Voice Activity Detection):** WebRTC VAD (`webrtcvad`) o lógica personalizada para detectar fin de frase.

### Dependencias externas:
- `vosk` o `whisper` para reconocimiento de voz offline.
- `pyttsx3` para síntesis hablada.
- `webrtcvad` o `silero-vad` para detección de actividad vocal.
- `pyaudio` o `sounddevice` para captura y reproducción de audio.
- `numpy` para procesamiento de señales de audio.
- (opcional) `espeak` o `nsss` como backends de síntesis en sistemas específicos.
- (opcional) `scipy` para análisis de silencio, energía, espectro, etc.

## 2b. `dialogo/` – Módulo de conversación natural

**Función:** Permite mantener conversaciones no estructuradas y contextuales con el usuario. Este módulo interpreta el texto reconocido por `voz/`, gestiona el contexto conversacional y genera respuestas libres.

### Subfunciones:

1. **Comprensión del lenguaje natural (NLU):**
   - Analiza el texto del usuario más allá de palabras clave.
   - Determina intención, entidades y contexto implícito.
   - Puede trabajar con parsers ligeros o modelos LLM.

2. **Gestión del contexto conversacional:**
   - Guarda la información de turnos anteriores (temas, pronombres, preferencias).
   - Permite que NORA recuerde detalles dentro de una sesión.

3. **Generación de respuestas dinámicas:**
   - Produce texto fluido y adaptado al usuario.
   - Puede usar plantillas, lógica FSM avanzada o LLM (ej. GPT vía API o DialoGPT offline).

4. **Integración emocional en la respuesta:**
   - Ajusta la respuesta según el estado emocional detectado por `voz/` o `vision/`.

### Entradas:
- Texto desde el módulo `voz/` (ASR).
- Estado emocional, contexto de usuario, eventos recientes.

### Salidas:
- Texto para TTS.
- Eventos conversacionales (`EVT_DIALOGUE_RESPONSE`, `EVT_DIALOGUE_CONFUSION`).

### Tecnologías:
- `transformers` (HuggingFace), `DialoGPT`, `Rasa`, `ChatterBot`, o llamada externa a `OpenAI GPT`.
- `SQLite` o sistema propio para persistencia contextual.

### Dependencias externas:
- `transformers`, `sentence-transformers`, `nltk`, `spacy` (según el motor elegido).
- `json` o `pickle` para mantener sesión.

## 3. `interfaz/` – Módulo de interacción y expresividad

**Función:** Gestiona todos los canales expresivos de NORA: rostro animado en pantalla, LEDs RGB y movimientos físicos con servos. Transforma los estados internos o emocionales del sistema en salidas simbólicas y sensoriales.

### Subfunciones:

1. **Gestión de pantalla facial animada:**

   - Muestra expresiones básicas (alegría, tristeza, espera, escucha...).
   - Permite transiciones animadas entre estados.
   - Genera atención visual mediante mirada o parpadeo.

2. **Control de LEDs RGB:**

   - Muestra colores según el estado interno o emoción actual.
   - Permite animaciones (pulsado, cambio gradual, ráfagas).
   - Se vincula con estados como “escuchando”, “pensando”, “procesando”.

3. **Control de servomotores:**

   - Ejecuta movimientos físicos de la cabeza o partes del rostro (mirar, asentir, inclinar).
   - Refuerza el diálogo o expresa emociones físicas.

4. **Coordinación multimodal (expresión compuesta):**

   - Sincroniza pantalla + LEDs + movimiento en respuestas complejas.
   - Permite definir “escenas expresivas” (ej: saludar, mirar a un lado, responder sonriente).

### Entradas:

- Comandos desde `sistema/` o `voz/` (estado, emoción, atención).
- Parámetros definidos por `dialogo/` o eventos visuales (gesto, presencia).

### Salidas:

- Animaciones visuales en pantalla.
- Cambios de color en LEDs.
- Movimientos físicos mediante PWM.

### Tecnologías:

- `Tkinter`, `PyQt`, `PyGame` o `Pillow` para la pantalla facial.
- Control de LEDs con `rpi_ws281x`, `neopixel`, o salidas GPIO PWM.
- Manejo de servos con `RPi.GPIO`, `pigpio`, `gpiozero`, o PWM por hardware.

### Dependencias externas:

- `rpi_ws281x` / `neopixel` para LEDs RGB direccionables.
- `RPi.GPIO` / `gpiozero` / `pigpio` para PWM y servos.
- `Pillow`, `PyGame`, `PyQt5`, `tkinter` (según la librería gráfica elegida).

##

## 4. `datos/` – Módulo de almacenamiento local

**Función:** Gestiona una base de datos local persistente donde se registran y consultan rutinas personalizadas, notas del usuario, configuraciones del sistema y eventos generados por el asistente. Permite almacenar, recuperar y actualizar información estructurada.

### Subfunciones:
1. **Gestión de rutinas:**
   - Almacena rutinas personalizadas (hora de despertar, recordatorios...).
   - Permite la modificación o eliminación por voz o GUI.

2. **Gestión de notas:**
   - Guarda notas dictadas por el usuario o creadas por comandos.
   - Recuperación por fecha o contenido parcial.

3. **Historial de eventos:**
   - Registra activaciones, emociones detectadas, diálogos y acciones del sistema.
   - Útil para auditoría o depuración.

4. **Parámetros y preferencias:**
   - Almacena configuraciones persistentes como idioma, volumen, perfil emocional o comportamiento por defecto.

### Entradas:
- Comandos desde `voz/`, `gui/` o `sistema/`.
- Datos desde `dialogo/` (por ejemplo, nueva nota o rutina).

### Salidas:
- Respuestas estructuradas (texto, fechas, configuraciones).
- Eventos como `EVT_DATA_RETRIEVED`, `EVT_NOTE_SAVED`.

### Tecnologías:
- `sqlite3` (directo o vía ORM ligero tipo `dataset` o `SQLAlchemy`).

## 5. `sistema/` – Módulo de control central

**Función:** Es el núcleo lógico de NORA. Orquesta el comportamiento global del sistema mediante una máquina de estados finita (FSM) y una gestión basada en eventos. Coordina todos los módulos, define respuestas según contexto y controla la transición entre estados operativos.

### Subfunciones:
1. **Gestión de estados globales:**
   - Controla los modos `ESPERA`, `ACTIVO`, `INTERACTIVO`, `DORMIDO`, etc.
   - Determina transiciones en función de eventos internos y externos.

2. **Gestión de eventos:**
   - Recibe y redistribuye eventos generados por sensores o módulos funcionales.
   - Desencadena acciones en `interfaz/`, `voz/`, `dialogo/`, etc.

3. **Evaluación de condiciones de activación/inhibición:**
   - Procesa eventos combinados como presencia + audio + rostro para activar interacción.
   - Inhibe respuestas si el sistema está ocupado, dormido o en modo restricción.

4. **Control de flujo de tareas:**
   - Prioriza peticiones, resuelve conflictos de concurrencia y delega control a los módulos adecuados.

### Entradas:
- Eventos del sistema (`EVT_FACE_DETECTED`, `EVT_NFC_ACTIVATE`, `EVT_IDLE_TIMEOUT`...).
- Estados de otros módulos.

### Salidas:
- Comandos a módulos (`CMD_EXPRESAR`, `CMD_RESPONDER`, `CMD_GUARDAR`).
- Transiciones de FSM (`STATE_IDLE` → `STATE_LISTENING`, etc.).

### Tecnologías:
- `transitions` (FSM), `asyncio`, `queue`, `eventbus` personalizado o `pyee`.
 `sistema/` – Módulo de control central

**Función:** Gestiona los estados internos del asistente, orquesta la lógica de activación e inactividad y coordina las decisiones generales.
**Tecnologías:** FSM central, EventManager.
**Entradas:** eventos del sistema, NFC, voz, visión.
**Salidas:** transiciones de estado, comandos a otros módulos.


## 6. `activacion/` – Módulo de activación por NFC y presencia

**Función:** Gestiona el encendido, apagado y activación del sistema NORA mediante mecanismos físicos como el módulo NFC o sensores de proximidad. Determina si el sistema debe entrar en estado activo, en espera o reposo.

### Subfunciones:

1. **Lectura de NFC:**
   - Detecta la aproximación de una tarjeta o etiqueta NFC.
   - Activa o desbloquea NORA según credencial o configuración.
   - Evento: `EVT_NFC_ACTIVATE`.

2. **Gestión de inactividad:**
   - Detecta ausencia prolongada de interacción o presencia.
   - Lanza eventos como `EVT_IDLE_TIMEOUT` o `EVT_AUTO_SLEEP`.

3. **Detección de presencia por ultrasonidos:**
   - Usa el sensor HC-SR04 para verificar si hay una persona presente.
   - Lanza eventos como `EVT_PRESENCE_CONFIRMED`, `EVT_PRESENCE_LOST`.

4. **Activación combinada con visión:**
   - Permite decisiones combinadas (NFC + rostro + presencia) para mayor robustez.
   - Permite lógica tipo: “si hay rostro y NFC, activa interfaz completa”.

### Entradas:
- Señal digital del sensor ultrasónico HC-SR04.
- Lecturas desde el lector NFC.
- Eventos desde `vision/` relacionados con detección de usuario.

### Salidas:
- Eventos de activación o reposo.
- Comandos hacia `sistema/` para cambiar estado global.

### Tecnologías:
- PN532 (vía I2C, UART o SPI).
- Sensor HC-SR04 (trigger/echo vía GPIO).
- Temporizadores y lógica combinada por software.

### Dependencias externas:
- `pn532pi`, `pynfc`, o librería equivalente para módulo NFC.
- `RPi.GPIO` o `gpiozero` para gestión del sensor ultrasónico.
- (opcional) `time`, `sched`, `threading` para gestión temporal avanzada.


## 7. `gui/` – Interfaz gráfica de usuario en ordenador

**Función:** Proporciona una interfaz visual ejecutada en el ordenador del desarrollador o usuario, permitiendo controlar manualmente el estado del sistema, observar eventos en tiempo real y probar módulos de forma asistida.

### Subfunciones:
- Panel de control: botones para activar/desactivar módulos, cambiar estados.
- Monitor de eventos: visualización de logs o eventos generados por el sistema.
- Configuración manual: edición de parámetros de entorno, emoción, volumen, etc.

### Tecnologías:
- `tkinter`, `PyQt`, `PySide`, `flask` (si se expone vía web).


## 8. `models/` – Carpeta para modelos de IA

**Función:** Almacena y organiza todos los modelos entrenados o descargados usados por el sistema (ASR, gestos, emociones, signos, etc.).

### Contenido esperado:
- Modelos de visión: YOLO, MediaPipe custom, OpenPose.
- Modelos de voz: Whisper, Vosk custom.
- Modelos de diálogo: DialoGPT, LLM fine-tuned.


## 9. `utils/` – Utilidades y funciones compartidas

**Función:** Reúne funciones auxiliares, constantes, herramientas de logging, configuración o cálculo compartidas por varios módulos.

### Ejemplos:
- Parsers de configuración.
- Cálculo de distancias, transformaciones de coordenadas.
- Generación de eventos estándar.


## 10. `tests/` – Módulos de prueba

**Función:** Contiene scripts, rutinas y test cases para probar módulos por separado antes de integrarlos.

### Subfunciones:
- Pruebas unitarias.
- Simulación de eventos.
- Validación de dispositivos hardware.


## 11. `control/` – Módulo de gestión del sistema embebido

**Función:** Supervisa y coordina el funcionamiento físico y operativo del sistema NORA. Incluye la inicialización de hardware, la supervisión de estado de los módulos y el soporte a dispositivos auxiliares como el expansor I/O. También permite tareas de administración como apagado controlado, reinicio o diagnóstico del sistema.

### Subfunciones:

1. **Inicialización del sistema:**
   - Configura GPIOs, buses y periféricos al arrancar.
   - Carga los módulos principales y estructura su ejecución.

2. **Supervisión de estado y salud:**
   - Monitoriza el estado de los módulos activos.
   - Detecta fallos y reinicia servicios si es necesario.
   - Accede a datos del sistema operativo: temperatura, CPU, RAM, conectividad.

3. **Gestión del expansor I/O (PCF8574):**
   - Asigna pines virtuales a funciones complementarias (LEDs simples, pulsadores).
   - Controla dispositivos conectados a través del expansor por I2C.

4. **Comandos administrativos:**
   - Permite apagar, reiniciar, lanzar pruebas o exportar logs desde `gui/` o CLI.
   - Define interfaces de control manual o remoto.

### Entradas:
- Señales del sistema operativo (monitor de procesos, temperatura).
- Comandos desde `gui/` o terminal.
- Configuración del sistema.

### Salidas:
- Logs estructurados o eventos del sistema.
- Señales GPIO o vía I2C (expansor).
- Comandos hacia `sistema/` o scripts externos.

### Tecnologías:
- `RPi.GPIO`, `gpiozero`, `pcf8574`, `psutil`, `os`, `subprocess`, `logging`
- Opcional: `flask` o `websocket` para control remoto desde navegador.