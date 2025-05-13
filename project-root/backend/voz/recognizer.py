import speech_recognition as sr

def escuchar_frase():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 200  # 🔧 Baja el umbral para detectar voz débil
    recognizer.pause_threshold = 0.8   # 🔧 Más sensible a pausas

    print("Micrófonos detectados:")
    for i, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"[{i}] {name}")

    with sr.Microphone(device_index=1) as source:  # Usa tu entrada MIC ADC
        print("Escuchando...")
        # NO ajustar al ruido porque te puede poner el threshold por las nubes
        # recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            print("No se detectó audio.")
            return None

    try:
        print("Procesando...")
        texto = recognizer.recognize_google(audio, language="es-ES")
        print(f"Has dicho: {texto}")
        return texto
    except sr.UnknownValueError:
        print("No se entendió lo que dijiste.")
        return None
    except sr.RequestError as e:
        print(f"Error en el servicio de reconocimiento: {e}")
        return None
