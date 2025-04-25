# Ficha Funcional – `animaciones_reactivas.py`

## Nombre del archivo:
`animaciones_reactivas.py`

## Responsabilidad principal:
Gestionar las animaciones automáticas que se activan en respuesta a eventos inesperados o fallos en el sistema. Este archivo se encarga de definir y ejecutar animaciones de emergencia o reactivas, como alertas visuales, parpadeos de LEDs o animaciones faciales que avisen al usuario de que ha ocurrido un evento imprevisto o un fallo.

## Entradas esperadas:
- **Tipo de entrada:** Eventos de error, fallos del sistema, eventos inesperados o eventos que requieran una respuesta rápida.
- **Fuente:** Módulos `sistema/`, `agentes/`, `interfaz/`, `voz/` que emiten eventos relacionados con fallos o situaciones imprevistas.
- **Formato o protocolo:** Eventos de error (`EVT_SYSTEM_ERROR`, `EVT_UNEXPECTED_EVENT`), comandos de activación de animaciones de emergencia.

## Salidas generadas:
- **Tipo de salida:** Activación de animaciones reactivas, alertas visuales o físicas, animaciones faciales o de LEDs.
- **Destinatario:** Hardware de salida visual y física (pantalla OLED/TFT, LEDs RGB, servomotores).
- **Ejemplo de salida:**
  - `CMD_ACTIVATE_ERROR_ANIMATION` (Instrucción para activar una animación reactiva como un parpadeo de LEDs o una expresión facial de alerta).
  - `AGT_ERROR_ANIMATION_COMPLETED` (Evento que indica que la animación reactiva se ha completado).
  - `CMD_BLINK_LEDS` (Instrucción para hacer parpadear los LEDs en respuesta a un error o evento inesperado).

## Módulos relacionados:
- **Entrada desde:** `sistema/`, `agentes/`, `interfaz/`, `voz/` (para recibir eventos relacionados con fallos o situaciones inesperadas que requieran una respuesta reactiva).
- **Salida hacia:** Hardware de salida visual y física (pantalla OLED/TFT, LEDs RGB, servomotores).
- **Comunicación bidireccional con:** `sistema/`, `interfaz/` para coordinar las respuestas visuales y físicas ante errores o fallos.

## Dependencias técnicas:
- **Librerías externas:** `Pillow` (para crear animaciones faciales de alerta), `rpi_ws281x`, `neopixel` (para controlar LEDs RGB WS2812), `RPi.GPIO`, `pigpio` (para controlar servomotores y generar animaciones físicas).
- **Hardware gestionado:** Pantalla OLED/TFT, LEDs RGB WS2812 (Neopixels), servomotores SG90/MG90.
- **Protocolos:** PWM, SPI, I2C para la comunicación con hardware, eventos internos para coordinar las animaciones reactivas.

## Notas adicionales:
Este archivo es esencial para garantizar que el sistema NORA pueda reaccionar de manera visible y coherente a situaciones imprevistas, como errores o fallos del sistema. Las animaciones reactivas proporcionan un medio de notificación visual que puede alertar al usuario de un problema, y la sincronización con las respuestas físicas (como el parpadeo de LEDs o el movimiento de la cabeza) refuerza la alerta visual. Esto mejora la interacción del usuario y asegura que los fallos no pasen desapercibidos.

## Archivos previstos del módulo:
- `animaciones_reactivas.py`: Animaciones automáticas ante eventos inesperados o fallos (este archivo).
- Archivos adicionales como `interfaz_main.py`, `pantalla_facial.py`, `leds_rgb.py`.
