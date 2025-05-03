# Ficha Funcional – `diagnostico_automatico.py`

## Nombre del archivo:
`diagnostico_automatico.py`

## Responsabilidad principal:
Ejecutar procedimientos automáticos de diagnóstico de hardware y sistema al arranque o bajo demanda. Verifica el correcto funcionamiento de componentes esenciales como sensores, expansores de I/O, módulo WiFi, almacenamiento externo y comunica los resultados mediante eventos estructurados.

## Entradas esperadas:
- **Tipo de entrada:** Solicitud de autotest, evento de arranque, comando de diagnóstico.
- **Fuente:** `control_main.py`, `gui/`, `sistema/`.
- **Formato o protocolo:** Llamada de función o evento tipo `CMD_AUTOTEST`.

## Salidas generadas:
- **Tipo de salida:** Resultados de test, eventos de error detectado, logs de estado de componentes.
- **Destinatario:** `control_main.py`, `sistema/`, `gui/`.
- **Ejemplo de salida:**
  - `EVT_SELFTEST_PASS`
  - `EVT_SELFTEST_FAIL_SENSOR`
  - `EVT_SELFTEST_FAIL_WIFI`

## Módulos relacionados:
- **Entrada desde:** `control_main.py`, `gui/`.
- **Salida hacia:** `control_main.py`, `sistema/`, `gui/`.
- **Comunicación bidireccional con:** Hardware supervisado.

## Dependencias técnicas:
- **Librerías externas:** `os`, `smbus2`, `serial`, `RPi.GPIO`, `logging`.
- **Hardware gestionado:** Sensores ambientales, expansor PCF8574, módulo WiFi, almacenamiento externo.
- **Protocolos:** GPIO, I2C, UART.

## Notas adicionales:
`diagnostico_automatico.py` permite validar la operatividad del sistema antes de su uso normal o durante rutinas de mantenimiento programadas. Los resultados deben ser persistidos en los logs para referencia futura y visualizados en la GUI cuando corresponda. Debe implementarse con tiempos de prueba razonables para evitar retrasos en el arranque normal.

