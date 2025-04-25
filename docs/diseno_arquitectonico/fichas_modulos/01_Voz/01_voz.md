# Ficha Funcional – Módulo de Voz

## Nombre del módulo:
`voz/`

## Responsabilidad principal:
Gestiona la interacción auditiva del sistema. Incluye el reconocimiento automático del habla (ASR), la síntesis de voz (TTS), el análisis emocional vocal y la gestión del turno conversacional. Es uno de los canales sensoriales y expresivos principales de NORA.

## Entradas esperadas:
- Tipo de entrada: señal de audio
- Fuente: micrófono USB
- Formato o protocolo: stream de audio PCM capturado mediante `pyaudio` o `sounddevice`, eventos de control y configuración en JSON

## Salidas generadas:
- Tipo de salida: texto, eventos semánticos, audio sintetizado
- Destinatario: `dialogo/`, `sistema/`, `interfaz/`, `agentes/`
- Ejemplo de salida:
  - Texto transcrito (`"qué hora es"`)
  - `EVT_SPEECH_RECOGNIZED`, `EVT_COMMAND_PARSED`, `EVT_WAKEWORD`
  - Salida de voz generada (`.wav` en RAM o stream de audio directo)

## Módulos relacionados:
- Entrada desde: `sensores/` (estado ambiental opcional), `sistema/` (activación), `gui/` (pruebas)
- Salida hacia: `dialogo/`, `interfaz/`, `sistema/`, `agentes/`
- Comunicación bidireccional con: `dialogo/` (texto), `agentes/` (modulación de voz y emociones)

## Dependencias técnicas:
- Librerías externas: `vosk`, `whisper`, `pyttsx3`, `webrtcvad`, `pyaudio`, `numpy`, `scipy`
- Hardware gestionado: micrófono USB, salida de audio vía jack o USB
- Protocolos: audio PCM, eventos internos, reproducción local (TTS)

## Notas adicionales:
Permite barge-in (interrupción de respuesta por voz), hotword (“oye NORA”), y aprendizaje progresivo del vocabulario del usuario. Puede delegar funciones como análisis emocional o detección de interrupciones a agentes especializados.

## Archivos previstos del módulo:
Listado de archivos `.py` que se espera implementar dentro del directorio `voz/` para estructurar sus funcionalidades.

- `voz_main.py`: Orquestador general del módulo.
- `asr.py`: Reconocimiento automático del habla.
- `tts.py`: Síntesis de voz.
- `vad.py`: Detección de actividad vocal y gestión del turno conversacional.
- `emocion_audio.py`: Análisis emocional basado en tono, ritmo y volumen.
- `hotword.py`: Detección de palabra clave (“oye NORA”).
- `parser_comandos.py`: Extracción estructurada de comandos desde el texto.
- `eventos_voz.py`: Emisión de eventos estándar del módulo.
- `utils_voz.py`: Funciones auxiliares para normalización de audio, espectrogramas, etc.
- `config_voz.py`: Parámetros configurables del módulo (idioma, sensibilidad, motores de TTS).
- `modelo_asr_loader.py`: Carga de modelos de ASR personalizados o adaptativos.
- `pipeline_audio.py`: Pipeline de procesamiento auditivo en tiempo real.
- `normalizacion_texto.py`: Conversión lingüística y fonética del texto para mejorar reconocimiento y síntesis.
- `perfil_voz_usuario.py`: Ajuste del sistema a características acústicas individuales del usuario.
- `entrenamiento_adaptativo.py`: Mejora progresiva del vocabulario mediante entrenamiento offline incremental.