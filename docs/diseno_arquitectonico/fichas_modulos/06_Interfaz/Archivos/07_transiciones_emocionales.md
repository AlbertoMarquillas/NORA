# Ficha Funcional – `transiciones_emocionales.py`

## Nombre del archivo:
`transiciones_emocionales.py`

## Responsabilidad principal:
Gestionar las transiciones suaves entre diferentes expresiones emocionales de NORA. Este archivo se encarga de crear transiciones graduales entre estados emocionales, como pasar de una expresión de tristeza a una de felicidad, asegurando que los cambios sean naturales y agradables visualmente.

## Entradas esperadas:
- **Tipo de entrada:** Comandos de modulación emocional, eventos de cambio de estado emocional.
- **Fuente:** `sistema/`, `agentes/`, `voz/`, `interfaz/` (para recibir eventos relacionados con el estado emocional de NORA).
- **Formato o protocolo:** Eventos emocionales (`EVT_EMOTION_CHANGED`), comandos internos (`CMD_...`), parámetros de transición de expresión emocional.

## Salidas generadas:
- **Tipo de salida:** Instrucciones para realizar transiciones suaves entre expresiones emocionales.
- **Destinatario:** Hardware de salida visual y física (pantalla OLED/TFT, LEDs RGB, servomotores).
- **Ejemplo de salida:**
  - `CMD_SMOOTH_TRANSITION` (Instrucción para realizar una transición suave entre dos expresiones emocionales).
  - `AGT_TRANSITION_COMPLETED` (Evento que indica que la transición emocional se ha completado con éxito).
  - `CMD_UPDATE_FACIAL_EXPRESSION` (Instrucción para actualizar la expresión facial en la pantalla según la transición emocional).

## Módulos relacionados:
- **Entrada desde:** `sistema/`, `agentes/`, `voz/`, `interfaz/` (para recibir eventos de cambio emocional que requieren una transición suave).
- **Salida hacia:** Hardware visual y físico (pantalla OLED/TFT, LEDs RGB, servomotores).
- **Comunicación bidireccional con:** `interfaz/`, `sistema/` para garantizar que las transiciones sean coherentes y sincronizadas con el estado global de NORA.

## Dependencias técnicas:
- **Librerías externas:** `Pillow` (para manipulación de imágenes durante la transición de expresiones faciales), `rpi_ws281x`, `neopixel` (para controlar los LEDs RGB durante la transición de color), `RPi.GPIO`, `pigpio` (para controlar los servomotores durante la transición de movimientos).
- **Hardware gestionado:** Pantalla OLED/TFT, LEDs RGB WS2812 (Neopixels), servomotores SG90/MG90.
- **Protocolos:** PWM, SPI, I2C para la comunicación con hardware, eventos internos para coordinar las transiciones emocionales.

## Notas adicionales:
Este archivo es fundamental para asegurar que las expresiones emocionales de NORA cambien de manera fluida y natural. Las transiciones emocionales no solo mejoran la interacción con el usuario al hacer que las respuestas sean más humanas, sino que también refuerzan la empatía del sistema al mostrar cambios graduales en sus respuestas visuales y físicas. Las transiciones suaves evitan cambios abruptos que puedan resultar incómodos para el usuario, creando una experiencia más agradable.

## Archivos previstos del módulo:
- `transiciones_emocionales.py`: Implementación de transiciones suaves entre expresiones emocionales (este archivo).
- Archivos adicionales como `modulacion_expresiva.py`, `escenas_expresivas.py`, `pantalla_facial.py`.
