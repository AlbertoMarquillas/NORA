"""
fsm_emotional_states.py

Modelo afectivo-operativo complementario a la FSM funcional de NORA.

Este módulo no sustituye los estados funcionales de la máquina de estados,
sino que proporciona una capa adicional para representar la disposición
afectiva dominante del sistema y modular su comportamiento.

El objetivo no es simular emociones humanas de forma teatral, sino aportar
una representación interna útil para ajustar estilo de respuesta, nivel de
vigilancia, tolerancia al error, persistencia de interacción o necesidad
de confirmación.
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from enum import Enum, auto


class EmotionalState(Enum):
    """
    Estados afectivo-operativos base de NORA.

    Notes
    -----
    Estos estados deben interpretarse como moduladores internos del
    comportamiento, no como emociones humanas literales.
    """

    NEUTRO = auto()
    """
    Estado base sin sesgo afectivo dominante.
    """

    CURIOSIDAD = auto()
    """
    Apertura a explorar nueva información o estímulos relevantes.
    """

    FOCO = auto()
    """
    Alta concentración en una tarea o interacción concreta.
    """

    DUDA = auto()
    """
    Incertidumbre operativa ante una entrada o decisión ambigua.
    """

    ALERTA = auto()
    """
    Elevación de vigilancia ante un evento importante o potencialmente anómalo.
    """

    FRUSTRACION = auto()
    """
    Estado asociado a errores repetidos, bloqueos o fallos de ejecución.
    """

    SATISFACCION = auto()
    """
    Estado asociado a una ejecución exitosa o interacción resuelta correctamente.
    """

    ESPERA_PROLONGADA = auto()
    """
    Estado asociado a periodos extensos de inactividad o ausencia de estímulo.
    """

    RECUPERACION = auto()
    """
    Estado asociado a recuperación tras fallo o restablecimiento del sistema.
    """


@dataclass(slots=True)
class EmotionalStatus:
    """
    Estado emocional actual del sistema.

    Attributes
    ----------
    estado : EmotionalState
        Estado afectivo dominante actual.
    intensidad : float
        Intensidad normalizada del estado en rango [0, 1].
    valencia : float
        Polaridad afectiva aproximada en rango [-1, 1].
        Valores negativos reflejan sesgo adverso; valores positivos,
        sesgo favorable.
    activacion : float
        Nivel de activación o arousal en rango [0, 1].
    trigger : str | None
        Causa o motivo principal del último cambio emocional.
    timestamp : float
        Marca temporal de la última actualización.
    """

    estado: EmotionalState = EmotionalState.NEUTRO
    intensidad: float = 0.0
    valencia: float = 0.0
    activacion: float = 0.0
    trigger: str | None = None
    timestamp: float = field(default_factory=time.time)

    def actualizar(
        self,
        nuevo_estado: EmotionalState,
        intensidad: float,
        *,
        trigger: str | None = None,
        valencia: float | None = None,
        activacion: float | None = None,
    ) -> None:
        """
        Actualiza el estado emocional dominante.

        Parameters
        ----------
        nuevo_estado : EmotionalState
            Nuevo estado afectivo dominante.
        intensidad : float
            Intensidad del nuevo estado en rango [0, 1].
        trigger : str | None, optional
            Motivo o causa principal del cambio.
        valencia : float | None, optional
            Nueva valencia en rango [-1, 1]. Si no se proporciona,
            se infiere a partir del estado emocional.
        activacion : float | None, optional
            Nuevo nivel de activación en rango [0, 1]. Si no se
            proporciona, se infiere a partir del estado emocional.
        """
        self.estado = nuevo_estado
        self.intensidad = self._clamp_01(intensidad)
        self.valencia = (
            self._clamp_signed_unit(valencia)
            if valencia is not None
            else self._default_valencia(nuevo_estado, self.intensidad)
        )
        self.activacion = (
            self._clamp_01(activacion)
            if activacion is not None
            else self._default_activacion(nuevo_estado, self.intensidad)
        )
        self.trigger = trigger
        self.timestamp = time.time()

    def modular(
        self,
        nuevo_estado: EmotionalState,
        delta_intensidad: float,
        *,
        trigger: str | None = None,
    ) -> None:
        """
        Modula el estado emocional actual de forma incremental.

        Si el nuevo estado coincide con el actual, la intensidad se ajusta
        sumando `delta_intensidad`. Si no coincide, el sistema cambia al
        nuevo estado con una intensidad inicial derivada de dicho delta.

        Parameters
        ----------
        nuevo_estado : EmotionalState
            Estado emocional a reforzar o introducir.
        delta_intensidad : float
            Ajuste incremental de intensidad.
        trigger : str | None, optional
            Motivo del ajuste emocional.
        """
        if nuevo_estado == self.estado:
            nueva_intensidad = self._clamp_01(self.intensidad + delta_intensidad)
        else:
            nueva_intensidad = self._clamp_01(abs(delta_intensidad))

        self.actualizar(
            nuevo_estado=nuevo_estado,
            intensidad=nueva_intensidad,
            trigger=trigger,
        )

    def decaer(self, tasa_por_segundo: float = 0.02) -> None:
        """
        Reduce progresivamente la intensidad emocional en función del tiempo
        transcurrido desde la última actualización.

        Parameters
        ----------
        tasa_por_segundo : float, optional
            Tasa lineal de decaimiento por segundo.
        """
        ahora = time.time()
        delta_t = max(0.0, ahora - self.timestamp)

        decremento = tasa_por_segundo * delta_t
        nueva_intensidad = self._clamp_01(self.intensidad - decremento)

        self.intensidad = nueva_intensidad
        self.activacion = self._clamp_01(self.activacion - decremento * 0.8)

        if self.intensidad == 0.0:
            self.estado = EmotionalState.NEUTRO
            self.valencia = 0.0
            self.activacion = 0.0
            self.trigger = None

        self.timestamp = ahora

    def reiniciar(self) -> None:
        """
        Reinicia el estado emocional a la condición neutra base.
        """
        self.estado = EmotionalState.NEUTRO
        self.intensidad = 0.0
        self.valencia = 0.0
        self.activacion = 0.0
        self.trigger = None
        self.timestamp = time.time()

    def snapshot(self) -> dict[str, float | str | None]:
        """
        Devuelve una representación serializable del estado emocional actual.

        Returns
        -------
        dict[str, float | str | None]
            Snapshot del estado emocional.
        """
        return {
            "estado": self.estado.name,
            "intensidad": self.intensidad,
            "valencia": self.valencia,
            "activacion": self.activacion,
            "trigger": self.trigger,
            "timestamp": self.timestamp,
        }

    @staticmethod
    def _clamp_01(value: float) -> float:
        """
        Limita un valor al rango [0, 1].

        Parameters
        ----------
        value : float
            Valor de entrada.

        Returns
        -------
        float
            Valor acotado.
        """
        return max(0.0, min(1.0, value))

    @staticmethod
    def _clamp_signed_unit(value: float) -> float:
        """
        Limita un valor al rango [-1, 1].

        Parameters
        ----------
        value : float
            Valor de entrada.

        Returns
        -------
        float
            Valor acotado.
        """
        return max(-1.0, min(1.0, value))

    @staticmethod
    def _default_valencia(
        estado: EmotionalState,
        intensidad: float,
    ) -> float:
        """
        Infere una valencia base a partir del estado emocional.

        Parameters
        ----------
        estado : EmotionalState
            Estado afectivo dominante.
        intensidad : float
            Intensidad actual.

        Returns
        -------
        float
            Valencia inferida.
        """
        base = {
            EmotionalState.NEUTRO: 0.0,
            EmotionalState.CURIOSIDAD: 0.3,
            EmotionalState.FOCO: 0.1,
            EmotionalState.DUDA: -0.2,
            EmotionalState.ALERTA: -0.1,
            EmotionalState.FRUSTRACION: -0.7,
            EmotionalState.SATISFACCION: 0.7,
            EmotionalState.ESPERA_PROLONGADA: -0.2,
            EmotionalState.RECUPERACION: 0.2,
        }[estado]
        return max(-1.0, min(1.0, base * max(0.2, intensidad)))

    @staticmethod
    def _default_activacion(
        estado: EmotionalState,
        intensidad: float,
    ) -> float:
        """
        Infere una activación base a partir del estado emocional.

        Parameters
        ----------
        estado : EmotionalState
            Estado afectivo dominante.
        intensidad : float
            Intensidad actual.

        Returns
        -------
        float
            Activación inferida.
        """
        base = {
            EmotionalState.NEUTRO: 0.1,
            EmotionalState.CURIOSIDAD: 0.5,
            EmotionalState.FOCO: 0.7,
            EmotionalState.DUDA: 0.4,
            EmotionalState.ALERTA: 0.8,
            EmotionalState.FRUSTRACION: 0.75,
            EmotionalState.SATISFACCION: 0.45,
            EmotionalState.ESPERA_PROLONGADA: 0.2,
            EmotionalState.RECUPERACION: 0.35,
        }[estado]
        return max(0.0, min(1.0, base * max(0.2, intensidad)))