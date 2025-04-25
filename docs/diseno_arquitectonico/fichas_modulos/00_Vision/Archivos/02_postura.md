# Ficha Específica – `postura.py`

## Nombre del archivo:
`postura.py`

## Responsabilidad principal:
Analizar las posiciones relativas del cuerpo a partir de la imagen captada para estimar el estado postural básico del usuario. Detecta posturas como erguido, encorvado o inactivo, generando eventos contextuales que informan sobre la condición física y de atención del usuario.

## Entradas esperadas:
- Frame de vídeo preprocesado (imagen BGR o RGB).
- Puntos clave del cuerpo (keypoints) generados por modelos de pose estimation.
- Configuraciones dinámicas (sensibilidad a cambios de postura, umbrales de alerta).

## Salidas generadas:
- Estado postural clasificado: `erguido`, `encorvado`, `inactivo`.
- Coordenadas principales del cuerpo (hombros, caderas, cabeza).
- Eventos asociados:
  - `EVT_POSTURE_STATUS`

## Funcionalidades principales:
- Detección de puntos clave del cuerpo mediante modelos de `MediaPipe Pose` u otros equivalentes.
- Cálculo de ángulos de inclinación y relación entre ejes corporales.
- Clasificación del estado postural según reglas definidas (umbral de inclinación, distancias verticales).
- Filtrado de ruido y gestión de detecciones inestables entre frames.
- Emisión de eventos internos indicando cambios de postura relevantes.

## Dependencias técnicas:
- `OpenCV` – Procesamiento de imágenes.
- `MediaPipe` – Estimación de poses humanas.
- `NumPy` – Cálculo de distancias, vectores y ángulos.