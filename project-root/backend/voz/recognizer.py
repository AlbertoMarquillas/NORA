# backend/voz/recognizer.py

import speech_recognition as sr

def escuchar_frase():
    """
    Escucha una frase por micrófono y devuelve el texto reconocido.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = recognizer.listen(source)
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
