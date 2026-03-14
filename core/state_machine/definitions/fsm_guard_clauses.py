"""
fsm_guard_clauses.py

Guardias evaluables durante una transición de la FSM de NORA.

Las guardias son reglas de validación dura que se ejecutan cuando una
transición ya parece válida por estado, evento y condiciones de contexto,
pero aún debe superarse una comprobación adicional de seguridad,
consistencia o disponibilidad operativa.

A diferencia de las condiciones, las guardias reciben información completa
sobre la transición propuesta: estado actual, evento, estado destino y
contexto operativo.
"""

from .fsm_conditions import FSMContext
from .fsm_definitions import FSMEvent, FSMState


def guardia_no_transicionar_a_escucha_si_audio_falla(
    estado_actual: FSMState,
    evento: FSMEvent,
    estado_destino: FSMState,
    context: FSMContext,
) -> bool:
    """
    Impide transiciones hacia ESCUCHANDO si el módulo de audio no está operativo.

    Parameters
    ----------
    estado_actual : FSMState
        Estado actual de la FSM.
    evento : FSMEvent
        Evento recibido.
    estado_destino : FSMState
        Estado destino propuesto.
    context : FSMContext
        Contexto operativo actual.

    Returns
    -------
    bool
        True si la transición está permitida; False en caso contrario.
    """
    if estado_destino == FSMState.ESCUCHANDO and not context.modulo_audio_operativo:
        return False
    return True


def guardia_no_transicionar_a_observacion_si_vision_falla(
    estado_actual: FSMState,
    evento: FSMEvent,
    estado_destino: FSMState,
    context: FSMContext,
) -> bool:
    """
    Impide transiciones hacia OBSERVANDO si el módulo de visión no está operativo.

    Parameters
    ----------
    estado_actual : FSMState
        Estado actual de la FSM.
    evento : FSMEvent
        Evento recibido.
    estado_destino : FSMState
        Estado destino propuesto.
    context : FSMContext
        Contexto operativo actual.

    Returns
    -------
    bool
        True si la transición está permitida; False en caso contrario.
    """
    if estado_destino == FSMState.OBSERVANDO and not context.modulo_vision_operativo:
        return False
    return True


def guardia_bloquear_interpretacion_si_sin_usuario(
    estado_actual: FSMState,
    evento: FSMEvent,
    estado_destino: FSMState,
    context: FSMContext,
) -> bool:
    """
    Impide transitar a INTERPRETANDO si no hay usuario presente.

    Parameters
    ----------
    estado_actual : FSMState
        Estado actual de la FSM.
    evento : FSMEvent
        Evento recibido.
    estado_destino : FSMState
        Estado destino propuesto.
    context : FSMContext
        Contexto operativo actual.

    Returns
    -------
    bool
        True si la transición está permitida; False en caso contrario.
    """
    if estado_destino == FSMState.INTERPRETANDO and not context.usuario_presente:
        return False
    return True


def guardia_bloquear_planificacion_si_procesamiento_falla(
    estado_actual: FSMState,
    evento: FSMEvent,
    estado_destino: FSMState,
    context: FSMContext,
) -> bool:
    """
    Impide transitar a PLANIFICANDO si el subsistema de procesamiento no está operativo.

    Parameters
    ----------
    estado_actual : FSMState
        Estado actual de la FSM.
    evento : FSMEvent
        Evento recibido.
    estado_destino : FSMState
        Estado destino propuesto.
    context : FSMContext
        Contexto operativo actual.

    Returns
    -------
    bool
        True si la transición está permitida; False en caso contrario.
    """
    if (
        estado_destino == FSMState.PLANIFICANDO
        and not context.modulo_procesamiento_operativo
    ):
        return False
    return True


def guardia_bloquear_ejecucion_si_acciones_inhibidas(
    estado_actual: FSMState,
    evento: FSMEvent,
    estado_destino: FSMState,
    context: FSMContext,
) -> bool:
    """
    Impide transitar a EJECUTANDO_ACCION si las acciones están inhibidas.

    Parameters
    ----------
    estado_actual : FSMState
        Estado actual de la FSM.
    evento : FSMEvent
        Evento recibido.
    estado_destino : FSMState
        Estado destino propuesto.
    context : FSMContext
        Contexto operativo actual.

    Returns
    -------
    bool
        True si la transición está permitida; False en caso contrario.
    """
    if estado_destino == FSMState.EJECUTANDO_ACCION and context.acciones_inhibidas:
        return False
    return True


def guardia_bloquear_habla_si_audio_falla(
    estado_actual: FSMState,
    evento: FSMEvent,
    estado_destino: FSMState,
    context: FSMContext,
) -> bool:
    """
    Impide transitar a HABLANDO si el módulo de audio no está operativo.

    Parameters
    ----------
    estado_actual : FSMState
        Estado actual de la FSM.
    evento : FSMEvent
        Evento recibido.
    estado_destino : FSMState
        Estado destino propuesto.
    context : FSMContext
        Contexto operativo actual.

    Returns
    -------
    bool
        True si la transición está permitida; False en caso contrario.
    """
    if estado_destino == FSMState.HABLANDO and not context.modulo_audio_operativo:
        return False
    return True


def guardia_no_activar_si_sistema_suspendido(
    estado_actual: FSMState,
    evento: FSMEvent,
    estado_destino: FSMState,
    context: FSMContext,
) -> bool:
    """
    Impide activar interacción normal si el sistema está suspendido.

    Esta guardia añade una segunda línea de defensa frente a activaciones
    accidentales o eventos mal emitidos cuando NORA se encuentra en modo
    suspendido.

    Parameters
    ----------
    estado_actual : FSMState
        Estado actual de la FSM.
    evento : FSMEvent
        Evento recibido.
    estado_destino : FSMState
        Estado destino propuesto.
    context : FSMContext
        Contexto operativo actual.

    Returns
    -------
    bool
        True si la transición está permitida; False en caso contrario.
    """
    if estado_actual == FSMState.SUSPENDIDO and estado_destino == FSMState.ATENDIENDO:
        return False
    return True


def guardia_siempre_permitido(
    estado_actual: FSMState,
    evento: FSMEvent,
    estado_destino: FSMState,
    context: FSMContext,
) -> bool:
    """
    Guarda incondicional.

    Parameters
    ----------
    estado_actual : FSMState
        Estado actual.
    evento : FSMEvent
        Evento recibido.
    estado_destino : FSMState
        Estado destino propuesto.
    context : FSMContext
        Contexto operativo actual.

    Returns
    -------
    bool
        Siempre True.
    """
    return True