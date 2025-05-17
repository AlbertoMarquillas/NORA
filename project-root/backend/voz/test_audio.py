import speech_recognition as sr

print("Micrófonos disponibles:")
for i, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"  [{i}] {name}")

try:
    mic_index = int(input("Selecciona el índice del micro que quieres usar: "))
    recognizer = sr.Recognizer()

    with sr.Microphone(device_index=mic_index) as source:
        print("🎧 Habla algo (5 segundos)...")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        print("✅ Audio capturado. Intentando reconocer...")

        text = recognizer.recognize_google(audio, language="es-ES")
        print(f"📝 Frase reconocida: {text}")
except Exception as e:
    print(f"❌ Error: {e}")
