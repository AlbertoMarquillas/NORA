# Ficha Específica – `eventos_activacion.py`

## Nombre del archivo:
`eventos_activacion.py`

## Responsabilidad principal:
Definir, estructurar y emitir los eventos internos generados por el módulo `activacion/`, estandarizando la comunicación de activaciones, denegaciones y cambios de estado hacia el resto del sistema.

## Entradas esperadas:
- Resultados de evaluación de fuentes de activación.
- Parámetros de eventos (tipo de activación, motivo, datos asociados).

## Salidas generadas:
- Emisión de eventos de activación estandarizados:
  - `EVT_ACTIVATION_CONFIRMED`
  - `EVT_ACTIVATION_DENIED`
  - `EVT_REST_MODE_TRIGGERED`
  - `EVT_NO_MOLESTAR_ACTIVADO`
  - `EVT_NO_MOLESTAR_DESACTIVADO`

## Funcionalidades principales:
- Definición de constantes de eventos estándar del módulo `activacion/`.
- Creación de estructuras enriquecidas (tipo, timestamp, datos adicionales).
- Emisión de eventos hacia `sistema/`, `agentes/` y otros módulos consumidores.
- Registro opcional de eventos relevantes para trazabilidad.

## Dependencias técnicas:
- `utils/gestion_eventos.py` – Creación y publicación de eventos internos.
- `datetime` – Generación de timestamps.
- `json` – Serialización de payloads de datos.

