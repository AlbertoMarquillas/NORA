# backend/voz/recognizer.py

import speech_recognition as sr

def escuchar_frase():
    """
    Escucha una frase por micrófono y devuelve el texto reconocido.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Escuchando...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            print("No se detectó audio.")
            return None
    try:
        texto = recognizer.recognize_google(audio, language="es-ES")
        print(f"Has dicho: {texto}")
        return texto
    except sr.UnknownValueError:
        print("No se entendió lo que dijiste.")
        return None
    except sr.RequestError as e:
        print(f"Error en el servicio de reconocimiento: {e}")
        return None

