"""
fsm_priority.py

Jerarquía de prioridades de eventos de la FSM de NORA.

Un valor menor indica mayor prioridad de procesamiento.

Notes
-----
La prioridad define el orden de atención cuando varios eventos compiten
en la cola. No sustituye a las transiciones, guardias o condiciones, pero
sí determina qué evento se evalúa antes.

Criterio general de prioridad
-----------------------------
1. Fallos críticos, apagado y cancelaciones duras.
2. Comandos explícitos de control del sistema.
3. Eventos de recuperación.
4. Resultados ya interpretados o listos para ejecutar.
5. Captura de entrada del usuario.
6. Timeouts y pérdida de contexto.
7. Activaciones externas.
8. Triggers programados o de menor urgencia.
"""

from .fsm_definitions import FSMEvent


FSM_EVENT_PRIORITY = {
    # =========================================================
    # NIVEL 1 — CRÍTICOS / APAGADO / FALLOS DUROS
    # =========================================================
    FSMEvent.EVT_SHUTDOWN: 1,
    FSMEvent.EVT_MODULE_FAILURE: 1,
    FSMEvent.EVT_MIC_FAILURE: 1,
    FSMEvent.EVT_CAMERA_FAILURE: 1,
    FSMEvent.EVT_PROCESS_FAILURE: 1,
    FSMEvent.EVT_ACTION_FAILED: 1,

    # =========================================================
    # NIVEL 2 — COMANDOS EXPLÍCITOS DE CONTROL
    # =========================================================
    FSMEvent.CMD_SUSPEND: 2,
    FSMEvent.CMD_WAKE: 2,
    FSMEvent.CMD_FORCE_RESUME: 2,
    FSMEvent.CMD_CANCEL_ACTION: 2,
    FSMEvent.CMD_CANCEL_LISTENING: 2,
    FSMEvent.CMD_INHIBIR_ACTIVACION: 2,
    FSMEvent.CMD_INHIBIR_ESCUCHA: 2,

    # =========================================================
    # NIVEL 3 — RECUPERACIÓN Y CONTROL DE ERROR
    # =========================================================
    FSMEvent.EVT_RECOVERY_STARTED: 3,
    FSMEvent.EVT_RECOVERY_SUCCESS: 3,
    FSMEvent.EVT_ERROR_RECOVERY_TIMEOUT: 3,

    # =========================================================
    # NIVEL 4 — RESULTADOS YA INTERPRETADOS / DECISIONES FUERTES
    # =========================================================
    FSMEvent.EVT_CONFIRMATION_RECEIVED: 4,
    FSMEvent.EVT_CONFIRMATION_REJECTED: 4,
    FSMEvent.EVT_PLAN_READY: 4,
    FSMEvent.EVT_INPUT_INTERPRETED: 4,
    FSMEvent.EVT_GESTURE_COMMAND: 4,
    FSMEvent.EVT_SPEECH_RECOGNIZED: 4,

    # =========================================================
    # NIVEL 5 — EJECUCIÓN Y FINALIZACIÓN DE ACCIONES
    # =========================================================
    FSMEvent.EVT_ACTION_STARTED: 5,
    FSMEvent.EVT_ACTION_COMPLETED: 5,
    FSMEvent.EVT_SPEECH_OUTPUT_STARTED: 5,
    FSMEvent.EVT_SPEECH_OUTPUT_FINISHED: 5,
    FSMEvent.EVT_CAPTURE_COMPLETED: 5,
    FSMEvent.EVT_READ_COMPLETED: 5,
    FSMEvent.EVT_INTERACTION_FINISHED: 5,

    # =========================================================
    # NIVEL 6 — INICIO DE ENTRADA / PERCEPCIÓN
    # =========================================================
    FSMEvent.EVT_SPEECH_START: 6,
    FSMEvent.EVT_GESTURE_DETECTED: 6,
    FSMEvent.EVT_ATTENTION_CONFIRMED: 6,
    FSMEvent.EVT_VISUAL_TARGET_DETECTED: 6,
    FSMEvent.EVT_READ_REQUEST_DETECTED: 6,

    # =========================================================
    # NIVEL 7 — TIMEOUTS / PÉRDIDA DE CONTEXTO
    # =========================================================
    FSMEvent.EVT_IDLE_TIMEOUT: 7,
    FSMEvent.EVT_LISTEN_TIMEOUT: 7,
    FSMEvent.EVT_CONFIRMATION_TIMEOUT: 7,
    FSMEvent.EVT_ACTION_TIMEOUT: 7,
    FSMEvent.EVT_ATTENTION_LOST: 7,
    FSMEvent.EVT_CONTEXT_LOST: 7,

    # =========================================================
    # NIVEL 8 — ACTIVACIONES EXTERNAS
    # =========================================================
    FSMEvent.EVT_NFC_ACTIVATE: 8,
    FSMEvent.EVT_WAKEWORD: 8,
    FSMEvent.EVT_PRESENCE_CONFIRMED: 8,
    FSMEvent.EVT_ATTENTION_GAINED: 8,

    # =========================================================
    # NIVEL 9 — ACTIVACIONES PROGRAMADAS / BAJA URGENCIA
    # =========================================================
    FSMEvent.EVT_SCHEDULE_TRIGGERED: 9,

    # =========================================================
    # NIVEL 10 — EVENTOS DE CICLO DE VIDA NO CRÍTICOS
    # =========================================================
    FSMEvent.EVT_BOOT: 10,
    FSMEvent.EVT_INIT_COMPLETED: 10,
    FSMEvent.EVT_CONFIRMATION_REQUIRED: 10,
    FSMEvent.EVT_NFC_DEACTIVATE: 10,
}

DEFAULT_EVENT_PRIORITY = 99
"""
Prioridad por defecto para eventos no contemplados explícitamente.
"""