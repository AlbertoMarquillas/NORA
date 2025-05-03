# Ficha Específica – `sensores_main.py`

## Nombre del archivo:
`sensores_main.py`

## Responsabilidad principal:
Actuar como coordinador central del módulo `sensores/`. Gestiona la inicialización de los sensores disponibles, programa su lectura periódica y emite eventos al sistema en función de las condiciones detectadas. Encapsula el ciclo de adquisición y distribución de datos sensoriales.

## Entradas esperadas:
- Configuraciones dinámicas de sensores (frecuencia, activación selectiva).
- Solicitudes de lectura puntual o activación/desactivación desde otros módulos (`sistema/`, `gui/`).

## Salidas generadas:
- Eventos de sensor interpretados (`EVT_PRESENCE_CONFIRMED`, `EVT_ENV_HOT`, `EVT_NFC_UID_DETECTED`, etc.).
- Logs opcionales de datos sensoriales.

## Funcionalidades principales:
- Detección y registro de sensores conectados (en base a configuración).
- Lanzamiento de hilos o tareas periódicas para cada tipo de sensor activo.
- Recolección y verificación de lecturas.
- Emisión de eventos contextualizados a partir de los datos físicos.
- Interfaz de diagnóstico para confirmar estado operativo de sensores.

## Dependencias técnicas:
- `threading`, `asyncio` – Gestión de lectura concurrente o asíncrona.
- Submódulos de sensores individuales.
- `config_sensores.py` – Frecuencia de lectura y umbrales definidos.
- `eventos_sensores.py` – Emisión de eventos normalizados.

