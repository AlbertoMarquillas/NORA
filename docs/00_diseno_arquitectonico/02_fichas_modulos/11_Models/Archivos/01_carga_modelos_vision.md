# Ficha Funcional – `carga_modelos_vision.py`

## Nombre del archivo:
`carga_modelos_vision.py`

## Responsabilidad principal:
Gestionar la carga, inicialización y validación de los modelos de visión artificial utilizados por NORA. Incluye modelos de detección de objetos, reconocimiento facial, estimación de pose, análisis de emociones visuales y reconocimiento de gestos.

## Entradas esperadas:
- **Tipo de entrada:** Solicitudes de carga de modelos de visión, parámetros de inicialización, rutas de modelos.
- **Fuente:** `models_main.py`, `vision/`, `agentes/`.
- **Formato o protocolo:** Rutas de archivos de modelo, configuraciones específicas de carga.

## Salidas generadas:
- **Tipo de salida:** Instancias de modelos de visión listos para inferencia.
- **Destinatario:** `vision/`, `agentes/`, `models_main.py`.
- **Ejemplo de salida:**
  - Cargado modelo YOLOv5 para detección de objetos
  - Inicializado modelo de emociones faciales

## Módulos relacionados:
- **Entrada desde:** `models_main.py`, `vision/`.
- **Salida hacia:** `vision/`, `agentes/`.
- **Comunicación bidireccional con:** `models_main.py` para control de estado de carga.

## Dependencias técnicas:
- **Librerías externas:** `TensorFlow`, `PyTorch`, `OpenCV`, `MediaPipe`, `numpy`, `torchvision`.
- **Hardware gestionado:** GPU opcional para aceleración.
- **Protocolos:** Inferencia de modelos de visión.

## Notas adicionales:
`carga_modelos_vision.py` debe ser capaz de cargar diferentes arquitecturas de modelos (CNNs, pose estimators, object detectors) y aplicar optimizaciones como conversión a formatos ligeros (`.tflite`, `ONNX`) si es necesario. Además, debe incluir mecanismos de verificación post-carga para garantizar que el modelo esté listo para recibir datos de entrada reales.

