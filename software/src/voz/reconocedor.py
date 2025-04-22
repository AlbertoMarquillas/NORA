"""
Módulo: voz/reconocedor.py

Este módulo define la clase ReconocedorVoz, responsable de simular o capturar
entrada de voz, transcribirla (mediante Vosk o simulación), y emitir eventos
reconocidos mediante el EventManager.
"""

from src.sistema.event_manager import Evento, EventManager
import random

class ReconocedorVoz:
    def __init__(self, event_manager: EventManager):
        self.em = event_manager

    def escuchar_simulado(self):
        """
        Simula una entrada de voz con un 70% de probabilidad de ser reconocida.
        """
        posibles_comandos = [
            "enciende la luz",
            "anótame beber agua",
            "cuál es la hora",
            "dime un dato curioso",
        ]
        
        threshold = 0.7  # 70% de probabilidad de éxito
        
        exito = random.random() < threshold  # 70% de éxito

        if exito:
            texto = random.choice(posibles_comandos)
            evento = Evento(
                tipo="EVT_COMMAND_RECOGNIZED",
                origen="voz",
                datos={"texto": texto},
                prioridad=2
            )
        else:
            evento = Evento(
                tipo="EVT_COMMAND_UNKNOWN",
                origen="voz",
                datos={},
                prioridad=3
            )

        print(f"[ReconocedorVoz] Emitiendo: {evento.tipo} {'('+evento.datos.get('texto')+')' if evento.datos else ''}")
        self.em.emitir(evento)
