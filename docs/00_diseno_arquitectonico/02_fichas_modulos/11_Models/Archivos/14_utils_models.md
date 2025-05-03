# Ficha Funcional – `utils_models.py`

## Nombre del archivo:
`utils_models.py`

## Responsabilidad principal:
Proporcionar funciones auxiliares y utilidades de soporte para el módulo `models/` de NORA. Incluye herramientas para carga de modelos, preprocesamiento de datos de entrada, ejecución estandarizada de inferencias, y manipulaciones de tensores o embeddings.

## Entradas esperadas:
- **Tipo de entrada:** Solicitudes internas de submódulos de `models/`, datos de entrada para inferencia o preprocesamiento.
- **Fuente:** `models_main.py`, submódulos de carga, `gestion_embeddings.py`, `gestion_fine_tuning.py`.
- **Formato o protocolo:** Tensores, matrices de características, rutas de modelos.

## Salidas generadas:
- **Tipo de salida:** Modelos cargados, datos preprocesados, inferencias ejecutadas, embeddings generados.
- **Destinatario:** Submódulos de `models/`, `vision/`, `voz/`, `dialogo/`, `datos/`.
- **Ejemplo de salida:**
  - Normalización de entrada de imagen
  - Inferencia estandarizada con manejo de excepciones
  - Carga segura de modelo desde archivo

## Módulos relacionados:
- **Entrada desde:** `models_main.py`, `carga_modelos_*`, `gestion_embeddings.py`, `gestion_fine_tuning.py`.
- **Salida hacia:** Submódulos de `models/`, `vision/`, `voz/`, `dialogo/`, `datos/`.
- **Comunicación bidireccional con:** Ninguna (utilidades de soporte).

## Dependencias técnicas:
- **Librerías externas:** `TensorFlow`, `PyTorch`, `OpenCV`, `numpy`, `scikit-learn`, `joblib`.
- **Hardware gestionado:** Indirectamente CPU o GPU (a través de frameworks de inferencia).
- **Protocolos:** Interno de manipulación de datos y modelos.

## Notas adicionales:
`utils_models.py` centraliza las operaciones comunes necesarias para facilitar la modularidad, la robustez y la eficiencia del sistema de modelos de NORA. Debe ser altamente confiable, incluyendo manejo de errores, validaciones de formato de entrada y opciones de logging para operaciones críticas de inferencia o carga de datos.

