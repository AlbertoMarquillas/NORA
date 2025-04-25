# Ficha Específica – `control_hysteresis.py`

## Nombre del archivo:
`control_hysteresis.py`

## Responsabilidad principal:
Gestionar los tiempos de espera y márgenes de histéresis en los procesos de activación del sistema NORA, evitando activaciones y desactivaciones rápidas o erráticas causadas por fluctuaciones en los eventos de entrada.

## Entradas esperadas:
- Eventos de activación detectados (presencia, atención, hotword, etc.).
- Configuraciones dinámicas (tiempos de histéresis para activación y reposo).

## Salidas generadas:
- Decisión validada de activación o mantenimiento de reposo.
- Eventos emitidos tras respetar los márgenes de histéresis.

## Funcionalidades principales:
- Aplicación de tiempos mínimos de estabilidad para confirmar activación.
- Prevención de reactivaciones consecutivas en intervalos demasiado cortos.
- Gestión de histéresis independiente para activación y para paso a reposo.
- Emisión de eventos finales solo tras validar la condición estable.

## Dependencias técnicas:
- `datetime`, `time` – Cálculo de intervalos de histéresis.
- `eventos_activacion.py` – Emisión de eventos finales tras validación.