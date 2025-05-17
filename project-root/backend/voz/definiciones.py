"""
definiciones.py

Archivo centralizado de configuración y frases clave para el sistema de voz de NORA.
Contiene los parámetros ajustables para entrada de voz, salida hablada, activadores FSM y configuración futura.
"""

# ─────────────────────────────────────────────────────────────
# 🎙️ Configuración de entrada de voz (micrófono)
# ─────────────────────────────────────────────────────────────

# Índice del micrófono (obtenido con sr.Microphone.list_microphone_names())
DEVICE_INDEX = 1

# Umbral mínimo de energía para considerar que alguien está hablando
ENERGY_THRESHOLD = 100

# Tiempo de silencio para considerar que la frase ha terminado (en segundos)
PAUSE_THRESHOLD = 0.8

# Tiempo máximo permitido por frase hablada
PHRASE_TIME_LIMIT = 10

# Tiempo máximo de espera sin captar voz antes de cancelar escucha
TIMEOUT = 3


# ─────────────────────────────────────────────────────────────
# 🗣️ Configuración de salida de voz (TTS)
# ─────────────────────────────────────────────────────────────

# Velocidad del habla
TTS_RATE = 150  # 100-200 es natural

# Volumen (de 0.0 a 1.0)
TTS_VOLUME = 1.0

# Voz por defecto: None = sistema
# En sistemas compatibles se puede especificar: 'spanish-latin-am', 'es', etc.
TTS_VOICE = None


# ─────────────────────────────────────────────────────────────
# 🚩 Frases clave predefinidas
# ─────────────────────────────────────────────────────────────

FRASES_ACTIVACION = [
    "hola nora",
    "oye nora",
    "nora estás ahí",
    "despierta nora",
    "nora activa"
]

FRASES_DESACTIVACION = [
    "nora apágate",
    "nora cierra",
    "nora silencio",
    "nora no hables más",
    "nora cállate",
    "adiós nora",
    "nora vete",
    "apagate nora",
    "nora vete a dormir"
]

FRASES_REPETICION = [
    "repite eso",
    "qué has dicho",
    "vuelve a decirlo"
]

FRASES_AYUDA = [
    "necesito ayuda",
    "no sé qué hacer",
    "explícame esto"
]


# ─────────────────────────────────────────────────────────────
# ⚙️ Definiciones de eventos FSM (valores usados por emisor_eventos.py)
# ─────────────────────────────────────────────────────────────
# URL del endpoint del backend que recibe eventos FSM
URL_EVENTO_FSM = "http://localhost:8000/api/evento/"

EVENTO_ACTIVACION = "EVT_WAKEWORD"
EVENTO_DESACTIVACION = "EVT_SHUTDOWN"
EVENTO_REPETICION = "EVT_REPETIR"
EVENTO_AYUDA = "EVT_PEDIR_AYUDA"  # puedes definirlo en tu FSM si no existe aún


# ─────────────────────────────────────────────────────────────
# 🧪 Configuración futura (modo debug, LLM, etc.)
# ─────────────────────────────────────────────────────────────

DEBUG_VOZ = True  # imprime información en consola
LLM_ACTIVO = False  # si es True, todo texto no reconocido se pasa al LLM
