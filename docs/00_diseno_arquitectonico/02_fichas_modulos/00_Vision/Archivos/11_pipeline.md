# Ficha Específica – `pipeline.py`

## Nombre del archivo:
`pipeline.py`

## Responsabilidad principal:
Definir y coordinar el flujo secuencial de procesamiento visual que se aplica a cada frame capturado en el módulo `vision/`. Gestiona la ejecución ordenada de las funciones especializadas de detección, análisis y generación de eventos perceptivos.

## Entradas esperadas:
- Frame de vídeo preprocesado (imagen BGR o RGB).
- Parámetros de configuración activa (`config_vision.py`).
- Referencias a modelos y submódulos cargados (`modelo_loader.py`).

## Salidas generadas:
- Resultados individuales de cada etapa de procesamiento (detección de rostro, análisis de atención, postura, emociones, gestos).
- Eventos internos generados por `eventos_vision.py` en función de los resultados obtenidos.

## Funcionalidades principales:
- Orquestación secuencial de:
  - Detección de rostros.
  - Estimación de atención visual.
  - Análisis de postura corporal.
  - Análisis de expresiones emocionales.
  - Detección de gestos simbólicos.
- Aplicación de configuraciones dinámicas para activar o desactivar fases del pipeline.
- Manejo de resultados parciales y su consolidación.
- Emisión de eventos al finalizar el procesamiento de cada frame.
- Gestión de errores o resultados incompletos durante el flujo.

## Dependencias técnicas:
- `utils_vision.py` – Funciones auxiliares de normalización y transformación de datos.
- Submódulos de procesamiento específicos (`deteccion_rostro.py`, `postura.py`, `atencion_visual.py`, `emociones.py`, `gestos.py`).
- `eventos_vision.py` – Emisión de eventos internos.

