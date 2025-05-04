"""
fsm_emotional_states.py

Este módulo define los estados emocionales posibles de NORA y proporciona
estructuras básicas para su evaluación, evolución y uso dentro del sistema
FSM o en sistemas paralelos de adaptación comportamental.

Estos estados no reemplazan los estados funcionales de la FSM, pero los
complementan ofreciendo un modelo afectivo capaz de modular decisiones,
prioridades o comportamientos.
"""

from enum import Enum, auto
from dataclasses import dataclass
import time

class EmotionalState(Enum):
    """Enumeración de estados emocionales base de NORA."""
    NEUTRO = auto()
    CURIOSIDAD = auto()
    FRUSTRACION = auto()
    SATISFACCION = auto()
    ALERTA = auto()
    ABURRIMIENTO = auto()

@dataclass
class EmotionalStatus:
    """
    Estructura que almacena el estado emocional actual del sistema y
    su intensidad relativa, junto con un timestamp de actualización.
    """
    estado: EmotionalState = EmotionalState.NEUTRO
    intensidad: float = 0.0  # Rango sugerido: 0.0 - 1.0
    timestamp: float = time.time()

    def actualizar(self, nuevo_estado: EmotionalState, intensidad: float):
        """Actualiza el estado emocional actual."""
        self.estado = nuevo_estado
        self.intensidad = max(0.0, min(1.0, intensidad))  # Clamp [0,1]
        self.timestamp = time.time()

    def decaer(self, factor: float = 0.01):
        """
        Reduce progresivamente la intensidad emocional para simular
        una evolución natural del estado afectivo.
        """
        self.intensidad = max(0.0, self.intensidad - factor)
