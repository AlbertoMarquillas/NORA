# Ficha Específica – `atencion_visual.py`

## Nombre del archivo:
`atencion_visual.py`

## Responsabilidad principal:
Detectar y evaluar el nivel de atención visual del usuario en función de la dirección de su mirada, posición facial relativa y presencia en el campo visual. Determina si el usuario está prestando atención activa al sistema NORA.

## Entradas esperadas:
- Frame de vídeo preprocesado (imagen BGR o RGB).
- Coordenadas de la detección facial `(x, y, w, h)`.
- Puntos clave de ojos (keypoints faciales) si están disponibles.
- Configuraciones dinámicas (sensibilidad a desvíos de atención, duración mínima de atención).

## Salidas generadas:
- Estado de atención: `atento`, `desviado`, `ausente`.
- Eventos asociados:
  - `EVT_ATTENTION_GAINED`
  - `EVT_ATTENTION_LOST`

## Funcionalidades principales:
- Cálculo de la orientación aproximada de la cabeza respecto al centro de la imagen.
- Análisis de la posición de los ojos dentro del rostro detectado (cuando se dispone de keypoints).
- Determinación de presencia visual activa en base a umbrales angulares o de desviación.
- Gestión de tiempos de atención mantenida para confirmar atención real.
- Emisión de eventos internos ante cambios de estado de atención.

## Dependencias técnicas:
- `OpenCV` – Procesamiento de imágenes.
- `MediaPipe` – Detección de landmarks faciales.
- `NumPy` – Cálculo de vectores y desviaciones angulares.

