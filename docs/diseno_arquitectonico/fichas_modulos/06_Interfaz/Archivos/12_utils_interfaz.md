# Ficha Funcional – `utils_interfaz.py`

## Nombre del archivo:
`utils_interfaz.py`

## Responsabilidad principal:
Proporcionar funciones auxiliares que soportan las operaciones de la interfaz de NORA, como la interpolación de movimientos, la gestión de animaciones, la normalización de intensidades de colores, y otras herramientas útiles para facilitar el trabajo con las salidas visuales y físicas del sistema.

## Entradas esperadas:
- **Tipo de entrada:** Datos de animación, parámetros de movimiento, configuraciones de color y tiempo.
- **Fuente:** Módulos `interfaz/`, `sistema/`, `agentes/`, `voz/` que requieren utilidades para la animación y visualización.
- **Formato o protocolo:** Parámetros de animación, instrucciones de movimiento (por ejemplo, coordenadas de servo), configuraciones de colores.

## Salidas generadas:
- **Tipo de salida:** Resultados de interpolación de movimientos, ajustes de color y brillo, animaciones generadas.
- **Destinatario:** `interfaz/`, `sistema/`, `agentes/` (para aplicar las utilidades de animación y visualización).
- **Ejemplo de salida:**
  - `AGT_COLOR_NORMALIZED` (Evento que indica que el color ha sido normalizado para la animación).
  - `CMD_INTERPOLATE_MOVEMENT` (Instrucción para interpolar un movimiento físico, como el movimiento de la cabeza).
  - `AGT_ANIMATION_FRAME` (Evento que indica que un nuevo cuadro de animación ha sido generado y está listo para ser mostrado).

## Módulos relacionados:
- **Entrada desde:** `interfaz/`, `sistema/`, `agentes/`, `voz/` (para recibir parámetros de animación, color y movimiento).
- **Salida hacia:** `interfaz/`, `sistema/`, `agentes/` (para aplicar los resultados de las utilidades en las animaciones y movimientos físicos).
- **Comunicación bidireccional con:** `interfaz/`, `sistema/` para garantizar que las animaciones y movimientos sean precisos y coherentes.

## Dependencias técnicas:
- **Librerías externas:** `math` (para cálculos de interpolación), `time` (para gestión de tiempos y retrasos), `Pillow` (para la manipulación de imágenes y gráficos de animación).
- **Hardware gestionado:** Ninguno directamente (se gestionan animaciones y movimientos a nivel lógico).
- **Protocolos:** PWM, SPI, I2C para el control de hardware, eventos internos para la coordinación de animaciones.

## Notas adicionales:
Este archivo es esencial para proporcionar soporte a las operaciones más complejas de animación y visualización de NORA. Las funciones de interpolación permiten realizar movimientos suaves y fluidos, mientras que las utilidades de normalización aseguran que los colores y las animaciones sean consistentes. `utils_interfaz.py` optimiza la interacción entre los distintos módulos de la interfaz, haciendo que las respuestas de NORA sean visualmente coherentes y adaptadas al contexto.

## Archivos previstos del módulo:
- `utils_interfaz.py`: Funciones auxiliares para interpolación de movimientos, gestión de animaciones, normalización de intensidades (este archivo).
- Archivos adicionales como `interfaz_main.py`, `pantalla_facial.py`, `leds_rgb.py`.
