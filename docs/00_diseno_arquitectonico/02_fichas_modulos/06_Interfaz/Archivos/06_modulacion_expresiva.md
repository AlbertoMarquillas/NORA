# Ficha Funcional – `modulacion_expresiva.py`

## Nombre del archivo:
`modulacion_expresiva.py`

## Responsabilidad principal:
Gestionar la modulación dinámica de las expresiones visuales y físicas de NORA basadas en el estado emocional global del sistema. Este archivo se encarga de ajustar las expresiones faciales, el color de los LEDs y los movimientos físicos en función de la intensidad emocional del sistema, asegurando que las respuestas sean coherentes y empáticas.

## Entradas esperadas:
- **Tipo de entrada:** Eventos emocionales, instrucciones de modulación, parámetros de expresión emocional.
- **Fuente:** `sistema/`, `agentes/`, `voz/`, `interfaz/` (para recibir datos que modulan la expresión emocional y la atención visual).
- **Formato o protocolo:** Eventos emocionales internos (`EVT_EMOTION_CHANGED`, `EVT_ATTENTION_GAINED`), parámetros de animación y expresiones.

## Salidas generadas:
- **Tipo de salida:** Actualización dinámica de las expresiones visuales y físicas, sincronización de la expresión emocional con el comportamiento del sistema.
- **Destinatario:** Hardware de salida visual y física (pantalla OLED/TFT, LEDs RGB, servomotores).
- **Ejemplo de salida:**
  - `CMD_ADJUST_EXPRESSION` (Instrucción para ajustar las expresiones faciales en la pantalla OLED/TFT según el estado emocional detectado).
  - `CMD_MODULATE_LED_COLOR` (Instrucción para cambiar el color de los LEDs en función de la emoción detectada).
  - `CMD_SYNC_PHYSICAL_EXPRESSION` (Instrucción para mover los servomotores en respuesta a la emoción del sistema).

## Módulos relacionados:
- **Entrada desde:** `sistema/`, `agentes/`, `voz/`, `interfaz/` (para recibir eventos y parámetros emocionales que afectan las expresiones).
- **Salida hacia:** Hardware visual y físico (pantalla OLED/TFT, LEDs RGB, servomotores).
- **Comunicación bidireccional con:** `interfaz/`, `sistema/`, `agentes/` para asegurar que las expresiones visuales y físicas sean coherentes con el estado emocional del sistema.

## Dependencias técnicas:
- **Librerías externas:** `Pillow` (para generar y actualizar imágenes de las expresiones faciales), `rpi_ws281x`, `neopixel` (para el control de LEDs RGB WS2812), `RPi.GPIO`, `pigpio` (para el control de servomotores).
- **Hardware gestionado:** Pantalla OLED/TFT, LEDs RGB WS2812 (Neopixels), servomotores SG90/MG90.
- **Protocolos:** PWM, SPI, I2C para la comunicación con hardware, eventos internos para coordinar las expresiones emocionales.

## Notas adicionales:
Este archivo es clave para crear interacciones dinámicas y empáticas con el usuario. Al ajustar las expresiones de NORA en función de las emociones detectadas, `modulacion_expresiva.py` permite que el sistema se muestre más sensible y consciente de las emociones del usuario. La sincronización entre las respuestas visuales y físicas mejora la inmersión y la coherencia de la experiencia.

## Archivos previstos del módulo:
- `modulacion_expresiva.py`: Modulación dinámica de la expresividad basada en el estado emocional del sistema (este archivo).
- Archivos adicionales como `escenas_expresivas.py`, `pantalla_facial.py`, `leds_rgb.py`.
