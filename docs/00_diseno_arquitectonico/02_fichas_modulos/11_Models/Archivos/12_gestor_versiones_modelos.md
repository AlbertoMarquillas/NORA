# Ficha Funcional – `gestor_versiones_modelos.py`

## Nombre del archivo:
`gestor_versiones_modelos.py`

## Responsabilidad principal:
Gestionar las versiones de los modelos de inteligencia artificial utilizados en NORA, permitiendo la identificación, seguimiento y recuperación segura de versiones anteriores de cada modelo. Facilita el control de actualizaciones y el rollback en caso de errores.

## Entradas esperadas:
- **Tipo de entrada:** Metadatos de modelos, identificadores de versiones, solicitudes de rollback o activación de versiones.
- **Fuente:** `models_main.py`, `actualizacion_remota_modelos.py`, `agentes/`.
- **Formato o protocolo:** Archivos de metadatos (JSON/YAML), estructuras de versiones.

## Salidas generadas:
- **Tipo de salida:** Modelos activados, reportes de gestión de versiones, alertas de inconsistencias.
- **Destinatario:** `models_main.py`, `agentes/`, `datos/`.
- **Ejemplo de salida:**
  - Activación de versión anterior estable del modelo de voz
  - Registro de nueva versión de modelo de visión

## Módulos relacionados:
- **Entrada desde:** `models_main.py`, `actualizacion_remota_modelos.py`, `agentes/`.
- **Salida hacia:** `models_main.py`, `agentes/`, `datos/`.
- **Comunicación bidireccional con:** `models_main.py` para actualización de referencias activas.

## Dependencias técnicas:
- **Librerías externas:** `os`, `json`, `yaml`, `shutil`, `logging`.
- **Hardware gestionado:** Almacenamiento de versiones en el sistema de archivos.
- **Protocolos:** Gestión de carpetas de versiones y archivos de control.

## Notas adicionales:
`gestor_versiones_modelos.py` debe garantizar una estructura ordenada de almacenamiento de modelos por versión, permitiendo operaciones atómicas de activación/cambio de versión y manteniendo siempre disponible una versión estable anterior en caso de fallos. Su correcta operación es crucial para la resiliencia y trazabilidad de la inteligencia de NORA.

