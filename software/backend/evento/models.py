from django.db import models

class TransicionFSM(models.Model):
    estado_anterior = models.CharField(max_length=50)
    evento = models.CharField(max_length=50)
    estado_nuevo = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.timestamp} | {self.estado_anterior} --({self.evento})--> {self.estado_nuevo}"
