# Ficha Específica – `modelo_loader.py`

## Nombre del archivo:
`modelo_loader.py`

## Responsabilidad principal:
Gestionar la carga, inicialización y configuración de los modelos de inteligencia artificial utilizados dentro del módulo `vision/`. Centraliza el proceso de selección, preparación y disponibilización de modelos de detección facial, análisis emocional, postura y atención.

## Entradas esperadas:
- Peticiones de carga de modelo específico (`tipo_modelo`, `ruta_modelo`, `parámetros de configuración`).
- Configuraciones dinámicas de operación (modo de detección, optimizaciones activas).

## Salidas generadas:
- Modelos de IA cargados en memoria, listos para su uso por los submódulos (`deteccion_rostro.py`, `emociones.py`, `postura.py`, etc.).
- Información de estado de carga y disponibilidad de cada modelo.

## Funcionalidades principales:
- Carga de modelos de IA desde archivos locales (`.pb`, `.tflite`, `.onnx`, etc.).
- Inicialización de sesiones de inferencia (TensorFlow, PyTorch o equivalente).
- Verificación de la integridad de los modelos antes de su activación.
- Gestión de múltiples versiones o configuraciones de modelos según tipo de tarea.
- Exposición de referencias a los modelos para ser utilizados por el resto de submódulos.

## Dependencias técnicas:
- `TensorFlow`, `TensorFlow Lite`, `PyTorch` o librerías equivalentes de inferencia.
- `NumPy` – Preprocesamiento y preparación de tensores.
- `os`, `pathlib` – Manejo de rutas de archivos de modelos.

