# Ficha Específica – `vision_main.py`

## Nombre del archivo:
`vision_main.py`

## Responsabilidad principal:
Coordinar el flujo general del módulo `vision/`. Inicializa los submódulos de procesamiento (detección de rostro, postura, atención, emociones, gestos), gestiona la captura de frames desde la cámara y organiza el procesamiento por etapas. Se encarga de recibir eventos de activación o consulta, ejecutar el pipeline de procesamiento visual y emitir los eventos de salida correspondientes.

## Entradas esperadas:
- Flujo de frames en tiempo real desde la cámara (CSI o USB).
- Eventos internos solicitando procesamiento (`EVT_ANALYZE_FRAME`, `EVT_CHECK_ATTENTION`, etc.).
- Configuraciones dinámicas (`JSON` de parámetros de operación: FPS, resolución, detecciones activas).

## Salidas generadas:
- Eventos perceptivos generados (`EVT_FACE_DETECTED`, `EVT_ATTENTION_GAINED`, `EVT_POSTURE_ALERT`, etc.).
- Información procesada y normalizada para consumo de `agentes/`, `interfaz/`, `sistema/`.

## Funcionalidades principales:
- Captura y configuración de la fuente de vídeo (`OpenCV VideoCapture`).
- Gestión del ciclo principal de procesamiento por frame (`loop_frame_processing()`).
- Llamadas secuenciales a los submódulos (`deteccion_rostro.py`, `postura.py`, `atencion_visual.py`, etc.).
- Emisión de eventos internos basados en los resultados de procesamiento.
- Gestión de errores de captura o procesamiento (desconexión de cámara, frames inválidos).
- Respuesta a eventos externos de activación o reconfiguración.

## Dependencias técnicas:
- `OpenCV` para captura y preprocesamiento de frames.
- `asyncio` (opcional) para gestión no bloqueante del ciclo de procesamiento.
- Llamadas a funciones de los submódulos específicos de `vision/`.

