# Ficha Funcional – Módulo de Voz

## Nombre del módulo:
`voz/`

## Responsabilidad principal:
Gestiona la interacción auditiva del sistema NORA. Se encarga del reconocimiento automático del habla (ASR) para convertir voz en texto, y de la síntesis de voz (TTS) para convertir texto en salida de audio, incluyendo análisis emocional vocal y gestión del turno conversacional.

## Entradas esperadas:
- Tipo de entrada: señal de audio, comandos de texto para síntesis, modulaciones emocionales
- Fuente: micrófono USB, `sistema/`, `dialogo/`, `agentes/`
- Formato o protocolo: stream de audio PCM, texto plano, eventos internos (`CMD_...`)

## Salidas generadas:
- Tipo de salida: texto reconocido, eventos semánticos, audio sintetizado
- Destinatario: `dialogo/`, `sistema/`, `interfaz/`, hardware de audio
- Ejemplo de salida:
  - `EVT_SPEECH_RECOGNIZED` (texto transcrito)
  - `EVT_COMMAND_PARSED` (comando extraído)
  - Stream de audio sintetizado enviado a salida sonora

## Módulos relacionados:
- Entrada desde: `sensores/` (estado ambiental opcional), `sistema/` (activación), `gui/` (pruebas)
- Salida hacia: `dialogo/`, `interfaz/`, `sistema/`, `agentes/`
- Comunicación bidireccional con: `dialogo/` (texto), `agentes/` (modulación de voz y emociones)

## Dependencias técnicas:
- Librerías externas: `vosk`, `whisper`, `pyttsx3`, `webrtcvad`, `pyaudio`, `numpy`, `scipy`
- Hardware gestionado: micrófono USB, altavoz o salida de audio jack/USB
- Protocolos: PCM para captura y reproducción, eventos internos

## Notas adicionales:
Permite hotword detection (“oye NORA”), interrupción de síntesis (barge-in), análisis emocional básico en voz, y aprendizaje adaptativo del vocabulario. La salida TTS puede ser modulada en tono y velocidad según emociones detectadas.

## Archivos previstos del módulo:
Listado de archivos `.py` que se espera implementar dentro del directorio `voz/` para estructurar sus funcionalidades.

- `voz_main.py`: Orquestador general del módulo.
- `asr.py`: Reconocimiento automático del habla.
- `tts.py`: Síntesis de texto a voz.
- `vad.py`: Detección de actividad vocal y gestión del turno conversacional.
- `emocion_audio.py`: Análisis emocional basado en características acústicas.
- `hotword.py`: Detección de palabra clave (“oye NORA”).
- `parser_comandos.py`: Parsing y extracción de comandos desde texto reconocido.
- `normalizacion_texto.py`: Conversión fonética y lingüística previa a la síntesis.
- `perfil_voz_usuario.py`: Ajuste acústico del reconocimiento a voces individuales.
- `entrenamiento_adaptativo.py`: Aprendizaje progresivo de vocabulario y patrones.
- `eventos_voz.py`: Definición y publicación de eventos auditivos.
- `pipeline_audio.py`: Flujo de procesamiento coordinado de entrada y salida de audio.
- `gestion_salida_tts.py`: Gestión avanzada de la salida de voz sintetizada (modulación, control de interrupciones, colas de salida).
- `variabilidad_prosodica.py`: Variación dinámica de tono, velocidad y volumen en la voz sintetizada.
- `interrupcion_semantica.py`: Detección de interrupciones basadas en cambios semánticos durante la conversación.
- `expresiones_vocales.py`: Inserción de expresiones auditivas naturales (suspiros, risas) en la síntesis.
- `motor_personalidad_voz.py`: Selección y modulación de perfiles de voz con rasgos diferenciados.
- `optimizacion_tts.py`: Minimización de latencia en el sistema de síntesis de voz.
- `config_voz.py`: Parámetros configurables del módulo (idioma, motores TTS, sensibilidad).
- `utils_voz.py`: Funciones auxiliares de tratamiento de audio y texto.