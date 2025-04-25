# Ficha Funcional – `gestion_desconexion_red.py`

## Nombre del archivo:
`gestion_desconexion_red.py`

## Responsabilidad principal:
Detectar desconexiones de red prolongadas en el sistema NORA y gestionar de manera segura las acciones de contingencia, como la activación de modos offline, la reconfiguración de servicios dependientes o la emisión de alertas al usuario o administrador.

## Entradas esperadas:
- **Tipo de entrada:** Eventos de estado de red, supervisión de conectividad, informes de fallos de comunicación.
- **Fuente:** `supervision_estado.py`, `gestion_wifi_externo.py`, `control_main.py`.
- **Formato o protocolo:** Eventos estructurados (`EVT_NETWORK_LOST`, `EVT_WIFI_DISCONNECTED`), pings fallidos, errores de socket.

## Salidas generadas:
- **Tipo de salida:** Activación de modo offline, alertas críticas, reintentos de reconexión.
- **Destinatario:** `control_main.py`, `sistema/`, `gui/`.
- **Ejemplo de salida:**
  - `CMD_ACTIVAR_MODO_OFFLINE`
  - `EVT_RECONEXION_EN_PROGRESO`
  - `EVT_FALLO_RECONEXION`

## Módulos relacionados:
- **Entrada desde:** `supervision_estado.py`, `gestion_wifi_externo.py`.
- **Salida hacia:** `control_main.py`, `sistema/`, `gui/`.
- **Comunicación bidireccional con:** Servicios de red internos.

## Dependencias técnicas:
- **Librerías externas:** `socket`, `os`, `subprocess`, `time`, `logging`.
- **Hardware gestionado:** Interfaces de red (WiFi, Ethernet).
- **Protocolos:** TCP/IP, ICMP (ping).

## Notas adicionales:
`gestion_desconexion_red.py` asegura que NORA pueda seguir funcionando de manera coherente y segura en escenarios de conectividad deficiente o inexistente. Debe implementar lógicas de reintento escalonado y permitir la restauración automática de servicios en cuanto la conexión se restablezca, minimizando el impacto para el usuario final.

