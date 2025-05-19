"""
fsm_guard_clauses.py

Este módulo define cláusulas de guarda para controlar transiciones sensibles
de la FSM de NORA. Las guardias son funciones booleanas que reciben el estado
actual, el evento recibido, el estado destino previsto y un contexto del sistema.

Se utilizan para evitar transiciones no deseadas en función de la situación
del sistema, errores previos, condiciones ambientales o preferencias del usuario.
"""

from fsm.definitions.fsm_definitions import FSMState, FSMEvent
from fsm.definitions.fsm_conditions import FSMContext

def guardia_no_transicionar_si_audio_falla(
    estado_actual: FSMState,
    evento: FSMEvent,
    estado_destino: FSMState,
    context: FSMContext
) -> bool:
    """
    Impide cualquier transición hacia ESCUCHA si el audio no está operativo.
    """
    if estado_destino == FSMState.ESCUCHA and not context.modulo_audio_operativo:
        return False
    return True

def guardia_bloquear_procesamiento_si_sin_usuario(
    estado_actual: FSMState,
    evento: FSMEvent,
    estado_destino: FSMState,
    context: FSMContext
) -> bool:
    """
    Impide transitar a PROCESANDO si no hay usuario presente.
    """
    if estado_destino == FSMState.PROCESANDO and not context.usuario_presente:
        return False
    return True

def guardia_siempre_permitido(
    estado_actual: FSMState,
    evento: FSMEvent,
    estado_destino: FSMState,
    context: FSMContext
) -> bool:
    """
    Guarda por defecto: permite cualquier transición.
    """
    return True
