# Ficha Funcional – `gestion_alarmas_criticas.py`

## Nombre del archivo:
`gestion_alarmas_criticas.py`

## Responsabilidad principal:
Gestionar, priorizar y coordinar las alarmas críticas generadas en el sistema NORA. Este archivo garantiza que los eventos de alta gravedad sean tratados de forma adecuada, permitiendo respuestas automáticas, escaladas al usuario o desencadenamiento de medidas de emergencia.

## Entradas esperadas:
- **Tipo de entrada:** Eventos críticos, alertas de supervisión, detecciones de fallos graves.
- **Fuente:** `supervision_estado.py`, `proteccion_fallos.py`, `control_main.py`, `sistema/`.
- **Formato o protocolo:** Eventos estructurados (`EVT_ERROR_CRITICO`, `EVT_TEMPERATURA_EXCESIVA`, `EVT_FALLO_SENSOR`).

## Salidas generadas:
- **Tipo de salida:** Acciones de emergencia, priorización de alarmas, notificación al usuario.
- **Destinatario:** `control_main.py`, `sistema/`, `gui/`.
- **Ejemplo de salida:**
  - `CMD_APAGADO_CRITICO_INMEDIATO`
  - `CMD_NOTIFICAR_USUARIO_CRITICO`
  - Registro detallado del incidente en logs

## Módulos relacionados:
- **Entrada desde:** `supervision_estado.py`, `proteccion_fallos.py`, `control_main.py`.
- **Salida hacia:** `control_main.py`, `sistema/`, `gui/`.
- **Comunicación bidireccional con:** Sistema de eventos y logs.

## Dependencias técnicas:
- **Librerías externas:** `logging`, `os`, `subprocess`.
- **Hardware gestionado:** Supervisión indirecta sobre CPU, sensores, interfaces.
- **Protocolos:** Interno, orientado a eventos y acciones de sistema operativo.

## Notas adicionales:
`gestion_alarmas_criticas.py` es un componente esencial para la seguridad y estabilidad del sistema NORA. Debe implementar una lógica de prioridad que permita distinguir entre alarmas inmediatas y alarmas diferibles, aplicando en cada caso la respuesta más adecuada para preservar la integridad del sistema y la experiencia del usuario.

