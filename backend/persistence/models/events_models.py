"""
events_models.py

Modelos de persistencia relacionados con el historial de eventos y
transiciones de la máquina de estados del sistema NORA.
"""

from django.db import models
from core.state_machine.definitions.fsm_definitions import FSMState, FSMEvent


class TransicionFSM(models.Model):
    """
    Registro persistente de una transición de la máquina de estados FSM.
    """

    estado_anterior = models.CharField(
        max_length=50,
        choices=[(s.name, s.name) for s in FSMState],
    )

    evento = models.CharField(
        max_length=50,
        choices=[(e.name, e.name) for e in FSMEvent],
    )

    estado_nuevo = models.CharField(
        max_length=50,
        choices=[(s.name, s.name) for s in FSMState],
    )

    timestamp = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
    )

    metadata = models.JSONField(
        null=True,
        blank=True,
        help_text="Información contextual opcional del evento."
    )

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self) -> str:
        return (
            f"{self.timestamp} | "
            f"{self.estado_anterior} --({self.evento})--> {self.estado_nuevo}"
        )