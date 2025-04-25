# Ficha Funcional – `leds_rgb.py`

## Nombre del archivo:
`leds_rgb.py`

## Responsabilidad principal:
Controlar las tiras de LEDs RGB WS2812 (Neopixels) y LEDs individuales, gestionando los cambios de color según el estado emocional y las interacciones del sistema NORA. Este archivo se encarga de actualizar los colores de los LEDs para reflejar el estado de NORA, utilizando diferentes colores para expresar emociones y estados.

## Entradas esperadas:
- **Tipo de entrada:** Comandos de modulación emocional, eventos de cambio de estado, instrucciones de expresión.
- **Fuente:** `sistema/`, `agentes/`, `voz/`, `interfaz/` (para recibir instrucciones sobre la modulación de los LEDs basadas en el estado emocional y las interacciones).
- **Formato o protocolo:** Eventos internos (`CMD_...`), instrucciones de color en formato RGB, parámetros de PWM.

## Salidas generadas:
- **Tipo de salida:** Activación de LEDs, cambios de color de las tiras de LEDs o LEDs individuales, transiciones de color.
- **Destinatario:** Hardware de salida visual (LEDs WS2812, LEDs individuales).
- **Ejemplo de salida:**
  - `CMD_UPDATE_LED_COLOR` (Instrucción para cambiar el color de los LEDs según el estado de NORA).
  - `CMD_LEDS_TRANSITION` (Instrucción para realizar una transición suave entre colores en los LEDs).
  - `AGT_LEDS_UPDATED` (Evento que indica que los LEDs han sido actualizados correctamente).

## Módulos relacionados:
- **Entrada desde:** `sistema/`, `agentes/`, `voz/`, `interfaz/` (para recibir eventos de cambio de color y modulación emocional).
- **Salida hacia:** Hardware visual (LEDs WS2812, LEDs individuales).
- **Comunicación bidireccional con:** `interfaz/` (para coordinar las actualizaciones de color y la modulación de las expresiones visuales).

## Dependencias técnicas:
- **Librerías externas:** `rpi_ws281x` o `neopixel` (para controlar las tiras de LEDs WS2812), `RPi.GPIO`, `pigpio` (para controlar los pines GPIO y gestionar los LEDs).
- **Hardware gestionado:** Tiras de LEDs RGB WS2812 (Neopixels) y LEDs individuales.
- **Protocolos:** PWM, SPI, eventos internos para coordinar las actualizaciones de color.

## Notas adicionales:
Este archivo es esencial para reflejar el estado emocional y de atención de NORA a través de sus LEDs. Los LEDs RGB permiten crear una respuesta visual que complementa la interacción con el usuario, reflejando emociones como alegría, tristeza, alerta o escucha. Al sincronizar estos colores con las expresiones faciales y los movimientos físicos, el sistema NORA puede generar una respuesta visual coherente y rica, mejorando la experiencia del usuario.

## Archivos previstos del módulo:
- `leds_rgb.py`: Control de tiras de LEDs WS2812 (Neopixels) y LEDs individuales (este archivo).
- Archivos adicionales como `interfaz_main.py`, `pantalla_facial.py`, `control_servos.py`.
