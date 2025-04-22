"""
Módulo: sistema/fsm.py

Define los estados funcionales internos de NORA y una clase FSM (Finite State Machine)
que gestiona las transiciones de estado en respuesta a eventos del sistema.

Este módulo es pasivo: recibe eventos, decide el nuevo estado, y emite eventos
para que otros módulos reaccionen (como voz, interfaz o control).
"""

from enum import Enum, auto

class EstadoNora(Enum):
    REPOSO     = auto()  # Sistema completamente inactivo, esperando NFC o comando
    PASIVO     = auto()  # Observa sin actuar, detecta presencia
    ESCUCHA    = auto()  # Reconociendo voz, esperando comandos
    ACTIVO     = auto()  # Ejecutando tarea o interacción
    DESPEDIDA  = auto()  # Transición de apagado o pausa
    ERROR      = auto()  # Estado especial tras fallo de reconocimiento o ejecución


class FSM:
    def __init__(self):
        self.estado_actual = EstadoNora.REPOSO

    def transicion(self, evento):
        print(f"[FSM] Estado actual: {self.estado_actual.name} | Evento recibido: {evento}")

        if self.estado_actual == EstadoNora.REPOSO:
            if evento == "EVT_NFC_ACTIVATE":
                self.estado_actual = EstadoNora.PASIVO

        elif self.estado_actual == EstadoNora.PASIVO:
            if evento == "EVT_FACE_DETECTED":
                self.estado_actual = EstadoNora.ESCUCHA
            elif evento == "EVT_IDLE_TIMEOUT":
                self.estado_actual = EstadoNora.REPOSO

        elif self.estado_actual == EstadoNora.ESCUCHA:
            if evento == "EVT_COMMAND_RECOGNIZED":
                self.estado_actual = EstadoNora.ACTIVO
            elif evento == "EVT_COMMAND_UNKNOWN":
                self.estado_actual = EstadoNora.ERROR

        elif self.estado_actual == EstadoNora.ACTIVO:
            if evento == "EVT_SHUTDOWN_REQUEST":
                self.estado_actual = EstadoNora.DESPEDIDA
            elif evento == "EVT_IDLE_TIMEOUT":
                self.estado_actual = EstadoNora.PASIVO

        elif self.estado_actual == EstadoNora.ERROR:
            self.estado_actual = EstadoNora.PASIVO

        elif self.estado_actual == EstadoNora.DESPEDIDA:
            self.estado_actual = EstadoNora.REPOSO

        print(f"[FSM] Nuevo estado: {self.estado_actual.name}")
        return self.estado_actual
