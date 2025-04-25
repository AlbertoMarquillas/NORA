# Ficha Específica – `deteccion_rostro.py`

## Nombre del archivo:
`deteccion_rostro.py`

## Responsabilidad principal:
Implementar las funciones encargadas de localizar rostros en las imágenes captadas por la cámara y, opcionalmente, realizar su seguimiento en tiempo real. Extrae coordenadas de bounding boxes que representan la presencia facial dentro del frame.

## Entradas esperadas:
- Frame de vídeo preprocesado (imagen BGR o Gray, tamaño configurable).
- Configuraciones dinámicas (modelo de detección activo, tamaño mínimo de rostro, sensibilidad).

## Salidas generadas:
- Coordenadas de detección facial: `(x, y, w, h)` para cada rostro identificado.
- Número de rostros detectados.
- Flags o métricas de calidad de detección (confianza, consistencia entre frames).

## Funcionalidades principales:
- Carga de modelo de detección facial (`Haar Cascade`, `DNN`, `MediaPipe Face Detection`, etc.).
- Localización de rostros en el frame actual.
- Filtrado de detecciones basado en tamaño, confianza o estabilidad.
- (Opcional) Seguimiento de posiciones faciales entre frames consecutivos.
- Adaptación de la resolución del frame para optimizar el rendimiento.
- Emisión de resultados al flujo de eventos de `vision_main.py`.

## Dependencias técnicas:
- `OpenCV` – Métodos de detección de objetos.
- `MediaPipe` – Detección avanzada de rostros (opcional).
- `NumPy` – Procesamiento matricial de coordenadas y bounding boxes.