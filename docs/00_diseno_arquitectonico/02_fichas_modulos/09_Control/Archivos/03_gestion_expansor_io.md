# Ficha Funcional – `gestion_expansor_io.py`

## Nombre del archivo:
`gestion_expansor_io.py`

## Responsabilidad principal:
Gestionar la comunicación y el control de las entradas y salidas digitales adicionales proporcionadas por el expansor de I/O PCF8574, conectado vía bus I2C. Permite ampliar la capacidad de control de dispositivos del sistema NORA sin sobrecargar los GPIOs nativos de la Raspberry Pi.

## Entradas esperadas:
- **Tipo de entrada:** Comandos de control de pines, solicitudes de lectura de entradas.
- **Fuente:** `control_main.py`, `interfaz/`, `sistema/`.
- **Formato o protocolo:** Llamadas internas a funciones, comunicación I2C estructurada.

## Salidas generadas:
- **Tipo de salida:** Actualización de estados de pines digitales, eventos de cambio de entrada.
- **Destinatario:** `control_main.py`, `sistema/`, dispositivos físicos conectados.
- **Ejemplo de salida:**
  - Activación de LEDs de estado adicionales.
  - Lectura de un pulsador conectado al expansor.

## Módulos relacionados:
- **Entrada desde:** `control_main.py`, `interfaz/`.
- **Salida hacia:** `control_main.py`, `sistema/`, `interfaz/`.
- **Comunicación bidireccional con:** Dispositivo PCF8574 vía bus I2C.

## Dependencias técnicas:
- **Librerías externas:** `smbus2`, `RPi.GPIO`, `logging`.
- **Hardware gestionado:** Expansor de I/O PCF8574.
- **Protocolos:** I2C.

## Notas adicionales:
`gestion_expansor_io.py` permite escalar el número de dispositivos que NORA puede controlar o monitorear, sin necesidad de hardware adicional complejo. Este archivo debe manejar adecuadamente los errores de comunicación en el bus I2C y garantizar la consistencia en la configuración y lectura de los pines del expansor, protegiendo la estabilidad del sistema en tiempo real.