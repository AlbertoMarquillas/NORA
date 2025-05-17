"""
recognizer.py

Este módulo gestiona la captura de voz desde el micrófono
y su conversión a texto mediante el motor de reconocimiento de Google.
La configuración se extrae de definiciones.py
"""

import speech_recognition as sr
import os
import sys
import contextlib
from voz.definiciones import (
    DEVICE_INDEX,
    ENERGY_THRESHOLD,
    PAUSE_THRESHOLD,
    PHRASE_TIME_LIMIT,
    TIMEOUT,
    DEBUG_VOZ
)

@contextlib.contextmanager
def suprimir_stderr():
    """
    Context manager que suprime temporalmente la salida estándar de errores (stderr).
    Evita que ALSA/jack impriman errores en consola.
    """
    with open(os.devnull, 'w') as fnull:
        old_stderr = sys.stderr
        try:
            sys.stderr = fnull
            yield
        finally:
            sys.stderr = old_stderr




def escuchar_frase() -> str | None:
    """
    Escucha una frase del micrófono y devuelve su transcripción en texto.
    """
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = ENERGY_THRESHOLD
    recognizer.pause_threshold = PAUSE_THRESHOLD

    try:
        mic_list = sr.Microphone.list_microphone_names()
        if "pulse" in mic_list:
            device_index = mic_list.index("pulse")
        else:
            device_index = DEVICE_INDEX  # fallback definido en definiciones.py

        with suprimir_stderr():
            with sr.Microphone(device_index=device_index) as source:
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
