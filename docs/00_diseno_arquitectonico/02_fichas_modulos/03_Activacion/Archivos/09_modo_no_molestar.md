# Ficha Específica – `modo_no_molestar.py`

## Nombre del archivo:
`modo_no_molestar.py`

## Responsabilidad principal:
Implementar y gestionar el modo "no molestar" para el sistema NORA, bloqueando temporalmente la activación automática por eventos sensoriales o de percepción durante periodos configurados.

## Entradas esperadas:
- Solicitudes de activación/desactivación del modo no molestar.
- Configuraciones dinámicas (duración del modo, fuentes de activación bloqueadas).

## Salidas generadas:
- Estado actual del modo (activo/inactivo).
- Eventos de control asociados:
  - `EVT_NO_MOLESTAR_ACTIVADO`
  - `EVT_NO_MOLESTAR_DESACTIVADO`

## Funcionalidades principales:
- Activación manual o programada del modo no molestar.
- Temporización automática para desactivación tras periodo definido.
- Bloqueo de evaluación de eventos de activación mientras el modo esté activo.
- Emisión de eventos informativos sobre cambios de estado.

## Dependencias técnicas:
- `datetime`, `time` – Control de temporización del modo activo.
- `eventos_activacion.py` – Emisión de eventos de control de estado.

