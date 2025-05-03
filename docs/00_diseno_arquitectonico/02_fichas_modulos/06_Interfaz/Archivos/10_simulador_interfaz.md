# Ficha Funcional – `simulador_interfaz.py`

## Nombre del archivo:
`simulador_interfaz.py`

## Responsabilidad principal:
Simular las salidas visuales y físicas del sistema NORA de manera offline, sin la necesidad de tener hardware físico conectado. Este archivo permite probar y desarrollar las expresiones visuales, animaciones y movimientos físicos en un entorno de simulación, facilitando la validación y depuración del sistema antes de su implementación en hardware real.

## Entradas esperadas:
- **Tipo de entrada:** Comandos de animación, eventos emocionales, instrucciones de modulación de la expresión, configuraciones de simulación.
- **Fuente:** Módulos `sistema/`, `agentes/`, `interfaz/`, `voz/` (para recibir eventos y comandos de modulación emocional y visual).
- **Formato o protocolo:** Eventos internos (`CMD_...`), parámetros de simulación, configuraciones de animación.

## Salidas generadas:
- **Tipo de salida:** Simulación de las animaciones, cambios en las expresiones visuales y movimientos físicos en el entorno de simulación.
- **Destinatario:** Consola o interfaz gráfica de simulación (simulador de pantalla, LEDs, servos).
- **Ejemplo de salida:**
  - `SIMULATION_START` (Instrucción para iniciar la simulación de expresiones y movimientos).
  - `CMD_SIMULATE_FACIAL_EXPRESSION` (Simula una expresión facial en el entorno gráfico o consola).
  - `AGT_SIMULATION_COMPLETED` (Evento que indica que una animación o movimiento ha sido simulado correctamente).

## Módulos relacionados:
- **Entrada desde:** `sistema/`, `agentes/`, `interfaz/`, `voz/` (para recibir eventos de simulación y comandos relacionados con la modulación de expresiones).
- **Salida hacia:** Consola o interfaz gráfica de simulación (entorno visual simulado).
- **Comunicación bidireccional con:** `interfaz/`, `sistema/` para coordinar las salidas visuales y físicas simuladas con las interacciones del sistema.

## Dependencias técnicas:
- **Librerías externas:** `pygame` o `tkinter` (para simular la interfaz gráfica de las salidas visuales), `Pillow` (para la manipulación de imágenes en la simulación de expresiones faciales), `RPi.GPIO` (simulación de pines GPIO, si es necesario para probar servos virtuales).
- **Hardware gestionado:** Ninguno directamente (se simulan las salidas visuales y físicas a través de gráficos en pantalla o consola).
- **Protocolos:** Simulación de eventos internos, manejo de entradas de comandos y salida visual sin hardware físico.

## Notas adicionales:
Este archivo es esencial para el desarrollo y la depuración del sistema antes de implementarlo en hardware real. Permite probar las expresiones faciales, los cambios de color en los LEDs y los movimientos físicos de manera simulada, lo que facilita la validación de la lógica del sistema y la detección temprana de errores o inconsistencias. Al utilizar un entorno de simulación, los desarrolladores pueden probar diferentes situaciones sin necesidad de tener acceso a la infraestructura de hardware física, lo que acelera el proceso de desarrollo.

## Archivos previstos del módulo:
- `simulador_interfaz.py`: Simulador offline de salidas visuales y físicas para pruebas y desarrollo sin hardware (este archivo).
- Archivos adicionales como `interfaz_main.py`, `pantalla_facial.py`, `leds_rgb.py`.
