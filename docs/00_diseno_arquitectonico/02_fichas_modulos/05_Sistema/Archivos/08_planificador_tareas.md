# Ficha Funcional – `planificador_tareas.py`

## Nombre del archivo:
`planificador_tareas.py`

## Responsabilidad principal:
Gestionar la programación y ejecución de tareas futuras o periódicas dentro del sistema NORA. Este archivo se encarga de programar acciones basadas en eventos o tiempos configurados, garantizando que las tareas se ejecuten en el momento adecuado, de manera eficiente y sin conflictos con otros procesos del sistema.

## Entradas esperadas:
- **Tipo de entrada:** Eventos de temporización, configuraciones de tareas, entradas de usuarios o módulos que solicitan acciones programadas.
- **Fuente:** Módulos `sistema/`, `agentes/`, `interfaz/`, que envían solicitudes de tareas a ejecutar o eventos que requieren programación.
- **Formato o protocolo:** Comandos de programación (`CMD_SCHEDULE_TASK`), eventos de temporización (`EVT_TASK_TRIGGERED`), configuraciones de tareas en formato JSON.

## Salidas generadas:
- **Tipo de salida:** Comandos de ejecución de tareas, confirmaciones de programación de tareas, eventos de ejecución.
- **Destinatario:** Módulos que gestionan tareas o acciones, como `sistema/`, `agentes/`, `interfaz/`.
- **Ejemplo de salida:**
  - `CMD_EXECUTE_TASK` (Comando para ejecutar una tarea programada).
  - `EVT_TASK_SCHEDULED` (Evento que confirma que una tarea ha sido programada correctamente).
  - `AGT_TASK_COMPLETED` (Evento que indica que una tarea programada ha sido completada).

## Módulos relacionados:
- **Entrada desde:** `sistema/`, `agentes/`, `interfaz/` (para recibir eventos y configuraciones que requieran la programación de tareas).
- **Salida hacia:** `sistema/`, `agentes/`, `interfaz/` (para ejecutar las tareas programadas o actualizar el estado del sistema en función de las tareas ejecutadas).
- **Comunicación bidireccional con:** `sistema/`, `agentes/`, `interfaz/` para gestionar la ejecución de tareas y garantizar que no haya conflictos con otras acciones.

## Dependencias técnicas:
- **Librerías externas:** `schedule` (para la programación de tareas periódicas), `asyncio` (para la ejecución de tareas asíncronas), `time` (para gestionar retrasos y tiempos de ejecución).
- **Hardware gestionado:** Ninguno directamente (gestiona la programación y ejecución de tareas a nivel lógico).
- **Protocolos:** Comunicación basada en eventos internos, temporización de eventos y ejecución programada de tareas.

## Notas adicionales:
Este archivo es esencial para organizar la ejecución de acciones dentro de NORA en función de tiempos específicos o eventos previos. El `planificador_tareas.py` asegura que las tareas no se ejecuten antes de su momento programado y que el sistema no se sobrecargue al intentar ejecutar demasiadas acciones simultáneamente. También permite la ejecución de tareas periódicas, asegurando que el sistema esté siempre actualizado y responda de manera continua a las condiciones del entorno.

## Archivos previstos del módulo:
- `planificador_tareas.py`: Programación y ejecución de acciones futuras o periódicas basadas en eventos o tiempos configurados (este archivo).
- Archivos adicionales como `gestion_eventos.py`, `sistema_main.py`.
