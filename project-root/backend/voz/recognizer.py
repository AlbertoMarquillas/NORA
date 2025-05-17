"""
recognizer.py

Este módulo gestiona la captura de voz desde el micrófono
y su conversión a texto mediante el motor de reconocimiento de Google.
La configuración se extrae de definiciones.py
"""

import speech_recognition as sr
from voz.definiciones import (
    DEVICE_INDEX,
    ENERGY_THRESHOLD,
    PAUSE_THRESHOLD,
    PHRASE_TIME_LIMIT,
    TIMEOUT,
    DEBUG_VOZ
)

def escuchar_frase() -> str | None:
    """
    Escucha una frase del micrófono y devuelve su transcripción en texto.

    Returns:
        str | None: El texto reconocido o None si no se pudo interpretar.
    """
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = ENERGY_THRESHOLD
    recognizer.pause_threshold = PAUSE_THRESHOLD

    mic_list = sr.Microphone.list_microphone_names()
    if DEBUG_VOZ:
        print("🎙️ Micrófonos disponibles:", mic_list)

    # Selección dinámica de índice
    try:
        if 'pulse' in mic_list:
            device_index = mic_list.index('pulse')
            if DEBUG_VOZ:
                print(f"🔄 Usando micrófono 'pulse' (índice {device_index})")
        else:
            device_index = DEVICE_INDEX
            if DEBUG_VOZ:
                print(f"⚠️ 'pulse' no encontrado. Usando índice por defecto: {DEVICE_INDEX}")
    except Exception as e:
        print(f"❌ Error al seleccionar micrófono: {e}")
        return None

    try:
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
