# Ficha Funcional – `test_control.py`

## Nombre del archivo:
`test_control.py`

## Responsabilidad principal:
Contener las pruebas unitarias y de integración destinadas a validar el funcionamiento de los módulos de control de hardware y supervisión operativa de NORA, incluyendo inicialización de periféricos, control de energía y monitoreo del estado del sistema.

## Entradas esperadas:
- **Tipo de entrada:** Comandos de inicialización, estados simulados de hardware, configuraciones de energía.
- **Fuente:** `control/`.
- **Formato o protocolo:** Configuraciones estructuradas, simulaciones de eventos de hardware.

## Salidas generadas:
- **Tipo de salida:** Resultados de pruebas de supervisión, logs de control de dispositivos.
- **Destinatario:** `tests_main.py`, desarrolladores.
- **Ejemplo de salida:**
  - Inicialización correcta del expansor de I/O
  - Activación exitosa de perfil de bajo consumo

## Módulos relacionados:
- **Entrada desde:** `control/`.
- **Salida hacia:** `tests_main.py`.
- **Comunicación bidireccional con:** `control/` para ejecución de pruebas dinámicas.

## Dependencias técnicas:
- **Librerías externas:** `unittest`, `pytest`, `mock`, `RPi.GPIO`, `smbus2`, `psutil`.
- **Hardware gestionado:** GPIOs, expansores, módulos WiFi, RTC (simulado o real).
- **Protocolos:** Control de dispositivos y gestión energética.

## Notas adicionales:
`test_control.py` debe evaluar tanto la respuesta correcta ante condiciones normales de operación como la robustez del sistema de control frente a fallos simulados, asegurando que NORA sea capaz de gestionar su hardware de forma fiable y segura en todo momento.