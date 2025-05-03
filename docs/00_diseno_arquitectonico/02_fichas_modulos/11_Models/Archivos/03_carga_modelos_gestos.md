# Ficha Funcional – `carga_modelos_gestos.py`

## Nombre del archivo:
`carga_modelos_gestos.py`

## Responsabilidad principal:
Gestionar la carga, inicialización y validación de los modelos de reconocimiento de gestos y signos utilizados por NORA. Incluye modelos basados en pose estimation, redes convolucionales o secuencias temporales (gestos dinámicos).

## Entradas esperadas:
- **Tipo de entrada:** Solicitudes de carga de modelos de gestos, parámetros de configuración, rutas de modelos.
- **Fuente:** `models_main.py`, `vision/`, `agentes/`.
- **Formato o protocolo:** Rutas a modelos preentrenados, configuraciones específicas de inferencia.

## Salidas generadas:
- **Tipo de salida:** Instancias de modelos de reconocimiento de gestos listos para uso.
- **Destinatario:** `vision/`, `agentes/`, `models_main.py`.
- **Ejemplo de salida:**
  - Modelo de reconocimiento de señales de mano cargado
  - Modelo de clasificador de gestos corporales inicializado

## Módulos relacionados:
- **Entrada desde:** `models_main.py`, `vision/`.
- **Salida hacia:** `vision/`, `agentes/`.
- **Comunicación bidireccional con:** `models_main.py` para seguimiento de modelos activos.

## Dependencias técnicas:
- **Librerías externas:** `TensorFlow`, `PyTorch`, `MediaPipe`, `OpenCV`, `numpy`.
- **Hardware gestionado:** GPU opcional para inferencia.
- **Protocolos:** Inferencia visual basada en pose keypoints o imágenes.

## Notas adicionales:
`carga_modelos_gestos.py` debe permitir cargar tanto modelos de gestos estáticos (basados en imagen única) como modelos de gestos dinámicos (basados en secuencias). También debe implementar verificaciones de compatibilidad entre la arquitectura del modelo y los datos de entrada esperados, asegurando un funcionamiento robusto en condiciones variadas de captura.

