# Ficha Específica – `utils_activacion.py`

## Nombre del archivo:
`utils_activacion.py`

## Responsabilidad principal:
Proporcionar funciones auxiliares comunes para el módulo `activacion/`, apoyando operaciones como validación de eventos, gestión de debounce para entradas físicas (botón), y utilidades para control de lógica de activación.

## Entradas esperadas:
- Datos de eventos captados (tipo, fuente, timestamp).
- Señales físicas de entrada (GPIO).
- Parámetros de filtrado o validación.

## Salidas generadas:
- Eventos procesados y validados.
- Resultados de utilidades de filtrado o temporización.

## Funcionalidades principales:
- Validación de eventos de activación en base a configuraciones activas.
- Aplicación de debounce a señales de botones físicos.
- Normalización de timestamps de eventos.
- Gestión de temporizadores auxiliares para control de histéresis.
- Herramientas de soporte a `gestion_boton.py`, `decision_activacion.py` y otros submódulos.

## Dependencias técnicas:
- `time`, `datetime` – Control de tiempos y temporización.
- `gpiozero`, `RPi.GPIO` – Gestión de señales físicas.
- `json` – Formateo de resultados estructurados.

