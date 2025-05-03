# Ficha Específica – `verificacion_calidad.py`

## Nombre del archivo:
`verificacion_calidad.py`

## Responsabilidad principal:
Comprobar que las condiciones de la imagen captada cumplen unos requisitos mínimos de calidad (iluminación suficiente, ausencia de obstrucciones, foco aceptable) para permitir un procesamiento visual fiable en el módulo `vision/`.

## Entradas esperadas:
- Frame de vídeo preprocesado (imagen BGR o Gray).
- Parámetros de umbrales configurables (luminosidad mínima, porcentaje de obstrucción tolerable, métricas de nitidez).

## Salidas generadas:
- Indicador de calidad de imagen: `aceptable` o `inaceptable`.
- Métricas específicas de evaluación:
  - Nivel de luminosidad promedio.
  - Nivel de desenfoque.
  - Porcentaje de área cubierta/oscurecida.
- Eventos opcionales:
  - `EVT_IMAGE_QUALITY_POOR`

## Funcionalidades principales:
- Cálculo de histograma de brillo y media de luminancia.
- Detección de desenfoque mediante estimación de gradientes (varianza de Laplaciano).
- Detección de áreas oscuras u obstrucciones importantes.
- Emisión de advertencias internas si la calidad cae por debajo de los umbrales.
- Sugerencia opcional de reconfiguración de parámetros de cámara si es necesario.

## Dependencias técnicas:
- `OpenCV` – Análisis de histograma, cálculo de desenfoque.
- `NumPy` – Procesamiento de datos matriciales y cálculos estadísticos.

