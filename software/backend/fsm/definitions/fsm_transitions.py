from fsm.definitions.fsm_definitions import FSMState, FSMEvent

"""
Tabla de transiciones de estado del sistema NORA.
Este diccionario representa las reglas de evolución de la máquina de estados finita (FSM).
Cada clave es una tupla (estado_origen, evento), y el valor asociado indica el estado destino
al que se debe transitar cuando dicho evento se produce en ese estado de origen.
Estas transiciones deben interpretarse como atómicas y gobernadas por las reglas de prioridad
descritas en el documento `fsm_prioridades.md`.
"""

FSM_TRANSITIONS = {
    # --- Transiciones desde el estado INACTIVO ---
    (FSMState.INACTIVO, FSMEvent.EVT_NFC_ACTIVATE): FSMState.ACTIVO,
    (FSMState.INACTIVO, FSMEvent.EVT_PRESENCE_CONFIRMED): FSMState.ACTIVO,
    (FSMState.INACTIVO, FSMEvent.EVT_WAKEWORD): FSMState.ACTIVO,

    # --- Transiciones desde el estado ACTIVO ---
    (FSMState.ACTIVO, FSMEvent.EVT_SPEECH_START): FSMState.ESCUCHANDO,
    (FSMState.ACTIVO, FSMEvent.EVT_GESTURE_COMMAND): FSMState.PROCESANDO,
    (FSMState.ACTIVO, FSMEvent.CMD_INHIBIR_ACTIVACION): FSMState.DURMIENDO,
    (FSMState.ACTIVO, FSMEvent.EVT_IDLE_TIMEOUT): FSMState.INACTIVO,

    # --- Transiciones desde el estado ESCUCHANDO ---
    (FSMState.ESCUCHANDO, FSMEvent.EVT_SPEECH_RECOGNIZED): FSMState.PROCESANDO,
    (FSMState.ESCUCHANDO, FSMEvent.EVT_LISTEN_TIMEOUT): FSMState.INACTIVO,
    (FSMState.ESCUCHANDO, FSMEvent.CMD_CANCEL_LISTENING): FSMState.INACTIVO,

    # --- Transiciones desde el estado PROCESANDO ---
    (FSMState.PROCESANDO, FSMEvent.EVT_PROCESS_COMPLETED): FSMState.RESPONDIENDO,
    (FSMState.PROCESANDO, FSMEvent.EVT_PROCESS_FAILURE): FSMState.DURMIENDO,

    # --- Transiciones desde el estado RESPONDIENDO ---
    (FSMState.RESPONDIENDO, FSMEvent.EVT_RECOVERY_SUCCESS): FSMState.INACTIVO,
    (FSMState.RESPONDIENDO, FSMEvent.CMD_FORCE_RESUME): FSMState.ACTIVO,

    # --- Transiciones desde el estado ERROR ---
    (FSMState.ERROR, FSMEvent.T_ERROR_RECOVERY_TIMEOUT): FSMState.INACTIVO,

    # --- Transiciones desde el estado DURMIENDO ---
    (FSMState.DURMIENDO, FSMEvent.CMD_FORCE_RESUME): FSMState.ACTIVO,
}
