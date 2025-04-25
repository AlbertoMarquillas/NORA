# Ficha Funcional – `fsm_control.py`

## Nombre del archivo:
`fsm_control.py`

## Responsabilidad principal:
Definir y gestionar la máquina de estados finita (FSM) del sistema NORA. Este archivo se encarga de la configuración de los estados del sistema, las transiciones entre estos estados y las acciones que se deben ejecutar en cada estado. La máquina de estados es el núcleo lógico que permite controlar el flujo del sistema y asegurar que NORA responda correctamente a los eventos del entorno.

## Entradas esperadas:
- **Tipo de entrada:** Eventos generados por los módulos perceptivos, eventos internos, configuraciones del sistema.
- **Fuente:** Módulos `agentes/`, `sensores/`, `vision/`, `voz/`, `sistema/`.
- **Formato o protocolo:** Eventos internos (`EVT_...`), comandos estructurados (`CMD_...`), configuraciones en formato JSON.

## Salidas generadas:
- **Tipo de salida:** Comandos de transición de estado, acciones asociadas a cada estado, eventos de cambio de estado.
- **Destinatario:** `sistema/` (para ejecutar la transición de estados y realizar las acciones correspondientes), `interfaz/` (para actualizar la visualización o la interfaz según el estado).
- **Ejemplo de salida:**
  - `EVT_STATE_CHANGED` (Evento que indica que el estado del sistema ha cambiado).
  - `CMD_TRANSITION_STATE` (Instrucción para cambiar de un estado a otro, con la ejecución de la acción asociada).
  - `AGT_ACTION_EXECUTED` (Evento que confirma que una acción asociada a un estado se ha completado correctamente).

## Módulos relacionados:
- **Entrada desde:** `agentes/`, `sistema/`, `interfaz/` (para recibir eventos que indican cambios de estado o necesitan activar una transición).
- **Salida hacia:** `sistema/` (para activar las transiciones de estado y acciones correspondientes), `interfaz/` (para actualizar la interfaz visual según el estado).
- **Comunicación bidireccional con:** `sistema/`, `agentes/`, `interfaz/` para garantizar que las transiciones de estado sean coherentes con el comportamiento del sistema.

## Dependencias técnicas:
- **Librerías externas:** `transitions` (para gestionar la máquina de estados finita), `asyncio` (para gestionar tareas asíncronas asociadas a los estados).
- **Hardware gestionado:** Ninguno directamente (gestiona la lógica del sistema a nivel de software).
- **Protocolos:** Comunicación basada en eventos internos, ciclo de vida de la FSM, transiciones de estados.

## Notas adicionales:
Este archivo es clave para gestionar la lógica del sistema NORA. La máquina de estados permite definir un flujo de trabajo claro y estructurado para la ejecución de las acciones del sistema en función del estado en el que se encuentre. El archivo se encarga de gestionar las transiciones de estado en función de los eventos que ocurren en el sistema, y coordina las acciones a realizar en cada uno de esos estados. La flexibilidad de la FSM asegura que el sistema pueda adaptarse a diferentes contextos y situaciones dinámicas.

## Archivos previstos del módulo:
- `fsm_control.py`: Definición de la máquina de estados y sus transiciones (este archivo).
- Archivos adicionales como `gestion_eventos.py`, `control_prioridades.py`, `monitor_consistencia.py`.
