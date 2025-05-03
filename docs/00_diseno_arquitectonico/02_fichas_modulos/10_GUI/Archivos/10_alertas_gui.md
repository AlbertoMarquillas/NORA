# Ficha Funcional – `alertas_gui.py`

## Nombre del archivo:
`alertas_gui.py`

## Responsabilidad principal:
Gestionar la visualización prioritaria de alertas y fallos críticos en la GUI de NORA. Presenta de forma inmediata y destacada los eventos de error, advertencia o condiciones de emergencia que requieren atención del usuario.

## Entradas esperadas:
- **Tipo de entrada:** Eventos críticos y alertas generados por el sistema.
- **Fuente:** `sistema/`, `control/`, `supervision_estado.py`, `gestion_alarmas_criticas.py`.
- **Formato o protocolo:** Eventos estructurados (`EVT_ERROR_CRITICO`, `EVT_TEMPERATURA_ALTA`, `EVT_NETWORK_DISCONNECTED`).

## Salidas generadas:
- **Tipo de salida:** Ventanas emergentes, notificaciones visuales, registros de alerta.
- **Destinatario:** Usuario (GUI).
- **Ejemplo de salida:**
  - Popup de sobrecalentamiento
  - Alerta de fallo de sensor
  - Indicador visual de conexión perdida

## Módulos relacionados:
- **Entrada desde:** `sistema/`, `control/`, `supervision_estado.py`, `gestion_alarmas_criticas.py`.
- **Salida hacia:** Usuario (GUI).
- **Comunicación bidireccional con:** `gui_main.py` para coordinar la presentación y gestión de alertas.

## Dependencias técnicas:
- **Librerías externas:** `tkinter`, `PyQt5`, `PySide2`, `threading`.
- **Hardware gestionado:** Ninguno.
- **Protocolos:** Flujo interno de eventos.

## Notas adicionales:
`alertas_gui.py` debe priorizar la visibilidad de eventos importantes, utilizando mecanismos como cambios de color, ventanas emergentes, sonidos opcionales o vibración visual de la GUI. Es crucial que las alertas sean no bloqueantes, permitiendo al usuario reconocerlas pero sin interrumpir la operación general salvo en casos de emergencia extrema.

