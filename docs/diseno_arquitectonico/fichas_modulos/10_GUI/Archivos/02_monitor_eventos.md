# Ficha Funcional – `monitor_eventos.py`

## Nombre del archivo:
`monitor_eventos.py`

## Responsabilidad principal:
Visualizar en tiempo real todos los eventos generados por los distintos módulos del sistema NORA. Permite al usuario supervisar la actividad interna del sistema, detectar anomalías, y analizar la secuencia de eventos producidos durante la operación.

## Entradas esperadas:
- **Tipo de entrada:** Flujos de eventos internos del sistema.
- **Fuente:** `sistema/`, `control/`, `voz/`, `interfaz/`, `sensores/`, `agentes/`.
- **Formato o protocolo:** Estructura de eventos estandarizados (`EVT_...`), colas o buses de eventos.

## Salidas generadas:
- **Tipo de salida:** Visualización de eventos en la GUI, filtros de eventos, exportación de logs opcional.
- **Destinatario:** Usuario (visualización directa), archivos de logs (opcional).
- **Ejemplo de salida:**
  - Lista cronológica de eventos
  - Filtro por tipo de evento (`EVT_SPEECH_RECOGNIZED`, `EVT_FACE_DETECTED`, etc.)

## Módulos relacionados:
- **Entrada desde:** `sistema/`, `control/`, `voz/`, `interfaz/`, `sensores/`, `agentes/`.
- **Salida hacia:** Usuario (GUI).
- **Comunicación bidireccional con:** `gui_main.py` para actualización dinámica de la visualización.

## Dependencias técnicas:
- **Librerías externas:** `tkinter`, `PyQt5`, `PySide2`, `queue`, `threading`.
- **Hardware gestionado:** Ninguno.
- **Protocolos:** Flujo interno de eventos.

## Notas adicionales:
`monitor_eventos.py` debe ser capaz de manejar altos volúmenes de eventos sin bloquear la interfaz de usuario, utilizando mecanismos de threading o colas asíncronas. Debe ofrecer opciones de filtrado, pausado y exportación de eventos para análisis o depuración técnica.