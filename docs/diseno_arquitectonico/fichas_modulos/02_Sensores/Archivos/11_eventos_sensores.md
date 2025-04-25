# Ficha Específica – `eventos_sensores.py`

## Nombre del archivo:
`eventos_sensores.py`

## Responsabilidad principal:
Definir, estructurar y emitir los eventos internos generados por el módulo `sensores/`, permitiendo comunicar de forma estandarizada al resto del sistema la información captada por los sensores.

## Entradas esperadas:
- Resultados de lectura de sensores individuales.
- Parámetros de eventos (tipo de evento, datos asociados).

## Salidas generadas:
- Emisión de eventos de sensores:
  - `EVT_PRESENCE_CONFIRMED`
  - `EVT_ENV_HOT`
  - `EVT_NFC_UID_DETECTED`
  - `EVT_ENV_LOGGED`, entre otros.

## Funcionalidades principales:
- Definición de constantes estándar para eventos del módulo `sensores/`.
- Creación de estructuras de eventos enriquecidos (tipo, timestamp, payload de datos).
- Emisión de eventos hacia `sistema/`, `agentes/`, `activacion/` y `datos/`.
- Registro opcional de eventos importantes para trazabilidad.

## Dependencias técnicas:
- `utils/gestion_eventos.py` – Creación y publicación de eventos internos.
- `datetime` – Generación de timestamps.
- `json` – Serialización de payloads de datos.

