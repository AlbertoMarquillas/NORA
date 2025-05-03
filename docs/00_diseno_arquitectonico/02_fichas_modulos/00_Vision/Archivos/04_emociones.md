# Ficha Específica – `emociones.py`

## Nombre del archivo:
`emociones.py`

## Responsabilidad principal:
Analizar las expresiones faciales captadas en el vídeo para inferir el estado emocional del usuario. Clasifica emociones básicas como alegría, tristeza, enfado, sorpresa, neutralidad, y genera eventos que enriquecen el contexto perceptivo de NORA.

## Entradas esperadas:
- Frame de vídeo preprocesado (imagen BGR o RGB).
- Coordenadas faciales `(x, y, w, h)` de la región de interés.
- Keypoints faciales (opcionalmente, landmarks específicos).
- Configuraciones dinámicas (modelo de emociones activo, sensibilidad a cambios emocionales).

## Salidas generadas:
- Emoción detectada: `feliz`, `triste`, `enfadado`, `sorprendido`, `neutral`.
- Nivel de confianza en la clasificación.
- Eventos asociados:
  - `EVT_EMOTION_CHANGED`

## Funcionalidades principales:
- Recorte y normalización de la región facial detectada.
- Aplicación de modelo de clasificación de emociones entrenado sobre imágenes faciales.
- Evaluación de la emoción dominante en la imagen actual.
- Suavizado temporal de detecciones para evitar cambios erráticos.
- Emisión de eventos internos indicando cambios significativos de estado emocional.

## Dependencias técnicas:
- `OpenCV` – Procesamiento de imágenes.
- `TensorFlow` o `PyTorch` – Carga y ejecución del modelo de clasificación de emociones.
- `NumPy` – Preprocesamiento de datos y manejo de resultados.