# Ficha Funcional – `pantalla_facial.py`

## Nombre del archivo:
`pantalla_facial.py`

## Responsabilidad principal:
Gestionar las animaciones faciales en la pantalla OLED/TFT, que representa las expresiones visuales de NORA. Este archivo se encarga de actualizar y modificar las imágenes faciales en tiempo real, en función de los estados emocionales y las interacciones del usuario, proporcionando una respuesta visual coherente y dinámica.

## Entradas esperadas:
- **Tipo de entrada:** Comandos de expresión facial, eventos emocionales, instrucciones de modulación de la expresión.
- **Fuente:** `sistema/`, `agentes/`, `voz/`, `interfaz/` (para recibir eventos de modulación emocional y comandos de actualización de la expresión facial).
- **Formato o protocolo:** Eventos internos (`CMD_...`), parámetros de animación, imágenes o patrones de expresión facial.

## Salidas generadas:
- **Tipo de salida:** Actualización de la expresión facial en la pantalla OLED/TFT, comandos de visualización de nuevas expresiones o transiciones entre expresiones.
- **Destinatario:** Hardware de salida visual (pantalla OLED/TFT).
- **Ejemplo de salida:**
  - `CMD_UPDATE_FACIAL_EXPRESSION` (Instrucción para actualizar la expresión facial en la pantalla OLED/TFT en función del estado emocional detectado).
  - `CMD_TRANSITION_FACIAL_EXPRESSION` (Instrucción para realizar una transición suave entre expresiones faciales).
  - `AGT_FACE_EXPRESSION_UPDATED` (Evento que indica que la expresión facial se ha actualizado correctamente).

## Módulos relacionados:
- **Entrada desde:** `sistema/`, `agentes/`, `voz/`, `interfaz/` (para recibir eventos que modulan la expresión facial).
- **Salida hacia:** Hardware visual (pantalla OLED/TFT).
- **Comunicación bidireccional con:** `interfaz/` (para coordinar las actualizaciones de la pantalla con las respuestas emocionales y contextuales del sistema).

## Dependencias técnicas:
- **Librerías externas:** `Pillow` (para generar y modificar imágenes de expresiones faciales), `RPi.GPIO`, `pigpio` (para controlar la pantalla a través de los pines GPIO), `Tkinter`, `PyGame`, o `PyQt5` (si se requiere una implementación gráfica adicional).
- **Hardware gestionado:** Pantalla OLED/TFT (conectada a la Raspberry Pi u otros controladores).
- **Protocolos:** I2C, SPI (para la comunicación con la pantalla), eventos internos para coordinar las actualizaciones.

## Notas adicionales:
Este archivo es fundamental para crear una experiencia visual rica y empática en NORA. La capacidad de modificar y actualizar las expresiones faciales en tiempo real permite que NORA responda de manera coherente a las emociones y estados del usuario, mejorando la interacción al hacerla más natural y emocionalmente inteligente. Las transiciones suaves entre diferentes expresiones faciales también aportan fluidez a la experiencia del usuario.

## Archivos previstos del módulo:
- `pantalla_facial.py`: Gestión de animaciones faciales en pantalla OLED/TFT (este archivo).
- Archivos adicionales como `interfaz_main.py`, `leds_rgb.py`, `control_servos.py`.
