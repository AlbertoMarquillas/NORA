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

### Interacción con el módulo `/agentes/`:
El módulo `vision/` publica los eventos perceptivos relevantes al sistema de agentes (`/agentes/`) para su análisis y toma de decisiones descentralizada. Asimismo, puede recibir instrucciones de agentes para modificar su comportamiento, por ejemplo, activar o desactivar funciones específicas (como el análisis emocional o la detección de signos). En futuras versiones, parte de sus subfunciones podrían ser delegadas a agentes visuales especializados para optimizar recursos o adaptarse al contexto.

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

### Interacción con el módulo `/agentes/`:
El módulo `voz/` emite eventos auditivos y emocionales que pueden ser interpretados por el sistema de agentes (`/agentes/`) para inferir el estado del usuario o activar decisiones conversacionales. Asimismo, puede ser modulado por agentes expresivos que ajusten el tono de voz, ritmo o respuestas según el contexto emocional. En futuras versiones, subfunciones como el reconocimiento emocional o la gestión de interrupciones podrían delegarse a agentes especializados auditivos.

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

### Interacción con el módulo `/agentes/`:
El módulo `dialogo/` puede recibir modulaciones expresivas desde el sistema de agentes (`/agentes/`), influenciando el tono, contenido o formato de las respuestas generadas. Asimismo, puede emitir señales contextuales o semánticas útiles para agentes que gestionan la coherencia emocional o la continuidad temática de la interacción. En futuras versiones, agentes lingüísticos podrían asumir directamente la función de generación o filtrado de respuesta en situaciones específicas.


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

### Interacción con el módulo `/agentes/`:
El módulo `interfaz/` actúa como canal de salida para decisiones expresivas generadas por agentes. Puede recibir instrucciones de agentes expresivos para modular los canales visuales (pantalla, LEDs, servos) de forma coherente con el estado emocional o intencional del sistema. Además, los agentes pueden coordinar múltiples canales para generar escenas multimodales en respuesta a eventos de alto nivel.
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

5. **Seguimiento de hábitos y comportamiento:**
   - Registra métricas de uso, emociones predominantes, horarios de interacción.
   - Permite análisis de bienestar o rutinas implícitas.

6. **Almacenamiento de perfiles de usuario:**
   - Soporta múltiples usuarios identificados por NFC, rostro o voz.
   - Guarda configuraciones específicas de cada perfil.

7. **Agenda y calendario integrado:**
   - Permite añadir eventos, citas y recordatorios con fecha y hora.
   - Integración opcional con GUI o exportación `.ics`.

8. **Gestión de listas dinámicas:**
   - Maneja listas como compras, tareas o ideas.
   - Permite añadir, consultar o eliminar ítems por voz o GUI.

9. **Registros multimedia o referenciales:**
   - Permite guardar eventos asociados a una referencia de voz, tiempo o contexto visual.

10. **Anotaciones emocionales:**
   - Guarda emociones detectadas durante interacciones específicas.
   - Permite adaptar la empatía futura del sistema.

### Entradas:
- Comandos desde `voz/`, `gui/` o `sistema/`.
- Datos desde `dialogo/` (por ejemplo, nueva nota o rutina).

### Salidas:
- Respuestas estructuradas (texto, fechas, configuraciones).
- Eventos como `EVT_DATA_RETRIEVED`, `EVT_NOTE_SAVED`.

### Tecnologías:
- `sqlite3` (directo o vía ORM ligero tipo `dataset` o `SQLAlchemy`).

### Interacción con el módulo `/agentes/`:
El módulo `datos/` puede ser consultado o actualizado por agentes que gestionen rutinas, hábitos, perfiles o condiciones emocionales persistentes. Asimismo, permite a los agentes acceder a patrones históricos que modulen el comportamiento del sistema (por ejemplo, evitar recomendaciones redundantes o reforzar hábitos saludables). En futuras versiones, agentes de análisis podrán generar anotaciones inteligentes o recomendaciones contextuales directamente sobre esta base de datos.

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

5. **Gestión del estado emocional global:**
   - Integra inputs de `voz/`, `vision/` y `dialogo/` para inferir un estado emocional del sistema.
   - Ajusta el comportamiento expresivo, verbal y reactivo en función del estado actual (empático).

6. **Supervisión de consistencia intermodular:**
   - Verifica que los módulos activos correspondan al estado global.
   - Puede lanzar eventos de autocorrección o reinicio selectivo si detecta desincronización.

### Entradas:
- Eventos del sistema (`EVT_FACE_DETECTED`, `EVT_NFC_ACTIVATE`, `EVT_IDLE_TIMEOUT`...).
- Estados y señales de módulos (`interfaz/`, `voz/`, `activacion/`, `datos/`, etc.).

### Salidas:
- Comandos a módulos (`CMD_EXPRESAR`, `CMD_RESPONDER`, `CMD_GUARDAR`).
- Transiciones de FSM (`STATE_IDLE` → `STATE_LISTENING`, etc.).
- Eventos para logging o debugging (`EVT_STATE_CHANGED`, `EVT_MODULE_FAILURE`).

### Tecnologías:
- `transitions` para FSM estructurada.
- `asyncio` y `queue` para ejecución concurrente no bloqueante.
- `pyee`, `pubsub`, o `eventbus` para sistema de eventos.
- (opcional) `watchdog`, `logging`, `threading` para control y depuración adicional.

### Interacción con el módulo `/agentes/`:
El módulo `sistema/` puede recibir eventos procesados por agentes para modificar su lógica de estado, priorización o supresión de flujos. También puede delegar decisiones de activación, inhibición o empatía a agentes especializados según contexto. A su vez, emite señales relevantes al módulo `/agentes/` para informar del estado operativo global o solicitar asesoramiento contextual.

## 6. `activacion/` – Módulo de activación por múltiples entradas

**Función:** Detecta credenciales físicas vía NFC. Anteriormente gestionaba ultrasonidos, pero esta lógica ha sido delegada al módulo `sensores/`.

### Fuentes de activación disponibles:

1. **NFC PN532 (desde sensores/):**
   - Autenticación por proximidad con tarjeta o etiqueta.

2. **Presencia física (desde `sensores/`):**
   - Activación automática al detectar un usuario cerca mediante HC-SR04.

3. **Atención visual (desde `vision/`):**
   - Activación si el usuario mantiene la mirada hacia NORA.

4. **Hotword (desde `voz/`):**
   - Frase como “oye NORA” activa el sistema.

5. **Botón físico (GPIO):**
   - Pulsador accesible en el chasis para activación manual.

6. **Bluetooth (desde `sensores/`):**
   - Activación al reconocer dispositivos cercanos emparejados.

### Función extendida:
- Este módulo escucha eventos de activación generados por otros módulos (`sensores/`, `vision/`, `voz/`) y determina si el sistema debe pasar a estado activo o interactivo. También aplica lógica combinada para evitar falsos positivos.

### Entradas:
- Eventos desde `sensores/` (`EVT_PRESENCE_CONFIRMED`, `EVT_NFC_UID_DETECTED`, `EVT_BLUETOOTH_DETECTED`).
- Eventos desde `vision/` (`EVT_ATTENTION_GAINED`).
- Eventos desde `voz/` (`EVT_WAKEWORD`).
- Señal digital de botón físico (opcional).

### Salidas:
- Eventos de activación o reposo.
- Comandos hacia `sistema/` para cambiar estado global.

### Tecnologías:
- Eventos gestionados mediante `eventbus` o `pyee`.
- Evaluación combinada de condiciones.
- Integración de entrada discreta (botón físico) mediante `gpiozero` o `RPi.GPIO`.

### Dependencias externas:
- Ninguna directa para lectura de hardware; depende de `sensores/` para datos físicos.
- Utilidades de eventos y lógica combinatoria.

### Interacción con el módulo `/agentes/`:
El módulo `activacion/` puede delegar la decisión final de activación al sistema de agentes, permitiendo aplicar lógicas contextuales más complejas y dinámicas. Los agentes pueden combinar múltiples fuentes sensoriales y estados históricos para decidir si activar o inhibir el sistema. Asimismo, el módulo puede emitir señales hacia `/agentes/` para ser consideradas en la evaluación general del entorno o del usuario.

## 7. `gui/` – Interfaz gráfica de usuario en ordenador

**Función:** Proporciona una interfaz visual ejecutada en el ordenador del desarrollador o usuario, permitiendo controlar manualmente el estado del sistema, observar eventos en tiempo real y probar módulos de forma asistida.

### Subfunciones:

1. **Panel de control:**
   - Botones para activar/desactivar módulos, cambiar entre estados del sistema.
   - Control manual de LEDs, expresiones, servos, volumen y emociones.

2. **Monitor de eventos:**
   - Visualización cronológica de eventos generados por módulos.
   - Filtros por tipo de evento, módulo de origen o severidad.
   - Registro exportable para depuración o análisis.

3. **Configuración manual:**
   - Edición directa de parámetros como idioma, perfil de usuario, tiempos de espera, sensibilidad.
   - Interfaz editable para las preferencias persistidas en `datos/`.

4. **Monitoreo de salud del sistema:**
   - Lectura de temperatura de CPU, carga, RAM, uptime, red.
   - Visualización gráfica o semáforos de estado.
   - Alerta de condiciones críticas.

5. **Panel de intervenciones técnicas:**
   - Posibilidad de reiniciar módulos individualmente.
   - Acceso a logs y eventos en tiempo real.
   - Control de pines GPIO en tiempo real.

6. **Lanzador de pruebas y diagnósticos:**
   - Ejecución de test unitarios o de integración desde `tests/`.
   - Visualización del resultado en GUI.

7. **Modo demostración / entrenamiento:**
   - Permite simular interacciones para presentaciones o desarrollo.
   - Controlar respuestas desde `dialogo/` o entrada de texto directa.

### Tecnologías:
- `tkinter`, `PyQt`, `PySide` para entorno de escritorio.
- `flask`, `dash`, `streamlit` si se desea exponer como servicio web local o remoto.
- `matplotlib` o `plotly` (opcional) para gráficas de uso o estado.

### Interacción con el módulo `/agentes/`:
El módulo `gui/` puede mostrar el estado interno y decisiones de los agentes activos, permitiendo visualizar cómo sus inferencias afectan al comportamiento global. También puede permitir la activación/desactivación manual de agentes o modificación de parámetros dinámicos, facilitando la experimentación y depuración en entornos de desarrollo o demostración.

## 8. `models/` – Carpeta para modelos de IA

**Función:** Almacena y organiza todos los modelos entrenados o descargados usados por el sistema (ASR, gestos, emociones, signos, etc.).

### 1. Contenido esperado

1. **Modelos de visión:**
   - Detección de objetos (YOLOv5, YOLOv8).
   - Estimación de pose y gestos (MediaPipe custom, OpenPose).
   - Clasificación de emociones faciales.

2. **Modelos de voz:**
   - Reconocimiento automático del habla (ASR) personalizado con `Whisper` o `Vosk` adaptado.
   - Análisis emocional a partir del tono de voz (redes LSTM o CNN sobre MFCCs).

3. **Modelos de diálogo:**
   - Generación de respuestas con `DialoGPT`, `GPT-2`/`GPT-3` fine-tuned o modelos propios.
   - Clasificadores de intención o extractores de entidades entrenados.

4. **Modelos de signos o lenguaje gestual:**
   - Reconocimiento de gestos estáticos o dinámicos en LSE/ASL.
   - Modelos basados en pose keypoints o CNN-RNN.

5. **Modelos personalizados y adaptativos:**
   - Modelos entrenados con los datos del usuario para adaptación progresiva.
   - Recomendaciones, hábitos, preferencias y predicciones personalizadas.

### 2. Estructura recomendada

- `/models/vision/` – Modelos relacionados con percepción visual: detección de objetos, reconocimiento facial, emociones visuales, gestos y postura corporal.
- `/models/voice/` – Modelos enfocados en procesamiento de audio: reconocimiento de voz (ASR), emociones vocales, segmentación por voz.
- `/models/dialogue/` – Modelos para generación de lenguaje, clasificación de intención, extracción de entidades y gestión del diálogo.
- `/models/sign/` – Modelos dedicados a la interpretación de lenguaje de signos o gestos simbólicos, tanto estáticos como dinámicos.
- `/models/user/` – Modelos entrenados con datos del usuario: comportamiento, preferencias, estilo comunicativo, sensibilidad a emociones.
- `/models/behavior/` – Modelos para análisis temporal de hábitos, rutinas implícitas, evaluación de constancia o anomalías.
- `/models/recommend/` – Modelos de recomendación contextual: sugerencias personalizadas basadas en patrones de uso e historial.
- `/models/shared/` – Componentes comunes a varios modelos: embeddings, tokenizers, normalizadores, funciones auxiliares.

### Interacción con el módulo `/agentes/`:
El sistema de agentes puede acceder dinámicamente a los modelos contenidos en esta carpeta para ejecutar inferencias específicas según el contexto. Cada agente puede estar asociado a uno o varios modelos (por ejemplo, un agente emocional con una red CNN sobre MFCCs, o un agente de atención visual con un modelo de estimación de mirada). Esta carpeta debe estar estructurada de forma coherente para facilitar la carga modular y el uso selectivo por parte de los agentes activos.

## 9. `utils/` – Utilidades y funciones compartidas

**Función:** Reúne funciones auxiliares, constantes, herramientas de logging, configuración o cálculo compartidas por varios módulos del sistema.

### Ejemplos de contenido:

1. **Parsers de configuración:**
   - Lectura y validación de archivos `.json`, `.yaml` o `.ini`.
   - Conversión de parámetros de entorno a estructuras internas.

2. **Funciones matemáticas y geométricas:**
   - Cálculo de distancias, ángulos, centroide, normalización de vectores.
   - Transformaciones entre coordenadas de imagen y físicas.

3. **Generación y gestión de eventos estándar:**
   - Funciones para emitir eventos internos (`emit_event()`), con estructura uniforme.
   - Enrutamiento básico o logging de eventos generados.

4. **Gestión de tiempo y temporizadores:**
   - Funciones de medición (`tic-toc`), espera cooperativa o temporización de fases.

5. **Logger global del sistema:**
   - Inicialización de `logging` estructurado.
   - Niveles configurables por módulo: `DEBUG`, `INFO`, `ERROR`, etc.

6. **Conversión y formateo:**
   - Adaptación de unidades, formatos de fecha/hora, traducción de cadenas, codificación segura.

7. **Utilidades de validación y comprobación:**
   - Comprobaciones de integridad, existencia de archivos, sanitización de entradas.

### Interacción con el módulo `/agentes/`:
El módulo `utils/` ofrece herramientas de soporte para el desarrollo y ejecución de agentes. Las funciones matemáticas, de gestión de eventos o de temporización pueden ser utilizadas directamente por agentes especializados en visión, voz o comportamiento. Además, proporciona parsers y validadores comunes que aseguran coherencia en la interpretación de configuraciones y parámetros dinámicos que los agentes puedan cargar o modificar.
## 10. `tests/` – Módulos de prueba

**Función:** Contiene scripts, rutinas y test cases destinados a verificar el comportamiento de los diferentes módulos del sistema NORA, tanto de forma aislada como en condiciones simuladas, antes de su integración completa.

### Subfunciones:

1. **Pruebas unitarias:**
   - Verificación de funciones individuales dentro de cada módulo (`utils`, `datos`, `voz`, etc.).
   - Uso de frameworks como `unittest`, `pytest` o `doctest`.

2. **Simulación de eventos:**
   - Generación artificial de eventos del sistema (`EVT_NFC_ACTIVATE`, `EVT_SPEECH_RECOGNIZED`, etc.).
   - Permite probar flujos sin necesidad de hardware conectado.

3. **Validación de dispositivos hardware:**
   - Comprobación de conectividad, respuesta y estabilidad de sensores, actuadores, interfaces (NFC, cámara, servos...).
   - Scripts interactivos para pruebas desde terminal o GUI.

4. **Pruebas de integración parcial:**
   - Validación de la interacción entre pares de módulos (por ejemplo, `voz` + `dialogo`, `vision` + `sistema`).
   - Ejecución controlada de flujos de eventos.

5. **Análisis de cobertura y regresión:**
   - Evaluación de qué partes del código están cubiertas por los tests.
   - Detección de errores introducidos tras modificaciones recientes.

6. **Benchmarking y estrés:**
   - Medición de tiempos de respuesta, rendimiento de inferencias, carga de CPU.
   - Pruebas en condiciones límite o prolongadas.

### Interacción con el módulo `/agentes/`:
El módulo `tests/` incluye pruebas específicas para validar el comportamiento y las decisiones de los agentes activos. Estas pruebas pueden cubrir inferencias realizadas por modelos asociados, condiciones contextuales evaluadas por los agentes, o el impacto de sus decisiones sobre los estados del sistema. Además, permite simular entornos dinámicos donde los agentes deben adaptarse, facilitando la validación de lógica adaptativa, priorización y modulación emocional.

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

5. **Gestión de energía y consumo:**
   - Controla el encendido/apagado selectivo de periféricos.
   - Soporta perfiles de bajo consumo para modo reposo o portátil.

6. **Gestión de logs estructurados:**
   - Registro automático por módulo y tipo de evento.
   - Rollover y exportación segura de archivos de log.

7. **Diagnóstico de arranque (autotest):**
   - Autoevaluación al encender: cámara, servos, NFC, sensores.
   - Emisión de eventos `EVT_SELFTEST_PASS`, `EVT_SELFTEST_FAIL`.

8. **Interfaz remota de administración:**
   - Servidor embebido para control remoto con navegador.
   - Acciones remotas de mantenimiento o estado del sistema.

9. **Protección frente a fallos físicos:**
   - Reinicio automático mediante watchdog interno.
   - Monitor de sobretemperatura con apagado de emergencia.

10. **Sincronización horaria:**
   - Inicialización del reloj del sistema (NTP o RTC externo).
   - Garantiza consistencia temporal en eventos y logs.

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

### Interacción con el módulo `/agentes/`:
El módulo `control/` puede servir como fuente de datos para agentes supervisores, proporcionando métricas de salud del sistema, logs o condiciones ambientales. A su vez, puede ejecutar acciones recomendadas por estos agentes, como apagado controlado ante sobretemperatura o reinicio selectivo de módulos. También facilita la auditoría de decisiones automatizadas registradas por los agentes en condiciones críticas.

## 12. `sensores/` – Módulo de adquisición y procesamiento ambiental

**Función:** Lectura y procesamiento de sensores físicos conectados a NORA. Publica eventos como temperatura, luz, humedad, calidad del aire y presencia.

### Subfunciones:

1. **Lectura periódica de sensores:**

   - DHT22/BME280 (temperatura y humedad)
   - TSL2561 (luminosidad)
   - MQ135/CCS811 (calidad del aire)
   - DS3231 (hora)
   - HC-SR04 (presencia física)

2. **Lectura de NFC (PN532):**

   - Detecta y decodifica tarjetas o etiquetas NFC.
   - Emite eventos como `EVT_NFC_UID_DETECTED` con el identificador de la etiqueta.
   - Permite reutilización de la lectura por múltiples módulos (activación, perfiles, registros).

3. **Conversión y validación:**

   - Conversión de unidades físicas, validación de rango

4. **Generación de eventos:**

   - Eventos como `EVT_ENV_HOT`, `EVT_DARK_ENV`, `EVT_PRESENCE_CONFIRMED`, `EVT_NFC_UID_DETECTED`

5. **Gestión de sensores BLE e I2C:**

   - Comunicación con periféricos inalámbricos o por bus digital

6. **Publicación de eventos y logging:**

   - Comunicación con `sistema/` y persistencia en `datos/`\*\*
   - DHT22/BME280 (temperatura y humedad)
   - TSL2561 (luminosidad)
   - MQ135/CCS811 (calidad del aire)
   - DS3231 (hora)
   - HC-SR04 (presencia física)

7. **Conversión y validación:**

   - Conversión de unidades físicas, validación de rango

8. **Generación de eventos:**

   - Eventos como `EVT_ENV_HOT`, `EVT_DARK_ENV`, `EVT_PRESENCE_CONFIRMED`

9. **Gestión de sensores BLE e I2C:**

   - Comunicación con periféricos inalámbricos o por bus digital

10. **Publicación de eventos y logging:**

    - Comunicación con `sistema/` y persistencia en `datos/`

### Tecnologías:

- `adafruit_dht`, `smbus2`, `gpiozero`, `bleak`, `datetime`, `json`, `paho-mqtt`

## 13. `agentes/` – Módulo de coordinación perceptiva y expresiva

**Función:**\
El módulo `agentes/` implementa una capa intermedia de coordinación inteligente entre los módulos sensoriales (`vision/`, `voz/`, `sensores/`, etc.) y los módulos actuadores (`interfaz/`, `sistema/`, `datos/`, etc.). Cada "agente" representa una entidad lógica especializada en procesar un tipo de información o supervisar un dominio funcional (visual, auditivo, emocional...), actuando como filtro, modulador o generador de decisiones autónomas.

Este módulo permite desacoplar la lógica central del sistema de las decisiones contextuales, facilitando adaptabilidad, personalización y extensibilidad mediante agentes dedicados.

### Subfunciones:

1. **Agentes perceptivos:**

   - Reciben eventos desde módulos sensoriales.
   - Evalúan condiciones contextuales o temporales (presencia continua, atención sostenida, tono emocional persistente...).
   - Generan nuevos eventos interpretados, por ejemplo: `AGT_ATTENTION_CONFIRMED`, `AGT_ENVIRONMENT_ALERT`.

2. **Agentes expresivos:**

   - Modulan la respuesta emocional y simbólica del sistema (colores, expresiones faciales, tono de voz) según el estado interno y contexto externo.
   - Determinan qué canales expresivos deben activarse y cómo sincronizarse.

3. **Agentes de activación y contexto:**

   - Deciden si el sistema debe cambiar de estado en función de múltiples entradas (voz, NFC, atención, sensor ultrasónico).
   - Evitan falsos positivos combinando datos multisensoriales.

4. **Agentes especializados delegados:**

   - Agentes dedicados a funciones concretas como: análisis emocional, interpretación de signos, clasificación de intención.
   - Permiten activar/desactivar capacidades según el contexto o el perfil del usuario.

5. **Gestión de prioridades y supresión:**

   - Permiten decidir qué eventos tienen precedencia y cuáles deben suprimirse temporalmente.
   - Ejemplo: suprimir detección de atención si se ha activado el modo descanso.

### Entradas:

- Eventos desde módulos perceptivos (`vision/`, `voz/`, `sensores/`).
- Estado global del sistema (`sistema/`).
- Configuraciones dinámicas del usuario (perfil, horario, modo activo/inactivo).

### Salidas:

- Eventos derivados para otros módulos (`sistema/`, `interfaz/`, `voz/`, `dialogo/`).
- Activación de escenas expresivas combinadas.
- Señales de modulación emocional o priorización (`CMD_SUPRIMIR_EVENTO`, `CMD_PRIORIDAD_ALTA`).

### Tecnologías:

- Sistema de eventos basado en `pyee`, `eventbus` o `asyncio.Queue`.
- Implementación flexible basada en clases `AgenteBase`, con posibilidad de extender por herencia (`AgenteVisual`, `AgenteAuditivo`, etc.).
- Evaluación de condiciones mediante reglas (tipo `if-this-then-that`) o lógica FSM por agente.

### Dependencias externas:

- No requiere librerías específicas fuera del sistema de eventos.
- Compatible con lógica FSM (`transitions`) o reglas condicionales.
- Puede integrarse con módulos de IA ligeros para toma de decisiones basadas en aprendizaje.

...

