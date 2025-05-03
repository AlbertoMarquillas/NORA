# Ficha Funcional – `gestion_tiempos.py`

## Nombre del archivo:
`gestion_tiempos.py`

## Responsabilidad principal:
Gestionar funciones relacionadas con la temporización, medición de intervalos y gestión de retardos de forma eficiente en el sistema NORA. Proporciona herramientas para cronometrar operaciones y sincronizar procesos cooperativos.

## Entradas esperadas:
- **Tipo de entrada:** Solicitudes de temporización, medición de tiempos de ejecución, retardos programados.
- **Fuente:** `sistema/`, `control/`, `voz/`, `vision/`, `agentes/`, `tests/`.
- **Formato o protocolo:** Parámetros numéricos (segundos, milisegundos), timestamps.

## Salidas generadas:
- **Tipo de salida:** Medición de tiempos, funciones de espera no bloqueantes.
- **Destinatario:** Módulos funcionales que requieran control temporal.
- **Ejemplo de salida:**
  - Cronómetro de duración de evento
  - Retardo cooperativo de 200 ms

## Módulos relacionados:
- **Entrada desde:** `sistema/`, `control/`, `voz/`, `vision/`, `agentes/`, `tests/`.
- **Salida hacia:** Módulos funcionales.
- **Comunicación bidireccional con:** No aplica (funciones de soporte).

## Dependencias técnicas:
- **Librerías externas:** `time`, `datetime`, `asyncio`.
- **Hardware gestionado:** Ninguno.
- **Protocolos:** Temporización interna, retardos asíncronos.

## Notas adicionales:
`gestion_tiempos.py` debe priorizar la eficiencia y la no obstrucción del flujo principal del sistema. Debe ofrecer tanto retardos activos como retardos cooperativos basados en `asyncio`, para adaptarse a las necesidades de NORA en escenarios sincrónicos y asincrónicos.

