# backend/voz/responder.py

import pyttsx3

def responder_texto(texto):
    """
    Convierte un texto en voz y lo reproduce por altavoz.
    """
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(texto)
    engine.runAndWait()
