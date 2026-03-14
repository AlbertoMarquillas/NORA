"""
fsm_definitions.py

Este módulo define los tipos fundamentales de la FSM de NORA:
estados, eventos, causas de rechazo y estructuras de resultado.

Este archivo constituye la base semántica del sistema de control.
Aquí se define qué modos globales puede adoptar NORA, qué estímulos
o comandos puede recibir, y cómo se representa el resultado del
procesamiento de un evento por la máquina de estados.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Any


class FSMState(Enum):
    """
    Estados operativos principales del sistema NORA.

    Estos estados representan el modo global del sistema y determinan
    cómo se interpretan los eventos entrantes.

    Notes
    -----
    Un estado debe representar una situación global del sistema que
    modifica la forma en que NORA responde a los eventos. Los detalles
    concretos de una entrada, acción o contexto no deben modelarse como
    estado si no alteran realmente la semántica global del sistema.
    """

    APAGADO = auto()
    """
    Sistema completamente apagado o no operativo.

    NORA no debe aceptar interacción normal ni ejecutar procesamiento
    operativo. Solo deberían aceptarse comandos privilegiados de arranque
    o mantenimiento, si se implementan.
    """

    INICIALIZANDO = auto()
    """
    Arranque del sistema y carga de módulos.

    En este estado NORA inicializa subsistemas, valida dependencias,
    recupera configuración y prepara el runtime antes de entrar en
    reposo operativo.
    """

    INACTIVO = auto()
    """
    Sistema encendido pero sin interacción activa.

    NORA permanece disponible y a la espera de un evento de activación
    válido, como wake word, gesto, presencia confirmada, NFC o trigger
    programado.
    """

    ATENDIENDO = auto()
    """
    NORA ha sido activada y está enfocada en una interacción.

    Este estado actúa como punto de entrada al flujo interactivo tras
    una activación válida. Desde aquí se decide si la interacción se
    orienta a voz, visión, lectura, confirmación u otra modalidad.
    """

    ESCUCHANDO = auto()
    """
    Esperando entrada de voz del usuario.

    NORA está preparada para capturar y procesar habla como fuente
    principal de entrada.
    """

    OBSERVANDO = auto()
    """
    Esperando señal visual o gestual relevante.

    NORA está preparada para capturar una señal procedente del canal
    visual, como un gesto, una presencia mantenida o un estímulo de
    atención visual.
    """

    INTERPRETANDO = auto()
    """
    Interpretación de entrada multimodal.

    En este estado NORA transforma entradas ya capturadas en una
    representación semántica utilizable, como intención, comando,
    entidad o consulta estructurada.
    """

    PLANIFICANDO = auto()
    """
    Decisión sobre qué acción ejecutar.

    NORA ya ha interpretado la entrada y ahora decide la siguiente
    operación global del sistema: responder, pedir confirmación,
    consultar un recurso, tomar una imagen, leer contenido, etc.
    """

    ESPERANDO_CONFIRMACION = auto()
    """
    Esperando confirmación del usuario antes de ejecutar una acción.

    Este estado es útil para operaciones ambiguas, sensibles o con
    impacto externo relevante.
    """

    EJECUTANDO_ACCION = auto()
    """
    Ejecución de una acción concreta.

    NORA está realizando una operación decidida previamente, ya sea
    una acción digital, lógica, sensorial o física.
    """

    HABLANDO = auto()
    """
    Produciendo salida verbal mediante TTS.

    NORA está respondiendo verbalmente al usuario y, salvo diseño
    contrario, no debería iniciar una nueva interacción incompatible
    hasta finalizar esta fase.
    """

    FINALIZANDO_INTERACCION = auto()
    """
    Cierre de interacción antes de volver a reposo.

    NORA completa tareas de limpieza, cierre de contexto y transición
    de vuelta a INACTIVO o a otro estado estable.
    """

    SUSPENDIDO = auto()
    """
    Sistema suspendido o inhibido.

    NORA permanece encendida pero desactiva parcial o totalmente la
    recepción de activaciones o interacciones normales.
    """

    RECUPERANDOSE = auto()
    """
    Estado transitorio de recuperación tras error.

    NORA intenta restaurar condiciones operativas después de un fallo
    o reinicialización de uno o varios módulos.
    """

    ERROR = auto()
    """
    Estado de fallo crítico o no recuperado.

    NORA ha detectado una condición que impide continuar la operación
    normal sin intervención o recuperación explícita.
    """


class FSMEvent(Enum):
    """
    Eventos consumibles por la FSM de NORA.

    Los eventos representan estímulos externos, señales internas,
    expiraciones temporales o comandos explícitos. Todo cambio de estado
    debe producirse como respuesta a un evento.

    Notes
    -----
    Convención de nombres:
    - EVT_* : suceso u observación del sistema
    - CMD_* : comando explícito o instrucción externa
    """

    # =========================================================
    # EVENTOS DE CICLO DE VIDA DEL SISTEMA
    # =========================================================

    EVT_BOOT = auto()
    """
    Solicitud o detección de arranque del sistema.
    """

    EVT_INIT_COMPLETED = auto()
    """
    Inicialización completada con éxito.
    """

    EVT_SHUTDOWN = auto()
    """
    Solicitud o ejecución de apagado del sistema.
    """

    # =========================================================
    # EVENTOS DE ACTIVACIÓN
    # =========================================================

    EVT_NFC_ACTIVATE = auto()
    """
    Activación mediante identificación NFC válida.
    """

    EVT_WAKEWORD = auto()
    """
    Activación por palabra clave detectada.
    """

    EVT_PRESENCE_CONFIRMED = auto()
    """
    Activación por presencia física confirmada.
    """

    EVT_ATTENTION_GAINED = auto()
    """
    Activación por atención visual detectada o ganada.
    """

    EVT_SCHEDULE_TRIGGERED = auto()
    """
    Activación por trigger programado.
    """

    # =========================================================
    # EVENTOS DE CAPTURA DE ENTRADA
    # =========================================================

    EVT_SPEECH_START = auto()
    """
    Inicio de entrada de voz detectado.
    """

    EVT_SPEECH_RECOGNIZED = auto()
    """
    Entrada verbal reconocida correctamente.
    """

    EVT_GESTURE_DETECTED = auto()
    """
    Señal gestual detectada, aún no necesariamente interpretada.
    """

    EVT_GESTURE_COMMAND = auto()
    """
    Comando gestual interpretado correctamente.
    """

    EVT_ATTENTION_CONFIRMED = auto()
    """
    Confirmación de atención visual sostenida.
    """

    EVT_VISUAL_TARGET_DETECTED = auto()
    """
    Detección de objetivo visual relevante.
    """

    EVT_READ_REQUEST_DETECTED = auto()
    """
    Detección de intención de lectura o análisis visual de contenido.
    """

    # =========================================================
    # EVENTOS DE INTERPRETACIÓN Y PLANIFICACIÓN
    # =========================================================

    EVT_INPUT_INTERPRETED = auto()
    """
    La entrada multimodal ha sido interpretada con éxito.
    """

    EVT_PLAN_READY = auto()
    """
    El plan de acción ha sido construido y está listo para ejecutarse.
    """

    EVT_CONFIRMATION_REQUIRED = auto()
    """
    La acción prevista requiere confirmación del usuario.
    """

    EVT_CONFIRMATION_RECEIVED = auto()
    """
    Confirmación positiva recibida.
    """

    EVT_CONFIRMATION_REJECTED = auto()
    """
    Confirmación negativa o rechazo recibido.
    """

    # =========================================================
    # EVENTOS DE EJECUCIÓN DE ACCIONES
    # =========================================================

    EVT_ACTION_STARTED = auto()
    """
    Inicio confirmado de la ejecución de una acción.
    """

    EVT_ACTION_COMPLETED = auto()
    """
    Acción completada con éxito.
    """

    EVT_ACTION_FAILED = auto()
    """
    Fallo durante la ejecución de la acción.
    """

    EVT_SPEECH_OUTPUT_STARTED = auto()
    """
    Inicio de salida verbal.
    """

    EVT_SPEECH_OUTPUT_FINISHED = auto()
    """
    Finalización de salida verbal.
    """

    EVT_CAPTURE_COMPLETED = auto()
    """
    Captura de imagen o recurso sensorial completada.
    """

    EVT_READ_COMPLETED = auto()
    """
    Lectura o análisis de contenido completado.
    """

    # =========================================================
    # EVENTOS DE FINALIZACIÓN DE INTERACCIÓN
    # =========================================================

    EVT_INTERACTION_FINISHED = auto()
    """
    La interacción ha concluido y puede cerrarse.
    """

    # =========================================================
    # EVENTOS DE TIMEOUT Y PÉRDIDA DE CONTEXTO
    # =========================================================

    EVT_IDLE_TIMEOUT = auto()
    """
    Tiempo global de inactividad excedido.
    """

    EVT_LISTEN_TIMEOUT = auto()
    """
    Tiempo excedido esperando voz.
    """

    EVT_CONFIRMATION_TIMEOUT = auto()
    """
    Tiempo excedido esperando confirmación.
    """

    EVT_ACTION_TIMEOUT = auto()
    """
    Tiempo excedido durante ejecución de acción.
    """

    EVT_ATTENTION_LOST = auto()
    """
    Pérdida de atención visual o de foco del usuario.
    """

    EVT_CONTEXT_LOST = auto()
    """
    Pérdida de contexto operativo relevante para continuar la interacción.
    """

    # =========================================================
    # EVENTOS DE ERROR Y RECUPERACIÓN
    # =========================================================

    EVT_MODULE_FAILURE = auto()
    """
    Falla técnica en módulo crítico.
    """

    EVT_MIC_FAILURE = auto()
    """
    Falla del canal de audio o micrófono.
    """

    EVT_CAMERA_FAILURE = auto()
    """
    Falla del canal de visión o cámara.
    """

    EVT_PROCESS_FAILURE = auto()
    """
    Error en interpretación, planificación o procesamiento interno.
    """

    EVT_RECOVERY_STARTED = auto()
    """
    Inicio del proceso de recuperación.
    """

    EVT_RECOVERY_SUCCESS = auto()
    """
    Recuperación completada con éxito.
    """

    EVT_ERROR_RECOVERY_TIMEOUT = auto()
    """
    Tiempo de recuperación agotado.
    """

    # =========================================================
    # COMANDOS EXPLÍCITOS DEL SISTEMA
    # =========================================================

    CMD_FORCE_RESUME = auto()
    """
    Reanudación forzada del sistema o de la interacción.
    """

    CMD_INHIBIR_ACTIVACION = auto()
    """
    Inhibición de activaciones externas.
    """

    CMD_INHIBIR_ESCUCHA = auto()
    """
    Inhibición del canal de voz.
    """

    CMD_CANCEL_LISTENING = auto()
    """
    Cancelación explícita del estado de escucha.
    """

    CMD_CANCEL_ACTION = auto()
    """
    Cancelación explícita de la acción en curso.
    """

    CMD_SUSPEND = auto()
    """
    Suspensión explícita del sistema.
    """

    CMD_WAKE = auto()
    """
    Reactivación explícita desde suspensión.
    """

    # =========================================================
    # EVENTOS DE DESACTIVACIÓN
    # =========================================================

    EVT_NFC_DEACTIVATE = auto()
    """
    Desactivación mediante NFC o retirada de autorización.
    """


class FSMRejectionReason(Enum):
    """
    Motivos posibles por los que un evento no genera transición.
    """

    QUEUE_EMPTY = auto()
    """
    No había eventos pendientes en la cola.
    """

    NO_TRANSITION_DEFINED = auto()
    """
    No existe una transición definida para la pareja (estado, evento).
    """

    CONDITION_FAILED = auto()
    """
    Una o más condiciones de transición no se cumplieron.
    """

    GUARD_FAILED = auto()
    """
    Una o más guardias bloquearon la transición.
    """

    INVALID_EVENT_PAYLOAD = auto()
    """
    El evento era conocido, pero su payload o metadatos eran inválidos.
    """

    SYSTEM_NOT_READY = auto()
    """
    El sistema no estaba listo para procesar el evento en ese momento.
    """

    EVENT_SUPERSEDED = auto()
    """
    El evento quedó desplazado por otro de mayor prioridad o por pérdida de vigencia.
    """


@dataclass(slots=True)
class FSMQueuedEvent:
    """
    Evento encolado para procesamiento por la FSM.

    Attributes
    ----------
    event : FSMEvent
        Evento lógico de la FSM.
    timestamp : float
        Marca temporal del evento.
    priority : int
        Prioridad numérica del evento. Menor valor implica mayor prioridad.
    sequence : int
        Secuencia monotónica para desempate determinista.
    source : str
        Fuente del evento.
    description : str
        Descripción legible asociada al evento.
    payload : dict[str, Any]
        Metadatos adicionales del evento.
    """

    event: FSMEvent
    timestamp: float
    priority: int
    sequence: int
    source: str = "unknown"
    description: str = ""
    payload: dict[str, Any] = field(default_factory=dict)

    def __lt__(self, other: "FSMQueuedEvent") -> bool:
        """
        Define el orden de prioridad para la cola heap.

        Parameters
        ----------
        other : FSMQueuedEvent
            Evento con el que se compara.

        Returns
        -------
        bool
            True si este evento debe procesarse antes que el otro.
        """
        if self.priority != other.priority:
            return self.priority < other.priority
        if self.timestamp != other.timestamp:
            return self.timestamp < other.timestamp
        return self.sequence < other.sequence


@dataclass(slots=True)
class FSMProcessResult:
    """
    Resultado del procesamiento de un evento por la FSM.

    Attributes
    ----------
    accepted : bool
        Indica si el evento produjo transición.
    source_state : FSMState | None
        Estado de origen.
    target_state : FSMState | None
        Estado de destino si hubo transición.
    event : FSMEvent | None
        Evento procesado.
    reason : FSMRejectionReason | None
        Motivo de rechazo si no hubo transición.
    message : str
        Mensaje explicativo.
    timestamp : float | None
        Timestamp del procesamiento.
    source : str
        Fuente del evento.
    payload : dict[str, Any]
        Payload asociado al evento.
    """

    accepted: bool
    source_state: FSMState | None
    target_state: FSMState | None
    event: FSMEvent | None
    reason: FSMRejectionReason | None
    message: str
    timestamp: float | None
    source: str = ""
    payload: dict[str, Any] = field(default_factory=dict)