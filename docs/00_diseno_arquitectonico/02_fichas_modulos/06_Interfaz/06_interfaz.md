# Ficha Funcional – Módulo de Interfaz

## Nombre del módulo:
`interfaz/`

## Responsabilidad principal:
Gestiona todos los canales expresivos físicos y visuales de NORA. Controla la pantalla facial animada, los LEDs RGB, y los servomotores, permitiendo traducir el estado interno del sistema y las emociones en salidas sensoriales perceptibles por el usuario.

## Entradas esperadas:
- Tipo de entrada: comandos de expresión, modulaciones emocionales, instrucciones de atención visual
- Fuente: `sistema/`, `agentes/`, `voz/`, `dialogo/`
- Formato o protocolo: eventos internos (`CMD_...`), parámetros de animación, instrucciones PWM

## Salidas generadas:
- Tipo de salida: activación de pantalla facial, cambios de color en LEDs, movimientos físicos
- Destinatario: hardware físico (pantalla OLED/TFT, LEDs WS2812, servomotores)
- Ejemplo de salida:
  - Animación de alegría en pantalla
  - Cambio de LEDs a color azul "escuchando"
  - Movimiento de cabeza hacia el usuario

## Módulos relacionados:
- Entrada desde: `sistema/`, `agentes/`, `voz/`, `dialogo/`
- Salida hacia: hardware de salida visual y física
- Comunicación bidireccional con: `agentes/` (modulación dinámica)

## Dependencias técnicas:
- Librerías externas: `rpi_ws281x`, `neopixel`, `RPi.GPIO`, `pigpio`, `Pillow`, `PyGame`, `PyQt5`, `tkinter` (según opción de implementación gráfica)
- Hardware gestionado: pantalla OLED/TFT, LEDs WS2812 (Neopixels), servomotores SG90/MG90
- Protocolos: PWM, SPI, I2C, eventos internos

## Notas adicionales:
Permite definir "escenas expresivas" combinadas, sincronizando animaciones faciales, cambios de LEDs y movimientos físicos para generar respuestas multimodales más ricas e inmersivas.

## Archivos previstos del módulo:
Listado de archivos `.py` que se espera implementar dentro del directorio `interfaz/` para estructurar sus funcionalidades.

- `interfaz_main.py`: Coordinador principal de salidas expresivas.
- `pantalla_facial.py`: Gestión de animaciones faciales en pantalla OLED/TFT.
- `leds_rgb.py`: Control de tiras de LEDs WS2812 (Neopixels) y LEDs individuales.
- `control_servos.py`: Movimiento de servomotores para gesticulaciones físicas.
- `escenas_expresivas.py`: Definición y sincronización de combinaciones expresivas (pantalla + LEDs + servos).
- `animaciones_predefinidas.py`: Biblioteca de animaciones y efectos visuales/emocionales.
- `modulacion_expresiva.py`: Modulación dinámica de la expresividad basada en el estado emocional del sistema.
- `transiciones_emocionales.py`: Implementación de transiciones suaves entre expresiones emocionales.
- `animaciones_reactivas.py`: Animaciones automáticas ante eventos inesperados o fallos.
- `motor_expresiones_parametrizadas.py`: Gestión de expresiones cargadas dinámicamente desde archivos externos.
- `simulador_interfaz.py`: Simulador offline de salidas visuales y físicas para pruebas y desarrollo sin hardware.
- `config_interfaz.py`: Configuración de parámetros gráficos, colores, tiempos de animaciones.
- `utils_interfaz.py`: Funciones auxiliares para interpolación de movimientos, gestión de animaciones, normalización de intensidades.

