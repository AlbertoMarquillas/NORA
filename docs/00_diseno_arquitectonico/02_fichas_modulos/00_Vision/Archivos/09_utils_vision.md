# Ficha Específica – `utils_vision.py`

## Nombre del archivo:
`utils_vision.py`

## Responsabilidad principal:
Proporcionar funciones auxiliares comunes para el módulo `vision/`, incluyendo operaciones de transformación de imágenes, normalización de datos visuales, cálculos geométricos sobre keypoints y métricas de evaluación de detecciones.

## Entradas esperadas:
- Imágenes o frames (BGR, RGB o Gray).
- Coordenadas o keypoints detectados.
- Parámetros de transformación o normalización.

## Salidas generadas:
- Imágenes transformadas.
- Coordenadas normalizadas o escaladas.
- Resultados de cálculos geométricos (distancias, ángulos, proporciones).
- Métricas evaluativas de precisión o confianza.

## Funcionalidades principales:
- Conversión de espacios de color (`BGR` ↔ `RGB` ↔ `Gray`).
- Redimensionado de imágenes preservando proporciones.
- Normalización de coordenadas de detección respecto al tamaño del frame.
- Cálculo de distancias euclidianas, ángulos entre puntos, proporciones relativas.
- Suavizado temporal de coordenadas para seguimiento más estable.
- Filtrado de detecciones ruidosas según umbrales configurables.

## Dependencias técnicas:
- `OpenCV` – Manipulación de imágenes y operaciones básicas.
- `NumPy` – Procesamiento matricial y cálculo de métricas.
- `math` – Cálculo de distancias, ángulos y funciones trigonométricas.

