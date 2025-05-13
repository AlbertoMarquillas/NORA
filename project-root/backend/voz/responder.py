"""
responder.py

Este módulo se encarga de generar respuestas habladas a partir de texto.
Utiliza pyttsx3 como motor TTS offline, configurable mediante definiciones.py.
"""

import pyttsx3
from voz.definiciones import TTS_RATE, TTS_VOLUME, TTS_VOICE, DEBUG_VOZ

# Almacena la última respuesta hablada (útil para REPETIR, logs, etc.)
ultima_respuesta = None


def inicializar_motor():
    """
    Inicializa y configura el motor TTS de pyttsx3 según los parámetros definidos.
    Retorna el motor listo para usar.
    """
    engine = pyttsx3.init()
    engine.setProperty("rate", TTS_RATE)
    engine.setProperty("volume", TTS_VOLUME)

    if TTS_VOICE:
        # Cambia la voz si se ha definido una específica
        for voice in engine.getProperty("voices"):
            if TTS_VOICE.lower() in voice.name.lower():
                engine.setProperty("voice", voice.id)
                break

    return engine


def responder_texto(texto: str):
    """
    Reproduce por voz un texto dado, usando pyttsx3.

    Args:
        texto (str): La frase a pronunciar.
    """
    global ultima_respuesta
    engine = inicializar_motor()

    if DEBUG_VOZ:
        print(f"🗣️ Respuesta hablada: {texto}")

    ultima_respuesta = texto
    engine.say(texto)
    engine.runAndWait()


def obtener_ultima_respuesta() -> str:
    """
    Devuelve el último texto que fue pronunciado por el sistema.
    """
    return ultima_respuesta or ""
