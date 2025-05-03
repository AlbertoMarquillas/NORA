# Ficha Específica – `config_activacion.py`

## Nombre del archivo:
`config_activacion.py`

## Responsabilidad principal:
Centralizar todos los parámetros configurables del módulo `activacion/`, incluyendo tiempos de espera, prioridades entre fuentes de activación, modo no molestar, y control de sensibilidad de detección.

## Entradas esperadas:
- Configuraciones por defecto definidas en el archivo.
- Opcionalmente, sobrescritura de configuraciones mediante entrada dinámica (`JSON`, `YAML`).

## Salidas generadas:
- Acceso estructurado a las configuraciones activas del módulo `activacion/`.
- Parámetros actualizados accesibles por submódulos.

## Funcionalidades principales:
- Definición de:
  - Tiempos de histéresis y activación mínima.
  - Priorización entre fuentes de activación (voz, visión, presencia, NFC, botón).
  - Configuración del modo no molestar (duración, bloqueo de fuentes).
  - Umbrales de validación de activaciones múltiples.
- Validación de configuraciones cargadas.
- Actualización dinámica de parámetros si se requiere.

## Dependencias técnicas:
- `json`, `yaml` – Lectura y carga de configuraciones.
- `os`, `pathlib` – Gestión de rutas a archivos de configuración.
- `copy` – Clonación segura de configuraciones en memoria.

