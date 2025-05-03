# Ficha Funcional – `normalizacion_texto.py`

## Nombre del archivo:
`normalizacion_texto.py`

## Responsabilidad principal:
Gestionar la conversión lingüística y fonética del texto para mejorar el reconocimiento y la síntesis de voz dentro del sistema NORA. Este archivo se encarga de normalizar el texto antes de que pase por el ASR (Reconocimiento Automático del Habla) y el TTS (Síntesis de Voz), corrigiendo errores de ortografía, variaciones fonéticas, y adaptando el texto a un formato más adecuado para su procesamiento.

## Entradas esperadas:
- **Tipo de entrada:** Texto en bruto, texto transcrito desde el ASR, comandos o consultas de texto.
- **Fuente:** `asr.py` (texto transcrito desde la señal de audio), `voz_main.py` (texto recibido para procesamiento de síntesis de voz).
- **Formato o protocolo:** Texto plano, eventos internos (`CMD_NORMALIZE_TEXT`).

## Salidas generadas:
- **Tipo de salida:** Texto normalizado, ajustado para mejorar la precisión en el ASR y TTS.
- **Destinatario:** `asr.py` (para mejorar la transcripción de la voz), `tts.py` (para mejorar la síntesis de voz).
- **Ejemplo de salida:**
  - `EVT_TEXT_NORMALIZED` (Evento que indica que el texto ha sido normalizado).
  - `CMD_NORMALIZE_TEXT` (Instrucción para normalizar el texto antes de pasarlo al ASR o TTS).
  - `AGT_NORMALIZED_TEXT` (Texto que ha sido procesado y corregido).

## Módulos relacionados:
- **Entrada desde:** `asr.py` (para recibir texto transcrito desde la señal de audio), `voz_main.py` (para recibir texto para la síntesis de voz).
- **Salida hacia:** `asr.py`, `tts.py` (para enviar el texto corregido y mejorado para su procesamiento).
- **Comunicación bidireccional con:** `sistema/`, `agentes/` para asegurar que el texto se procese correctamente y que sea coherente con las respuestas del sistema.

## Dependencias técnicas:
- **Librerías externas:** `nltk`, `spacy` (para el procesamiento de texto natural y la normalización), `unidecode` (para eliminar acentos y caracteres especiales).
- **Hardware gestionado:** Ninguno directamente (se maneja el texto y la fonética a nivel lógico).
- **Protocolos:** Comunicación basada en eventos internos, procesamiento y corrección de texto.

## Notas adicionales:
Este archivo es clave para mejorar la precisión de las respuestas de NORA tanto en el reconocimiento de voz (ASR) como en la síntesis de voz (TTS). La normalización del texto garantiza que el sistema pueda manejar variaciones en la ortografía o errores comunes, haciendo que el sistema sea más robusto frente a distintas formas de expresar un mismo contenido. Al aplicar esta normalización antes de pasar por ASR y TTS, se mejora la interacción del usuario con el sistema.

## Archivos previstos del módulo:
- `normalizacion_texto.py`: Conversión lingüística y fonética del texto para mejorar reconocimiento y síntesis (este archivo).
- Archivos adicionales como `asr.py`, `tts.py`, `voz_main.py`.
