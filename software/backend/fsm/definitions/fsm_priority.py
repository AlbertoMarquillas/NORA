"""
fsm_priority.py

Este módulo define la jerarquía de prioridades entre eventos del sistema NORA,
según el esquema establecido en `fsm_prioridades.md`.

Las prioridades determinan el orden de evaluación de eventos en condiciones
de simultaneidad o competencia, garantizando un comportamiento determinista
de la FSM.
"""

from fsm.definitions.fsm_definitions import FSMEvent

# Diccionario que asigna un nivel de prioridad a cada evento.
# Cuanto menor el número, mayor la prioridad.
FSM_EVENT_PRIORITY = {
    # Nivel 1 – Fallos críticos
    FSMEvent.EVT_MODULE_FAILURE: 1,
    FSMEvent.EVT_PROCESS_FAILURE: 1,

    # Nivel 2 – Entrada válida reconocida
    FSMEvent.EVT_SPEECH_RECOGNIZED: 2,
    FSMEvent.EVT_GESTURE_COMMAND: 2,

    # Nivel 3 – Inicio de intención
    FSMEvent.EVT_SPEECH_START: 3,
    FSMEvent.EVT_ATTENTION_CONFIRMED: 3,

    # Nivel 4 – Activadores externos
    FSMEvent.EVT_NFC_ACTIVATE: 4,
    FSMEvent.EVT_WAKEWORD: 4,

    # Nivel 5 – Indicadores de inactividad
    FSMEvent.EVT_IDLE_TIMEOUT: 5,
    FSMEvent.EVT_ATTENTION_LOST: 5,

    # Nivel 6 – Expiración interna
    FSMEvent.EVT_LISTEN_TIMEOUT: 6,
    FSMEvent.T_ERROR_RECOVERY_TIMEOUT: 6,

    # Nivel 7 – Activaciones programadas
    FSMEvent.EVT_SCHEDULE_TRIGGERED: 7,
}

# Prioridad por defecto (baja) para eventos no contemplados.
DEFAULT_EVENT_PRIORITY = 99
