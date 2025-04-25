# Ficha Específica – `eventos_voz.py`

## Nombre del archivo:
`eventos_voz.py`

## Responsabilidad principal:
Definir, estructurar y emitir los eventos específicos generados por el módulo `voz/`. Permite una comunicación estandarizada y coherente entre el procesamiento de voz y el resto del sistema NORA.

## Entradas esperadas:
- Resultados de submódulos de `voz/` (ASR, TTS, VAD, hotword, análisis emocional).
- Parámetros para la generación de eventos (tipo de evento, datos asociados).

## Salidas generadas:
- Emisión de eventos estructurados:
  - `EVT_SPEECH_RECOGNIZED`
  - `EVT_COMMAND_PARSED`
  - `EVT_WAKEWORD_DETECTED`
  - `EVT_EMOTION_AUDIO_ANALYZED`

## Funcionalidades principales:
- Definición de constantes de eventos estándar para el módulo `voz/`.
- Creación de estructuras enriquecidas para los eventos (tipo, timestamp, payload de datos).
- Emisión de eventos hacia `sistema/`, `dialogo/`, `interfaz/`, `agentes/`.
- Registro opcional de eventos relevantes para trazabilidad.

## Dependencias técnicas:
- `utils/gestion_eventos.py` – Creación y emisión de eventos internos.
- `datetime` – Generación de timestamps.
- `json` – Serialización de payloads complejos.

