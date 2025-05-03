# Ficha Funcional – `motor_expresiones_parametrizadas.py`

## Nombre del archivo:
`motor_expresiones_parametrizadas.py`

## Responsabilidad principal:
Gestionar las expresiones cargadas dinámicamente desde archivos externos. Este archivo se encarga de cargar, interpretar y ejecutar expresiones visuales y emocionales de NORA a partir de parámetros proporcionados en archivos de configuración o scripts externos. Permite una personalización avanzada y flexible de las respuestas de NORA, sin necesidad de modificar el código fuente.

## Entradas esperadas:
- **Tipo de entrada:** Archivos de configuración o scripts que definan expresiones faciales, de LEDs y movimientos físicos.
- **Fuente:** Archivos externos (JSON, XML, o cualquier otro formato estructurado), comandos internos (`CMD_LOAD_EXPRESSION`).
- **Formato o protocolo:** Archivos de configuración de expresiones, eventos de activación de expresiones (`CMD_...`), parámetros de animación.

## Salidas generadas:
- **Tipo de salida:** Activación de expresiones cargadas dinámicamente, actualización de la interfaz visual y física basada en los parámetros de los archivos cargados.
- **Destinatario:** Hardware de salida visual y física (pantalla OLED/TFT, LEDs RGB, servomotores).
- **Ejemplo de salida:**
  - `CMD_LOAD_EXPRESSION` (Instrucción para cargar y ejecutar una expresión facial a partir de un archivo externo).
  - `AGT_EXPRESSION_LOADED` (Evento que indica que una expresión ha sido cargada y ejecutada correctamente).
  - `CMD_UPDATE_LEDS` (Instrucción para actualizar los LEDs según los parámetros definidos en el archivo de configuración de la expresión).

## Módulos relacionados:
- **Entrada desde:** Archivos de configuración externa, `sistema/`, `agentes/` (para recibir los comandos que activan las expresiones parametrizadas).
- **Salida hacia:** Hardware de salida visual y física (pantalla OLED/TFT, LEDs RGB, servomotores).
- **Comunicación bidireccional con:** `interfaz/`, `sistema/` para coordinar las expresiones dinámicas con el comportamiento general de NORA.

## Dependencias técnicas:
- **Librerías externas:** `json` (para cargar y manejar archivos de configuración), `Pillow` (para manipular imágenes de expresiones faciales), `rpi_ws281x`, `neopixel` (para controlar LEDs RGB WS2812), `RPi.GPIO`, `pigpio` (para controlar servomotores).
- **Hardware gestionado:** Pantalla OLED/TFT, LEDs RGB WS2812 (Neopixels), servomotores SG90/MG90.
- **Protocolos:** PWM, SPI, I2C para la comunicación con hardware, eventos internos para coordinar las expresiones cargadas.

## Notas adicionales:
Este archivo permite una gran flexibilidad en la personalización de las expresiones de NORA. Al cargar expresiones desde archivos externos, `motor_expresiones_parametrizadas.py` permite la adaptación rápida del sistema a nuevas situaciones o cambios en las preferencias del usuario sin necesidad de modificar el código base. Este enfoque facilita la expansión y la personalización del sistema, proporcionando una experiencia más rica y dinámica.

## Archivos previstos del módulo:
- `motor_expresiones_parametrizadas.py`: Gestión de expresiones cargadas dinámicamente desde archivos externos (este archivo).
- Archivos adicionales como `interfaz_main.py`, `escenas_expresivas.py`, `leds_rgb.py`.
