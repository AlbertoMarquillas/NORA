# Ficha Funcional – `escenas_expresivas.py`

## Nombre del archivo:
`escenas_expresivas.py`

## Responsabilidad principal:
Definir y gestionar las combinaciones sincronizadas de respuestas físicas, visuales y vocales del sistema NORA. Este archivo se encarga de coordinar las diferentes expresiones del sistema, como las animaciones faciales, el cambio de color en los LEDs y los movimientos físicos de los servos, para crear escenas expresivas completas que mejoren la interacción con el usuario.

## Entradas esperadas:
- **Tipo de entrada:** Comandos de expresión, eventos emocionales, instrucciones de atención visual y cambios de estado.
- **Fuente:** Módulos `sistema/`, `agentes/`, `voz/`, `interfaz/` que generan eventos o instrucciones de modulación emocional, visual o física.
- **Formato o protocolo:** Eventos internos (`CMD_...`), instrucciones de animación y color, parámetros de PWM para controlar los movimientos.

## Salidas generadas:
- **Tipo de salida:** Activación de escenas expresivas sincronizadas (pantalla + LEDs + servos).
- **Destinatario:** Hardware físico (pantalla OLED/TFT, LEDs RGB, servomotores).
- **Ejemplo de salida:**
  - `CMD_PLAY_SCENE` (Instrucción para ejecutar una escena expresiva completa, como un saludo o una respuesta empática).
  - `AGT_SCENE_COMPLETED` (Evento que indica que la escena expresiva se ha completado exitosamente).
  - `CMD_SYNC_EXPRESSIONS` (Instrucción para asegurar que las expresiones faciales, los LEDs y los movimientos físicos estén sincronizados).

## Módulos relacionados:
- **Entrada desde:** `sistema/`, `agentes/`, `voz/`, `interfaz/` (para recibir eventos que requieren una respuesta expresiva sincronizada).
- **Salida hacia:** Hardware de salida visual y física (pantalla OLED/TFT, LEDs RGB, servomotores).
- **Comunicación bidireccional con:** `interfaz/`, `agentes/` (para coordinar las expresiones visuales, auditivas y físicas de manera coherente).

## Dependencias técnicas:
- **Librerías externas:** `Pillow` (para manipular imágenes de las expresiones faciales), `RPi.GPIO`, `pigpio` (para controlar los servomotores y LEDs), `rpi_ws281x` (para controlar LEDs WS2812).
- **Hardware gestionado:** Pantalla OLED/TFT, LEDs RGB WS2812 (Neopixels), servomotores SG90/MG90.
- **Protocolos:** PWM, SPI, I2C para comunicación con hardware, eventos internos para sincronización de expresiones.

## Notas adicionales:
Este archivo es clave para proporcionar una respuesta emocional rica y coherente de NORA. La capacidad de sincronizar los canales expresivos (pantalla, LEDs y servos) permite que NORA realice interacciones más naturales y dinámicas, reflejando de manera visible las emociones y reacciones del sistema. Las "escenas expresivas" pueden ser predefinidas o generadas en tiempo real, adaptándose al contexto y proporcionando una experiencia inmersiva para el usuario.

## Archivos previstos del módulo:
- `escenas_expresivas.py`: Definición y sincronización de combinaciones expresivas (pantalla + LEDs + servos) (este archivo).
- Archivos adicionales como `interfaz_main.py`, `pantalla_facial.py`, `leds_rgb.py`.
