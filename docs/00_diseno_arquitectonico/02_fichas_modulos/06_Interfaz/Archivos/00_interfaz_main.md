# Ficha Funcional – `interfaz_main.py`

## Nombre del archivo:
`interfaz_main.py`

## Responsabilidad principal:
Gestionar la coordinación principal de todas las salidas expresivas del sistema NORA, incluyendo la pantalla facial, los LEDs RGB y los servomotores. Este archivo es el encargado de recibir las instrucciones para actualizar las expresiones visuales y físicas del sistema, asegurando que las respuestas multimodales (visual, física y vocal) se ejecuten de manera sincronizada y coherente.

## Entradas esperadas:
- **Tipo de entrada:** Comandos de expresión, modulaciones emocionales, instrucciones de atención visual.
- **Fuente:** `sistema/`, `agentes/`, `voz/`, `dialogo/` (que generan eventos o comandos de activación de expresiones).
- **Formato o protocolo:** Eventos internos (`CMD_...`), instrucciones de animación, parámetros de PWM.

## Salidas generadas:
- **Tipo de salida:** Activación de las expresiones visuales y físicas del sistema, actualización de los componentes de la interfaz (pantalla, LEDs, servos).
- **Destinatario:** Hardware físico (pantalla OLED/TFT, LEDs WS2812, servomotores SG90/MG90).
- **Ejemplo de salida:**
  - `CMD_UPDATE_FACIAL_EXPRESSION` (Instrucción para actualizar la expresión facial en la pantalla OLED/TFT).
  - `CMD_UPDATE_LEDS` (Instrucción para cambiar el color de los LEDs RGB según el estado de NORA).
  - `CMD_MOVE_HEAD` (Instrucción para mover los servomotores y realizar una acción física, como orientar la cabeza hacia el usuario).

## Módulos relacionados:
- **Entrada desde:** `sistema/`, `agentes/`, `voz/`, `dialogo/` (para recibir eventos de expresión y emociones que afecten la visualización).
- **Salida hacia:** Hardware de salida visual y física (pantalla OLED/TFT, LEDs RGB, servomotores).
- **Comunicación bidireccional con:** `agentes/` (para recibir instrucciones de modulación emocional y ajustar las expresiones dinámicamente).

## Dependencias técnicas:
- **Librerías externas:** `rpi_ws281x`, `neopixel` (para controlar LEDs RGB WS2812), `RPi.GPIO`, `pigpio` (para controlar servomotores), `Pillow`, `PyGame`, `PyQt5`, `tkinter` (para gestionar animaciones gráficas, dependiendo de la implementación elegida).
- **Hardware gestionado:** Pantalla OLED/TFT, LEDs RGB WS2812 (Neopixels), servomotores SG90/MG90.
- **Protocolos:** PWM, SPI, I2C, eventos internos para coordinar las salidas de la interfaz.

## Notas adicionales:
Este archivo actúa como el coordinador principal de las respuestas físicas y visuales de NORA. Permite la sincronización de múltiples canales expresivos, como la animación facial, la iluminación de LEDs y los movimientos físicos, garantizando que el sistema brinde una experiencia coherente y emocionalmente adecuada. La capacidad de sincronizar estos canales permite que NORA responda de manera natural y empática ante los eventos o interacciones del usuario.

## Archivos previstos del módulo:
- `interfaz_main.py`: Coordinador principal de salidas expresivas (este archivo).
- Archivos adicionales como `pantalla_facial.py`, `leds_rgb.py`, `control_servos.py`.
