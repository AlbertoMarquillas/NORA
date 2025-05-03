# Ficha Funcional – `agente_priorizacion.py`

## Nombre del archivo:
`agente_priorizacion.py`

## Responsabilidad principal:
Gestionar la priorización de eventos y tareas dentro del sistema NORA, asegurando que las acciones más importantes o urgentes sean ejecutadas en primer lugar. Este agente toma decisiones sobre la prioridad de los eventos recibidos, manejando la concurrencia y evitando que eventos menos relevantes interfieran con los más urgentes.

## Entradas esperadas:
- **Tipo de entrada:** Eventos del sistema, señales de priorización, configuraciones dinámicas de prioridad.
- **Fuente:** Módulos `agentes/`, `sistema/`, `interfaz/` que generan eventos y configuraciones que necesitan ser priorizados.
- **Formato o protocolo:** Eventos internos (`EVT_...`), configuraciones en formato JSON que determinan la prioridad.

## Salidas generadas:
- **Tipo de salida:** Prioridades asignadas a los eventos, decisiones de supresión o reprogramación de eventos.
- **Destinatario:** `sistema/` (para modificar el flujo de eventos), `interfaz/` (para ajustar la interfaz en función de las prioridades).
- **Ejemplo de salida:**
  - `AGT_PRIORITY_HIGH` (Evento que indica que el evento tiene alta prioridad y debe ser procesado inmediatamente).
  - `CMD_SUPPRESS_EVENT` (Instrucción para suprimir un evento de baja prioridad).
  - `AGT_PRIORITY_LOW` (Evento que indica que el evento tiene baja prioridad y puede ser procesado más tarde).

## Módulos relacionados:
- **Entrada desde:** `agentes/`, `sistema/`, `interfaz/` (para recibir eventos que deben ser priorizados).
- **Salida hacia:** `sistema/`, `interfaz/` (para modificar el flujo de eventos o ajustar la interfaz).
- **Comunicación bidireccional con:** `agentes/`, `sistema/`, `interfaz/` para asegurar que las decisiones de priorización sean implementadas de manera efectiva.

## Dependencias técnicas:
- **Librerías externas:** `heapq` (para gestionar las colas de prioridad), `json` (para la configuración dinámica de prioridades).
- **Hardware gestionado:** Ninguno directamente (se maneja a nivel lógico).
- **Protocolos:** Comunicación basada en eventos internos, gestión de prioridades y concurrencia.

## Notas adicionales:
Este agente es fundamental para asegurar que el sistema NORA responda de manera eficiente a los eventos más críticos o urgentes. La priorización no solo se basa en la urgencia de un evento, sino también en el contexto del sistema, el estado emocional del usuario y la interacción con otros agentes. Este agente permite gestionar tareas concurrentes y coordinar múltiples eventos sin generar bloqueos ni latencias innecesarias.

## Archivos previstos del módulo:
- `agente_priorizacion.py`: Gestión de prioridades y supresión de eventos en competencia (este archivo).
- Archivos adicionales de agentes como `agente_emocional.py`, `agente_base.py`.
