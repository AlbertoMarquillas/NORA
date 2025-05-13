from enum import Enum, auto

class FSMState(Enum):
    """
    Enumeración de estados operativos del sistema NORA.

    Cada estado representa una fase distintiva en el ciclo de vida del asistente físico,
    reflejando tanto su disponibilidad funcional como su foco de atención o actividad principal.
    Estos estados son mutuamente excluyentes y se gestionan de forma determinista mediante la FSM.
    """
    INACTIVO = auto()
    ACTIVO = auto()
    ESCUCHANDO = auto()
    PROCESANDO = auto()
    RESPONDIENDO = auto()
    ERROR = auto()
    DURMIENDO = auto()


class FSMEvent(Enum):
    """
    Enumeración de eventos que pueden provocar transiciones entre estados en la FSM de NORA.

    Los eventos representan estímulos externos (sensores, voz, gestos, comandos),
    internos (errores, timeouts), o instrucciones directas de los agentes del sistema.
    Cada evento está documentado en `eventos.md` y posee una prioridad relativa definida.
    """
    # --- Eventos de activación ---
    EVT_NFC_ACTIVATE = auto()         # Activación mediante identificación NFC válida.
    EVT_WAKEWORD = auto()             # Activación por palabra clave detectada (hotword).
    EVT_PRESENCE_CONFIRMED = auto()   # Activación por presencia física confirmada.
    EVT_ATTENTION_GAINED = auto()     # Activación por atención visual sostenida.
    EVT_SCHEDULE_TRIGGERED = auto()   # Activación por evento programado en agenda.

    # --- Eventos de interacción ---
    EVT_SPEECH_START = auto()         # Inicio de entrada de voz detectado.
    EVT_ATTENTION_CONFIRMED = auto()  # Atención visual mantenida confirmada.
    EVT_SPEECH_RECOGNIZED = auto()    # Entrada verbal válida reconocida.
    EVT_GESTURE_COMMAND = auto()      # Comando gestual interpretado correctamente.

    # --- Eventos de suspensión o abandono ---
    EVT_IDLE_TIMEOUT = auto()         # Tiempo de inactividad excedido.
    EVT_ATTENTION_LOST = auto()       # Atención visual perdida.

    # --- Eventos de expiración interna ---
    EVT_LISTEN_TIMEOUT = auto()       # Expiración por falta de voz durante ESCUCHA
    
    # --- Eventos de error ---
    EVT_MODULE_FAILURE = auto()       # Falla técnica en módulo crítico.
    EVT_MIC_FAILURE = auto()          # Falla del canal de audio o micrófono.
    EVT_PROCESS_FAILURE = auto()      # Error en el procesamiento de entrada o decisión.

    # --- Eventos de finalización o resolución ---
    EVT_PROCESS_COMPLETED = auto()    # Proceso de respuesta completado con éxito.
    EVT_RECOVERY_SUCCESS = auto()     # Recuperación automática tras error.
    T_ERROR_RECOVERY_TIMEOUT = auto() # Tiempo de espera de recuperación finalizado.

    # --- Comandos explícitos del sistema ---
    CMD_FORCE_RESUME = auto()         # Reanudación forzada de interacción.
    CMD_INHIBIR_ACTIVACION = auto()   # Inhibición de cualquier activación externa.
    CMD_INHIBIR_ESCUCHA = auto()      # Inhibición de la entrada verbal.
    CMD_CANCEL_LISTENING = auto()     # Cancelación inmediata del estado de escucha.
    
    # --- Eventos de desactivación ---
    EVT_SHUTDOWN = auto()             # Desactivación del sistema por comando o evento.
    EVT_NFC_DEACTIVATE = auto()       # Desactivación por NFC no válido.
    EVT_PRESENCE_LOST = auto()        # Desactivación por ausencia física.
    EVT_ATTENTION_LOST = auto()       # Desactivación por pérdida de atención visual. 
