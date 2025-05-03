# Ficha Específica – `config_vision.py`

## Nombre del archivo:
`config_vision.py`

## Responsabilidad principal:
Centralizar todos los parámetros configurables relacionados con el módulo `vision/`, incluyendo configuraciones de captura de vídeo, opciones de procesamiento, sensibilidad de detección y rutas a los modelos de IA.

## Entradas esperadas:
- Parámetros por defecto definidos en el archivo.
- Opcionalmente, sobrescritura de parámetros a través de configuración dinámica (`JSON` o `YAML`).

## Salidas generadas:
- Estructura de configuración accesible por todos los submódulos de `vision/`.
- Parámetros actualizados en tiempo de ejecución si se reciben configuraciones externas.

## Funcionalidades principales:
- Definición de:
  - Resolución de captura de vídeo.
  - FPS objetivo de procesamiento.
  - ROI (Región de Interés) para análisis localizado.
  - Sensibilidad de detecciones (rostro, atención, postura, emociones, gestos).
  - Rutas relativas o absolutas a modelos de IA utilizados.
- Posibilidad de actualizar configuraciones durante la operación.
- Validación de parámetros para prevenir configuraciones inconsistentes.

## Dependencias técnicas:
- `json` o `yaml` – Lectura de configuraciones externas.
- `os` o `pathlib` – Gestión de rutas de archivos.
- `copy` – Clonación de estructuras de configuración base para seguridad.