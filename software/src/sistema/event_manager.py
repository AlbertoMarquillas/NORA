"""
Módulo: sistema/event_manager.py

Este módulo define el EventManager, un sistema de distribución de eventos
para la arquitectura modular de NORA. Permite que los módulos del sistema
se comuniquen de forma desacoplada y priorizada mediante suscripción a eventos.
"""

from collections import defaultdict
from datetime import datetime
from queue import PriorityQueue

class Evento:
    def __init__(self, tipo, origen, datos=None, prioridad=3):
        self.tipo = tipo
        self.origen = origen
        self.datos = datos or {}
        self.timestamp = datetime.now()
        self.prioridad = prioridad  # 1 = alta, 5 = baja

    def __lt__(self, other):
        return self.prioridad < other.prioridad


class EventManager:
    def __init__(self):
        self.oyentes = defaultdict(list)  # tipo_evento → [callbacks]
        self.cola = PriorityQueue()

    def suscribir(self, tipo_evento, callback):
        self.oyentes[tipo_evento].append(callback)
        print(f"[EventManager] Subscripción registrada para '{tipo_evento}'")

    def emitir(self, evento):
        print(f"[EventManager] Evento encolado: {evento.tipo} desde {evento.origen}")
        self.cola.put((evento.prioridad, evento))

    def procesar(self):
        while not self.cola.empty():
            _, evento = self.cola.get()
            print(f"[EventManager] Procesando {evento.tipo} desde {evento.origen} @ {evento.timestamp}")
            for callback in self.oyentes.get(evento.tipo, []):
                callback(evento)
