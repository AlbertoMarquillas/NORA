# Ficha Específica – `gestion_boton.py`

## Nombre del archivo:
`gestion_boton.py`

## Responsabilidad principal:
Gestionar la detección de pulsaciones del botón físico conectado al sistema y su evaluación como fuente de activación manual para NORA.

## Entradas esperadas:
- Señales digitales de pulsación de botón (GPIO).
- Configuraciones dinámicas (modo de activación manual, debounce, número de pulsaciones requeridas).

## Salidas generadas:
- Eventos de activación manual basada en botón físico.
- Eventos asociados:
  - `EVT_ACTIVATION_CONFIRMED`

## Funcionalidades principales:
- Detección estable de pulsaciones mediante gestión de rebotes (debounce).
- Validación de patrones de pulsación si se requiere (simple, doble clic).
- Emisión de evento de activación inmediatamente tras confirmación de pulsación válida.

## Dependencias técnicas:
- `gpiozero`, `RPi.GPIO` – Gestión de entradas digitales.
- `time` – Control de debounce y temporización de pulsaciones.
- `eventos_activacion.py` – Emisión de eventos de activación.

