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

    print(">> Inicio del bucle de escucha")

    # Selección del micrófono
    mics = sr.Microphone.list_microphone_names()
    if DEBUG_VOZ:
        print(f"🎙️ Micrófonos disponibles: {mics}")

    if "pulse" in mics:
        mic_index = mics.index("pulse")
        if DEBUG_VOZ:
            print(f"🔄 Usando micrófono 'pulse' (índice {mic_index})")
    else:
        mic_index = DEVICE_INDEX
        if DEBUG_VOZ:
            print(f"🔄 Usando micrófono por índice: {mic_index}")

    try:
        with sr.Microphone(device_index=mic_index) as source:
            print("✅ Micrófono abierto correctamente.")
            try:
                print("🛠️ Ajustando ruido ambiente...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
            except Exception as e:
                print(f"⚠️ Error ajustando el ruido ambiente: {e}")
                recognizer.energy_threshold = ENERGY_THRESHOLD
                print(f"⚠️ Usando ENERGY_THRESHOLD fijo: {ENERGY_THRESHOLD}")

            print("🎧 Escuchando por el micro...")
            audio = recognizer.listen(
                source,
                timeout=TIMEOUT,
                phrase_time_limit=PHRASE_TIME_LIMIT
            )
    except sr.WaitTimeoutError:
        print("⏱️ No se detectó voz durante el tiempo límite.")
        return None
    except Exception as e:
        print(f"❌ Error al acceder al micro: {e}")
        return None

    # Reconocimiento de texto
    try:
        texto = recognizer.recognize_google(audio, language="es-ES")
        print(f"📝 Frase reconocida: {texto}")
        return texto
    except sr.UnknownValueError:
        print("🤔 No se entendió lo que se dijo.")
        return None
    except sr.RequestError as e:
        print(f"🔌 Error de conexión con el servicio de reconocimiento: {e}")
        return None
