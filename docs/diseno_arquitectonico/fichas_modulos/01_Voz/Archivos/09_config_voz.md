# Ficha Específica – `config_voz.py`

## Nombre del archivo:
`config_voz.py`

## Responsabilidad principal:
Centralizar todos los parámetros configurables relacionados con el módulo `voz/`, incluyendo configuraciones de ASR, TTS, hotword detection y gestión de sensibilidad de audio.

## Entradas esperadas:
- Parámetros definidos por defecto en el archivo.
- Configuraciones dinámicas de entrada externa (archivos JSON/YAML).

## Salidas generadas:
- Acceso estructurado a configuraciones activas por parte de todos los submódulos de `voz/`.
- Actualización dinámica de parámetros durante la operación.

## Funcionalidades principales:
- Definición de:
  - Sensibilidad de detección de voz y hotword.
  - Idioma activo del ASR y TTS.
  - Selección de modelo de ASR preferido.
  - Velocidad, tono y estilo de voz para TTS.
  - Umbrales de actividad vocal.
- Validación de configuraciones cargadas.
- Sobrescritura segura de parámetros en tiempo de ejecución.

## Dependencias técnicas:
- `json`, `yaml` – Lectura y carga de configuraciones dinámicas.
- `os`, `pathlib` – Gestión de rutas a recursos de audio y modelos.
- `copy` – Clonación de configuraciones base para seguridad.

