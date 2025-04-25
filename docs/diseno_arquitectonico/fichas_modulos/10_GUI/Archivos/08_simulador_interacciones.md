# Ficha Funcional – `simulador_interacciones.py`

## Nombre del archivo:
`simulador_interacciones.py`

## Responsabilidad principal:
Permitir la simulación manual de interacciones de usuario dentro de la GUI de NORA. Facilita la prueba de flujos de conversación, reacciones del sistema a eventos perceptivos simulados y el entrenamiento de respuestas modulares sin necesidad de sensores o hardware activo.

## Entradas esperadas:
- **Tipo de entrada:** Acciones del usuario (selección de eventos, texto de comandos, configuración de contexto).
- **Fuente:** Usuario (interacción GUI).
- **Formato o protocolo:** Formularios y botones de simulación.

## Salidas generadas:
- **Tipo de salida:** Generación de eventos simulados, respuestas del sistema, logs de simulación.
- **Destinatario:** `sistema/`, `voz/`, `dialogo/`, `interfaz/`, `agentes/`.
- **Ejemplo de salida:**
  - `EVT_FACE_DETECTED` (simulado)
  - `EVT_WAKEWORD` (simulado)
  - Texto enviado como comando de voz reconocido

## Módulos relacionados:
- **Entrada desde:** Usuario (GUI).
- **Salida hacia:** `sistema/`, `voz/`, `dialogo/`, `interfaz/`, `agentes/`.
- **Comunicación bidireccional con:** `gui_main.py` para actualizar resultados de simulación.

## Dependencias técnicas:
- **Librerías externas:** `tkinter`, `PyQt5`, `PySide2`, `threading`.
- **Hardware gestionado:** Ninguno (operación simulada).
- **Protocolos:** Interno de eventos del sistema.

## Notas adicionales:
`simulador_interacciones.py` es una herramienta esencial para el desarrollo y depuración de NORA, permitiendo validar reacciones sin depender de la captura de datos reales. Debe ser fácil de usar, configurable y capaz de simular condiciones de flujo complejas (secuencias de eventos, simultaneidad, estados emocionales).

