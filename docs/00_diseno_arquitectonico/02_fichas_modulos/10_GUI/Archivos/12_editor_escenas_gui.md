# Ficha Funcional – `editor_escenas_gui.py`

## Nombre del archivo:
`editor_escenas_gui.py`

## Responsabilidad principal:
Permitir la creación, edición y gestión gráfica de "escenas expresivas" en NORA, combinando expresiones faciales, iluminación LED y movimientos físicos (servos). Facilita la programación visual de reacciones complejas para distintos estados o eventos.

## Entradas esperadas:
- **Tipo de entrada:** Acciones de usuario (selección de expresiones, colores, movimientos, tiempos).
- **Fuente:** Usuario (interacción GUI).
- **Formato o protocolo:** Formularios, sliders, selectores gráficos.

## Salidas generadas:
- **Tipo de salida:** Definición de escenas estructuradas, comandos de prueba de escena, guardado de configuraciones.
- **Destinatario:** `interfaz/`, `datos/`, `sistema/`.
- **Ejemplo de salida:**
  - Definición de escena "saludo animado"
  - Envío de prueba de escena a `interfaz/`
  - Guardado de escena personalizada

## Módulos relacionados:
- **Entrada desde:** Usuario (GUI).
- **Salida hacia:** `interfaz/`, `datos/`, `sistema/`.
- **Comunicación bidireccional con:** `gui_main.py` para control de flujo y visualización.

## Dependencias técnicas:
- **Librerías externas:** `tkinter`, `PyQt5`, `PySide2`, `json`.
- **Hardware gestionado:** Indirectamente LEDs RGB, servomotores, pantalla facial.
- **Protocolos:** Comandos internos de control de hardware.

## Notas adicionales:
`editor_escenas_gui.py` debe proporcionar una interfaz intuitiva para combinar múltiples canales expresivos (visual, físico, lumínico) en escenas sincronizadas. Las escenas creadas deben poder almacenarse, cargarse y reutilizarse fácilmente, permitiendo su asociación posterior a estados internos, emociones o respuestas automáticas de NORA.