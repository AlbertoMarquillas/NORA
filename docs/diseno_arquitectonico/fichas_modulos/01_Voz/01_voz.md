# Ficha Funcional – Módulo de Voz

## Nombre del módulo:
`voz/`

## Responsabilidad principal:
Gestiona la interacción auditiva del sistema NORA. Se encarga del reconocimiento automático del habla (ASR) para convertir voz en texto, la síntesis de voz (TTS) para convertir texto en salida de audio, el análisis emocional vocal, y la gestión del turno conversacional. Además, permite la detección de palabras clave y la interrupción de la respuesta vocal.

## Entradas esperadas:
- **Tipo de entrada:** Señal de audio, comandos de texto para síntesis, modulaciones emocionales.
- **Fuente:** Micrófono USB, `sistema/`, `dialogo/`, `agentes/`.
- **Formato o protocolo:** Stream de audio PCM, texto plano, eventos internos (`CMD_...`), comandos de activación como hotword.

## Salidas generadas:
- **Tipo de salida:** Texto reconocido, eventos semánticos, audio sintetizado.
- **Destinatario:** `dialogo/`, `sistema/`, `interfaz/`, hardware de audio.
- **Ejemplo de salida:**
  - `EVT_SPEECH_RECOGNIZED` (Texto transcrito del habla).
  - `EVT_COMMAND_PARSED` (Comando extraído del texto reconocido).
  - `EVT_WAKEWORD` (Detección de la palabra clave, como "oye NORA").
  - Stream de audio sintetizado, generado a partir de texto, enviado a salida sonora.

## Módulos relacionados:
- **Entrada desde:** `sensores/` (estado ambiental opcional), `sistema/` (activación), `gui/` (pruebas).
- **Salida hacia:** `dialogo/`, `interfaz/`, `sistema/`, `agentes/`.
- **Comunicación bidireccional con:** `dialogo/` (texto), `agentes/` (modulación de voz y emociones).

## Dependencias técnicas:
- **Librerías externas:** `vosk`, `whisper`, `pyttsx3`, `webrtcvad`, `pyaudio`, `numpy`, `scipy`.
- **Hardware gestionado:** Micrófono USB, salida de audio mediante jack o USB.
- **Protocolos:** PCM para captura y reproducción, eventos internos.

## Notas adicionales:
El módulo de voz permite la detección de hotword (“oye NORA”), interrupción de la síntesis (barge-in), análisis emocional básico en la voz y aprendizaje adaptativo del vocabulario. La salida TTS (síntesis de voz) puede ser modulada en tono y velocidad según emociones detectadas. Este módulo permite mejorar la interacción auditiva con el sistema y permite la interacción natural mediante voz, además de integrar análisis y modulación emocional.

## Archivos previstos del módulo:
Listado de archivos `.py` que se espera implementar dentro del directorio `voz/` para estructurar sus funcionalidades:

- **`voz_main.py`**: Orquestador general del módulo.
- **`asr.py`**: Reconocimiento automático del habla (ASR).
- **`tts.py`**: Síntesis de texto a voz (TTS).
- **`vad.py`**: Detección de actividad vocal y gestión del turno conversacional.
- **`emocion_audio.py`**: Análisis emocional basado en tono, ritmo y volumen.
- **`hotword.py`**: Detección de palabra clave (“oye NORA”).
- **`parser_comandos.py`**: Extracción estructurada de comandos desde el texto.
- **`eventos_voz.py`**: Emisión de eventos estándar del módulo de voz.
- **`utils_voz.py`**: Funciones auxiliares para normalización de audio, espectrogramas, etc.
- **`config_voz.py`**: Parámetros configurables del módulo (idioma, sensibilidad, motores de TTS).
- **`modelo_asr_loader.py`**: Carga de modelos de ASR personalizados o adaptativos.
- **`pipeline_audio.py`**: Pipeline de procesamiento auditivo en tiempo real.
- **`normalizacion_texto.py`**: Conversión lingüística y fonética del texto para mejorar el reconocimiento y síntesis.
- **`perfil_voz_usuario.py`**: Ajuste del sistema a características acústicas individuales del usuario.
- **`entrenamiento_adaptativo.py`**: Mejora progresiva del vocabulario mediante entrenamiento offline incremental.
- **`gestion_salida_tts.py`**: Gestión avanzada de la salida de voz sintetizada (modulación, control de interrupciones, colas de salida).
- **`variabilidad_prosodica.py`**: Variación dinámica de tono, velocidad y volumen en la voz sintetizada.
- **`interrupcion_semantica.py`**: Detección de interrupciones basadas en cambios semánticos durante la conversación.
- **`expresiones_vocales.py`**: Inserción de expresiones auditivas naturales (suspiros, risas) en la síntesis.
- **`motor_personalidad_voz.py`**: Selección y modulación de perfiles de voz con rasgos diferenciados.
- **`optimizacion_tts.py`**: Minimización de latencia en el sistema de síntesis de voz.
- **`config_voz.py`**: Parámetros configurables del módulo (idioma, motores TTS, sensibilidad).
- **`utils_voz.py`**: Funciones auxiliares de tratamiento de audio y texto.
