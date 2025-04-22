"""
Módulo: voz/sintetizador.py

Este módulo define la clase SintetizadorVoz, que se encarga de reproducir
respuestas habladas mediante síntesis de texto a voz (TTS), utilizando
el motor pyttsx3. Se integra con el EventManager escuchando eventos EVT_DECIR_TEXTO.
"""

import pyttsx3
from src.sistema.event_manager import Evento

class SintetizadorVoz:
    def __init__(self, event_manager):
        self.engine = pyttsx3.init()
        self.em = event_manager
        self.em.suscribir("EVT_DECIR_TEXTO", self.hablar)
        print("[SintetizadorVoz] Suscrito a EVT_DECIR_TEXTO")

    def hablar(self, evento: Evento):
        texto = evento.datos.get("texto", "")
        if texto:
            print(f"[SintetizadorVoz] → {texto}")
            self.engine.say(texto)
            self.engine.runAndWait()
        else:
            print("[SintetizadorVoz] Advertencia: evento sin campo 'texto'")
