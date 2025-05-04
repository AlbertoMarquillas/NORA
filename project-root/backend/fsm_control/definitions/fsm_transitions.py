from fsm_control.definitions.fsm_definitions import FSMState, FSMEvent

"""
Tabla de transiciones de estado del sistema NORA.
Este diccionario representa las reglas de evolución de la máquina de estados finita (FSM).
Cada clave es una tupla (estado_origen, evento), y el valor asociado indica el estado destino
al que se debe transitar cuando dicho evento se produce en ese estado de origen.
Estas transiciones deben interpretarse como atómicas y gobernadas por las reglas de prioridad
descritas en el documento `fsm_prioridades.md`.
"""

FSM_TRANSITIONS = {
    # --- Transiciones desde el estado REPOSO ---
    # Activación mediante credencial NFC válida.
    (FSMState.REPOSO, FSMEvent.EVT_NFC_ACTIVATE): FSMState.ACTIVADO,
    # Activación automática por detección de presencia cercana.
    (FSMState.REPOSO, FSMEvent.EVT_PRESENCE_CONFIRMED): FSMState.ACTIVADO,
    # Activación por contacto visual mantenido.
    (FSMState.REPOSO, FSMEvent.EVT_ATTENTION_GAINED): FSMState.ACTIVADO,
    # Entrada directa por voz mediante hotword.
    (FSMState.REPOSO, FSMEvent.EVT_WAKEWORD): FSMState.ESCUCHA,
    # Activación por evento programado en agenda.
    (FSMState.REPOSO, FSMEvent.EVT_SCHEDULE_TRIGGERED): FSMState.ACTIVADO,

    # --- Transiciones desde el estado ACTIVADO ---
    # Inicio de interacción verbal detectado.
    (FSMState.ACTIVADO, FSMEvent.EVT_SPEECH_START): FSMState.ESCUCHA,
    # Confirmación visual de atención centrada en el usuario.
    (FSMState.ACTIVADO, FSMEvent.EVT_ATTENTION_CONFIRMED): FSMState.ATENCION,
    # Paso a reposo por inactividad prolongada.
    (FSMState.ACTIVADO, FSMEvent.EVT_IDLE_TIMEOUT): FSMState.REPOSO,
    # Paso a error por fallo técnico detectado en algún módulo.
    (FSMState.ACTIVADO, FSMEvent.EVT_MODULE_FAILURE): FSMState.ERROR,

    # --- Transiciones desde el estado ESCUCHA ---
    # Reconocimiento de comando de voz válido.
    (FSMState.ESCUCHA, FSMEvent.EVT_SPEECH_RECOGNIZED): FSMState.PROCESANDO,
    # Timeout por ausencia de entrada verbal.
    (FSMState.ESCUCHA, FSMEvent.EVT_LISTEN_TIMEOUT): FSMState.ACTIVADO,
    # Falla del micrófono o canal de audio.
    (FSMState.ESCUCHA, FSMEvent.EVT_MIC_FAILURE): FSMState.ERROR,

    # --- Transiciones desde el estado ATENCION ---
    # Usuario inicia expresión verbal mientras mantiene atención visual.
    (FSMState.ATENCION, FSMEvent.EVT_SPEECH_START): FSMState.ESCUCHA,
    # Reconocimiento de gesto interpretado como comando.
    (FSMState.ATENCION, FSMEvent.EVT_GESTURE_COMMAND): FSMState.PROCESANDO,
    # Se pierde el foco de atención visual.
    (FSMState.ATENCION, FSMEvent.EVT_ATTENTION_LOST): FSMState.ACTIVADO,

    # --- Transiciones desde el estado PROCESANDO ---
    # Respuesta completada correctamente.
    (FSMState.PROCESANDO, FSMEvent.EVT_PROCESS_COMPLETED): FSMState.ACTIVADO,
    # Fallo en el análisis o en la generación de respuesta.
    (FSMState.PROCESANDO, FSMEvent.EVT_PROCESS_FAILURE): FSMState.ERROR,

    # --- Transiciones desde el estado ERROR ---
    # Recuperación automática exitosa tras fallo.
    (FSMState.ERROR, FSMEvent.EVT_RECOVERY_SUCCESS): FSMState.ACTIVADO,
    # Timeout de espera de recuperación técnica.
    (FSMState.ERROR, FSMEvent.T_ERROR_RECOVERY_TIMEOUT): FSMState.ACTIVADO,
    # Reanudación forzada de interacción por el usuario.
    (FSMState.ERROR, FSMEvent.CMD_FORCE_RESUME): FSMState.ESCUCHA,
}
