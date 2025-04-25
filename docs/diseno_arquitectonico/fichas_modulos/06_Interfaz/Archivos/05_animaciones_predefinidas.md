# Ficha Funcional – `animaciones_predefinidas.py`

## Nombre del archivo:
`animaciones_predefinidas.py`

## Responsabilidad principal:
Gestionar un conjunto de animaciones y efectos visuales/emocionales predefinidos que el sistema NORA puede utilizar para expresar diferentes estados y emociones. Este archivo proporciona una biblioteca de animaciones que se pueden activar en función del estado emocional o la situación del usuario, mejorando la interacción con respuestas visuales predecibles y coherentes.

## Entradas esperadas:
- **Tipo de entrada:** Comandos de activación de animaciones, eventos emocionales, instrucciones de cambio de estado.
- **Fuente:** Módulos `sistema/`, `agentes/`, `interfaz/`, `voz/` que generan eventos o comandos relacionados con las animaciones predefinidas.
- **Formato o protocolo:** Eventos internos (`CMD_...`), parámetros de animación, configuraciones de animaciones predefinidas.

## Salidas generadas:
- **Tipo de salida:** Activación de animaciones predefinidas, secuencias de efectos visuales, transiciones entre animaciones.
- **Destinatario:** Hardware visual (pantalla OLED/TFT, LEDs RGB).
- **Ejemplo de salida:**
  - `CMD_PLAY_PREDEFINED_ANIMATION` (Instrucción para reproducir una animación predefinida, como una sonrisa o un saludo).
  - `AGT_ANIMATION_COMPLETED` (Evento que indica que la animación predefinida se ha completado con éxito).
  - `CMD_START_EFFECT` (Instrucción para activar un efecto visual emocional como un parpadeo de luces o una animación de espera).

## Módulos relacionados:
- **Entrada desde:** `sistema/`, `agentes/`, `interfaz/`, `voz/` (para recibir eventos y comandos que disparen animaciones predefinidas).
- **Salida hacia:** Hardware visual (pantalla OLED/TFT, LEDs RGB).
- **Comunicación bidireccional con:** `interfaz/`, `sistema/` (para coordinar la ejecución de animaciones con otros elementos de la interfaz o el estado del sistema).

## Dependencias técnicas:
- **Librerías externas:** `Pillow` (para manipulación de imágenes de las animaciones faciales), `RPi.GPIO`, `pigpio` (para controlar servos y LEDs), `rpi_ws281x` (para controlar LEDs WS2812).
- **Hardware gestionado:** Pantalla OLED/TFT, LEDs RGB WS2812 (Neopixels), servomotores SG90/MG90.
- **Protocolos:** PWM, SPI, I2C para la comunicación con hardware, eventos internos para coordinar las animaciones.

## Notas adicionales:
Este archivo es fundamental para que NORA tenga una serie de animaciones predefinidas que puedan ser utilizadas de manera eficiente para expresar estados emocionales o interactuar con el usuario de forma coherente. Las animaciones predefinidas pueden ser usadas en situaciones comunes, como saludos, respuestas emocionales, o cuando NORA necesita realizar un gesto específico. Estas animaciones proporcionan un nivel adicional de interacción visual que mejora la experiencia del usuario.

## Archivos previstos del módulo:
- `animaciones_predefinidas.py`: Biblioteca de animaciones y efectos visuales/emocionales (este archivo).
- Archivos adicionales como `interfaz_main.py`, `pantalla_facial.py`, `leds_rgb.py`.
