# Ficha Funcional – `gestion_wifi_externo.py`

## Nombre del archivo:
`gestion_wifi_externo.py`

## Responsabilidad principal:
Gestionar la configuración, supervisión y control operativo del módulo WiFi adicional (ESP8266 o similar) conectado al sistema NORA. Permite habilitar o deshabilitar conectividad secundaria, monitorizar la calidad de la conexión y gestionar contingencias de comunicación en redes locales o remotas.

## Entradas esperadas:
- **Tipo de entrada:** Comandos de configuración WiFi, solicitudes de supervisión de red.
- **Fuente:** `control_main.py`, `gui/`, `sistema/`.
- **Formato o protocolo:** Instrucciones internas, comandos UART, configuraciones por eventos.

## Salidas generadas:
- **Tipo de salida:** Estado de conexión WiFi, alarmas de caída de red, informes de calidad de señal.
- **Destinatario:** `control_main.py`, `sistema/`, `gui/`.
- **Ejemplo de salida:**
  - `EVT_WIFI_CONNECTED`
  - `EVT_WIFI_DISCONNECTED`
  - `EVT_WIFI_SIGNAL_WEAK`

## Módulos relacionados:
- **Entrada desde:** `control_main.py`, `gui/`.
- **Salida hacia:** `control_main.py`, `sistema/`, `gui/`.
- **Comunicación bidireccional con:** Módulo WiFi (ESP8266 o similar) vía UART.

## Dependencias técnicas:
- **Librerías externas:** `serial` (pySerial), `logging`, `subprocess`.
- **Hardware gestionado:** Módulo WiFi externo (ej. ESP8266).
- **Protocolos:** UART, TCP/IP (nivel lógico).

## Notas adicionales:
`gestion_wifi_externo.py` proporciona al sistema NORA la capacidad de mantener comunicaciones robustas mediante interfaces inalámbricas externas. Su correcto funcionamiento es vital para asegurar redundancia de conectividad, capacidad de control remoto y sincronización de eventos en entornos donde la conectividad primaria pudiera verse comprometida. Debe implementar mecanismos de reconexión automática y diagnóstico rápido de fallos de red.

