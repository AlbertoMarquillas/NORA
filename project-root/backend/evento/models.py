from django.db import models

class EventoRecibido(models.Model):
    """
    Representa un evento FSM recibido desde cualquier origen (simulación, sensores, etc.).
    Se almacena con tipo, nombre del evento, descripción y marca temporal.
    """
    tipo = models.CharField(max_length=64)
    evento = models.CharField(max_length=64)
    descripcion = models.TextField(blank=True)
    origen = models.CharField(max_length=64, default="frontend")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.timestamp}] {self.evento} ({self.tipo})"


class TransicionFSM(models.Model):
    """
    Registro estructurado de una transición de estado en la FSM de NORA.
    """
    estado_anterior = models.CharField(max_length=64)
    evento = models.CharField(max_length=64)
    estado_nuevo = models.CharField(max_length=64)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.estado_anterior} --({self.evento})--> {self.estado_nuevo}"
