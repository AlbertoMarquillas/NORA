"""
responder.py

Este módulo se encarga de generar respuestas habladas a partir de texto.
Utiliza pyttsx3 en Windows y espeak-ng en Linux, configurable mediante definiciones.py.
"""

import platform
import subprocess
from voz.definiciones import TTS_RATE, TTS_VOLUME, TTS_VOICE, DEBUG_VOZ

# Almacena la última respuesta hablada (útil para REPETIR, logs, etc.)
ultima_respuesta = None

# Detectar sistema operativo
SO_ACTUAL = platform.system()


def responder_texto(texto: str):
    """
    Reproduce por voz un texto dado, usando el motor apropiado según el sistema operativo.

    Args:
        texto (str): La frase a pronunciar.
    """
    global ultima_respuesta
    ultima_respuesta = texto

    if DEBUG_VOZ:
        print(f"🗣️ Respuesta hablada: {texto}")

    if SO_ACTUAL == "Windows":
        _responder_con_pyttsx3(texto)
    else:
        _responder_con_espeak(texto)


def _responder_con_pyttsx3(texto: str):
    """
    Utiliza pyttsx3 para reproducir texto en sistemas Windows.
    """
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty("rate", TTS_RATE)
    engine.setProperty("volume", TTS_VOLUME)

    if TTS_VOICE:
        for voice in engine.getProperty("voices"):
            if TTS_VOICE.lower() in voice.name.lower():
                engine.setProperty("voice", voice.id)
                break

    engine.say(texto)
    engine.runAndWait()
    del engine


def _responder_con_espeak(texto: str):
    """
    Utiliza espeak-ng para reproducir texto en sistemas Linux.
    Requiere tener instalado el paquete `espeak-ng`.
    """
    cmd = [
        "espeak-ng",
        "-s", str(TTS_RATE),
        "-a", str(int(TTS_VOLUME * 200)),  # espeak-ng usa 0-200
        "-v", TTS_VOICE or "es",
        texto
    ]
    try:
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        print("❌ No se encontró espeak-ng. Instálalo con: sudo apt install espeak-ng")


def obtener_ultima_respuesta() -> str:
    """
    Devuelve el último texto que fue pronunciado por el sistema.
    """
    return ultima_respuesta or ""
