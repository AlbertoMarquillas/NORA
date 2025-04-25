# Ficha Específica – `eventos_vision.py`

## Nombre del archivo:
`eventos_vision.py`

## Responsabilidad principal:
Definir, estructurar y emitir los eventos específicos generados por el módulo `vision/`. Establece un formato común para comunicar las detecciones realizadas (rostros, atención, postura, emociones, gestos) al resto del sistema de forma estandarizada.

## Entradas esperadas:
- Resultados de procesamiento visual provenientes de los submódulos (`deteccion_rostro.py`, `postura.py`, `emociones.py`, `gestos.py`, etc.).
- Parámetros de los eventos: tipo de evento, datos asociados (coordenadas, emoción detectada, nivel de atención, etc.).

## Salidas generadas:
- Emisión de eventos internos estructurados:
  - `EVT_FACE_DETECTED`
  - `EVT_ATTENTION_GAINED`
  - `EVT_POSTURE_ALERT`
  - `EVT_EMOTION_CHANGED`
  - `EVT_GESTURE_WAVE`, entre otros.

## Funcionalidades principales:
- Definición de constantes de eventos estándar del módulo `vision/`.
- Creación de estructuras de eventos enriquecidos (tipo, timestamp, payload de datos).
- Emisión de eventos hacia el `sistema/` y módulos receptores (`agentes/`, `interfaz/`, `datos/`).
- Opcionalmente, log de eventos relevantes para trazabilidad.

## Dependencias técnicas:
- `utils/gestion_eventos.py` – Utilidades de creación y emisión de eventos internos.
- `datetime` – Generación de timestamps para los eventos.
- `json` – Opcionalmente, serialización de payloads de eventos complejos.

