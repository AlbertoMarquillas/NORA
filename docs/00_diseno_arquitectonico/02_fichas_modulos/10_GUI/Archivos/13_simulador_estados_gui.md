# Ficha Funcional – `simulador_estados_gui.py`

## Nombre del archivo:
`simulador_estados_gui.py`

## Responsabilidad principal:
Simular manualmente los diferentes estados de la máquina de estados finita (FSM) de NORA a través de la GUI. Permite validar transiciones, reacciones del sistema y visualización de cambios de estado sin necesidad de generar eventos reales.

## Entradas esperadas:
- **Tipo de entrada:** Selección manual de estados o transiciones.
- **Fuente:** Usuario (interacción GUI).
- **Formato o protocolo:** Eventos de simulación estructurados.

## Salidas generadas:
- **Tipo de salida:** Cambios de estado internos, actualizaciones de interfaz, logs de simulación.
- **Destinatario:** `sistema/`, `interfaz/`, `voz/`, `datos/`.
- **Ejemplo de salida:**
  - Simulación de estado `STATE_LISTENING`
  - Simulación de transición a `STATE_IDLE`

## Módulos relacionados:
- **Entrada desde:** Usuario (GUI).
- **Salida hacia:** `sistema/`, `interfaz/`, `voz/`, `datos/`.
- **Comunicación bidireccional con:** `gui_main.py` para control de flujo y visualización de cambios.

## Dependencias técnicas:
- **Librerías externas:** `tkinter`, `PyQt5`, `PySide2`, `threading`.
- **Hardware gestionado:** Ninguno.
- **Protocolos:** Interno de cambios de estados FSM.

## Notas adicionales:
`simulador_estados_gui.py` es una herramienta fundamental para la depuración y demostración de comportamientos de NORA. Debe reflejar visualmente el estado actual, permitir forzar transiciones seguras y registrar las acciones simuladas en el historial de eventos para su análisis posterior.