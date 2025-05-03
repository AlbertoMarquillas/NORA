# Ficha Funcional – `supervision_estado.py`

## Nombre del archivo:
`supervision_estado.py`

## Responsabilidad principal:
Monitorizar continuamente el estado físico y operativo de NORA, incluyendo temperatura de la CPU, carga de RAM, estado de conectividad de red y otros parámetros críticos. Detectar condiciones anómalas o peligrosas, generar eventos de alerta y registrar logs para diagnóstico.

## Entradas esperadas:
- **Tipo de entrada:** Solicitudes de supervisión periódica, eventos de actualización de estado.
- **Fuente:** `control_main.py`, temporizadores internos, sistema operativo.
- **Formato o protocolo:** Llamadas internas de supervisión, lecturas de sensores del sistema.

## Salidas generadas:
- **Tipo de salida:** Alarmas críticas, actualizaciones de estado, logs de supervisión.
- **Destinatario:** `control_main.py`, `sistema/`, `gui/`.
- **Ejemplo de salida:**
  - `EVT_CPU_OVERHEAT`
  - `EVT_MEMORY_LOW`
  - `EVT_NETWORK_DISCONNECTED`

## Módulos relacionados:
- **Entrada desde:** `control_main.py`.
- **Salida hacia:** `control_main.py`, `sistema/`, `gui/`.
- **Comunicación bidireccional con:** Sistema operativo (a través de librerías como `psutil`).

## Dependencias técnicas:
- **Librerías externas:** `psutil`, `os`, `subprocess`, `logging`.
- **Hardware gestionado:** CPU, RAM, interfaces de red.
- **Protocolos:** Acceso a información del sistema operativo.

## Notas adicionales:
`supervision_estado.py` es crítico para la detección temprana de fallos o degradaciones en el funcionamiento de NORA. Permite al sistema tomar medidas preventivas, como activar modos de bajo consumo, notificar al usuario o realizar apagados controlados ante riesgos. Su diseño debe ser altamente eficiente para evitar sobrecargar el sistema durante la supervisión continua.

