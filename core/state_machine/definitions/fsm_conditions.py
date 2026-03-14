"""
fsm_conditions.py

Este módulo define el contexto operativo de la FSM y las condiciones
evaluables sobre dicho contexto. Las condiciones se utilizan en
transiciones concretas para decidir si una regla puede aplicarse.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class FSMContext:
    """
    Contexto operativo de la FSM de NORA.

    El contexto contiene información de estado global del sistema,
    sensores y condiciones operativas que pueden ser evaluadas por
    las condiciones de transición.

    Notes
    -----
    El contexto no representa el estado de la FSM. El estado de la FSM
    se gestiona de forma independiente en el controlador. Este objeto
    solo contiene información auxiliar que puede influir en las reglas
    de transición.
    """

    # =========================================================
    # DATOS GENERALES
    # =========================================================

    sensor_data: dict[str, Any] = field(default_factory=dict)
    """
    Datos agregados de sensores y subsistemas.
    """

    # =========================================================
    # CONTEXTO DE USUARIO
    # =========================================================

    usuario_presente: bool = False
    """
    Indica si existe presencia de usuario confirmada.
    """

    atencion_usuario: bool = False
    """
    Indica si el usuario está prestando atención activa al sistema.
    """

    # =========================================================
    # ESTADO DE MÓDULOS
    # =========================================================

    modulo_audio_operativo: bool = True
    """
    Indica si el subsistema de audio está operativo.
    """

    modulo_vision_operativo: bool = True
    """
    Indica si el subsistema de visión está operativo.
    """

    modulo_procesamiento_operativo: bool = True
    """
    Indica si el subsistema de procesamiento está operativo.
    """

    # =========================================================
    # FLAGS DE CONTROL
    # =========================================================

    activacion_inhibida: bool = False
    """
    Indica si el sistema tiene inhibida la activación externa.
    """

    escucha_inhibida: bool = False
    """
    Indica si la entrada de audio está inhibida.
    """

    acciones_inhibidas: bool = False
    """
    Indica si la ejecución de acciones está temporalmente inhibida.
    """

    # =========================================================
    # CONTEXTO DE INTERACCIÓN
    # =========================================================

    ultima_fuente_activacion: str | None = None
    """
    Última fuente que activó el sistema.
    """

    ultima_intencion_detectada: str | None = None
    """
    Última intención interpretada por el sistema.
    """

    interaccion_activa: bool = False
    """
    Indica si hay una interacción activa en curso.
    """

    # =========================================================
    # TEMPORALIDAD
    # =========================================================

    ultimo_evento_ts: float | None = None
    """
    Timestamp del último evento relevante procesado.
    """

    inicio_interaccion_ts: float | None = None
    """
    Timestamp de inicio de la interacción actual.
    """

    # =========================================================
    # UTILIDADES
    # =========================================================

    def merge(self, **changes: Any) -> None:
        """
        Actualiza parcialmente el contexto actual.

        Parameters
        ----------
        **changes : Any
            Campos del contexto a actualizar.
        """
        for key, value in changes.items():
            if not hasattr(self, key):
                raise AttributeError(f"FSMContext no tiene el atributo '{key}'.")
            setattr(self, key, value)


# =========================================================
# CONDICIONES BÁSICAS
# =========================================================


def condicion_siempre(context: FSMContext) -> bool:
    """
    Condición incondicional.
    """
    return True


# =========================================================
# CONDICIONES DE USUARIO
# =========================================================


def condicion_usuario_presente(context: FSMContext) -> bool:
    """
    Comprueba si hay un usuario presente.
    """
    return context.usuario_presente


def condicion_usuario_atento(context: FSMContext) -> bool:
    """
    Comprueba si el usuario está prestando atención al sistema.
    """
    return context.atencion_usuario


# =========================================================
# CONDICIONES DE MÓDULOS
# =========================================================


def condicion_audio_operativo(context: FSMContext) -> bool:
    """
    Comprueba si el subsistema de audio está operativo.
    """
    return context.modulo_audio_operativo


def condicion_vision_operativa(context: FSMContext) -> bool:
    """
    Comprueba si el subsistema de visión está operativo.
    """
    return context.modulo_vision_operativo


def condicion_procesamiento_operativo(context: FSMContext) -> bool:
    """
    Comprueba si el subsistema de procesamiento está operativo.
    """
    return context.modulo_procesamiento_operativo


# =========================================================
# CONDICIONES DE CONTROL
# =========================================================


def condicion_activacion_no_inhibida(context: FSMContext) -> bool:
    """
    Comprueba si la activación externa está permitida.
    """
    return not context.activacion_inhibida


def condicion_escucha_no_inhibida(context: FSMContext) -> bool:
    """
    Comprueba si la escucha está permitida.
    """
    return not context.escucha_inhibida


def condicion_acciones_permitidas(context: FSMContext) -> bool:
    """
    Comprueba si la ejecución de acciones está permitida.
    """
    return not context.acciones_inhibidas


# =========================================================
# CONDICIONES DE INTERACCIÓN
# =========================================================


def condicion_interaccion_activa(context: FSMContext) -> bool:
    """
    Comprueba si hay una interacción activa en curso.
    """
    return context.interaccion_activa


def condicion_no_interaccion_activa(context: FSMContext) -> bool:
    """
    Comprueba si no hay interacción activa.
    """
    return not context.interaccion_activa