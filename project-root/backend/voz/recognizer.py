"""
recognizer.py

Este módulo gestiona la captura de voz desde el micrófono
y su conversión a texto mediante el motor de reconocimiento de Google.
La configuración se extrae de definiciones.py
"""

import os
import sys
import speech_recognition as sr
from voz.definiciones import (
    DEVICE_INDEX,
    ENERGY_THRESHOLD,
    PAUSE_THRESHOLD,
    PHRASE_TIME_LIMIT,
    TIMEOUT,
    DEBUG_VOZ
)

import contextlib

@contextlib.contextmanager
def suprimir_alsa_errors():
    """
    Redirige el descriptor de errores estándar a /dev/null para ocultar
    mensajes molestos de ALSA, jackd, etc.
    """
    fd_stderr = sys.stderr.fileno()
    fd_devnull = os.open(os.devnull, os.O_WRONLY)
    old_stderr = os.dup(fd_stderr)
    try:
        os.dup2(fd_devnull, fd_stderr)
        yield
    finally:
        os.dup2(old_stderr, fd_stderr)
        os.close(fd_devnull)
        os.close(old_stderr)


def escuchar_frase() -> str | None:
    """
    Escucha una frase del micrófono y devuelve su transcripción en texto.

    Returns:
        str | None: El texto reconocido o None si no se pudo interpretar.
    """
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = ENERGY_THRESHOLD
    recognizer.pause_threshold = PAUSE_THRESHOLD

    try:
        with suprimir_alsa_errors():
            with sr.Microphone(device_index=sr.Microphone.list_microphone_names().index('pulse')) as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)
                if DEBUG_VOZ:
                    print("🎧 Escuchando por el micro...")

                audio = recognizer.listen(
                    source,
                    timeout=TIMEOUT,
                    phrase_time_limit=PHRASE_TIME_LIMIT
                )
    except sr.WaitTimeoutError:
        if DEBUG_VOZ:
            print("⏱️ No se detectó voz durante el tiempo límite.")
        return None
    except Exception as e:
        if DEBUG_VOZ:
            print(f"❌ Error al acceder al micro: {e}")
        return None

    # Reconocimiento de texto
    try:
        texto = recognizer.recognize_google(audio, language="es-ES")
        if DEBUG_VOZ:
            print(f"📝 Frase reconocida: {texto}")
        return texto
    except sr.UnknownValueError:
        if DEBUG_VOZ:
            print("🤔 No se entendió lo que se dijo.")
        return None
    except sr.RequestError as e:
        if DEBUG_VOZ:
            print(f"🔌 Error de conexión con el servicio de reconocimiento: {e}")
        return None
