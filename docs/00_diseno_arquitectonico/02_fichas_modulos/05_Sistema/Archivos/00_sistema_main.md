# Ficha Funcional – `sistema_main.py`

## Nombre del archivo:
`sistema_main.py`

## Responsabilidad principal:
Orquestar el funcionamiento global del sistema NORA. Este archivo se encarga de la inicialización del sistema, la configuración de los módulos y la ejecución del ciclo principal de eventos, asegurando que el sistema se mantenga en funcionamiento de manera coherente, gestionando la transición entre estados y la distribución de eventos a los módulos correspondientes.

## Entradas esperadas:
- **Tipo de entrada:** Eventos generados por los módulos perceptivos, agentes, configuraciones globales, comandos de activación.
- **Fuente:** Módulos `vision/`, `voz/`, `sensores/`, `agentes/`, configuraciones del sistema (`config_sistema.py`).
- **Formato o protocolo:** Eventos internos (`EVT_...`), comandos estructurados (`CMD_...`), configuraciones en formato JSON.

## Salidas generadas:
- **Tipo de salida:** Comandos de actuación, transiciones de estado global, registros de actividad y manejo de eventos.
- **Destinatario:** `sistema/`, `interfaz/`, `voz/`, `dialogo/`, `datos/`, `agentes/`.
- **Ejemplo de salida:**
  - `CMD_EXPRESAR` (Comando para iniciar una acción de respuesta visual o verbal).
  - `EVT_STATE_CHANGED` (Evento de cambio de estado global del sistema).
  - `CMD_RESPONDER` (Comando para generar una respuesta a un evento recibido).
  - `CMD_GUARDAR` (Instrucción para almacenar datos relevantes en la base de datos o el sistema de persistencia).

## Módulos relacionados:
- **Entrada desde:** `vision/`, `voz/`, `sensores/`, `agentes/`, `config_sistema.py` (configuración del sistema y los módulos).
- **Salida hacia:** `sistema/`, `interfaz/`, `voz/`, `dialogo/`, `agentes/`, `datos/` (para ejecutar acciones o procesar eventos en los módulos correspondientes).
- **Comunicación bidireccional con:** Todos los módulos funcionales principales, como `sistema/`, `agentes/`, `interfaz/`, `voz/`, y otros que requieren coordinación.

## Dependencias técnicas:
- **Librerías externas:** `transitions` (para la gestión de la máquina de estados), `asyncio` (para la ejecución asíncrona de eventos y tareas), `queue` (para la gestión de eventos en cola), `pyee` o `eventbus` (para la gestión de eventos internos).
- **Hardware gestionado:** Ninguno directamente (se coordina el hardware a través de otros módulos).
- **Protocolos:** Manejo de eventos internos, gestión de la máquina de estados, ciclos de ejecución asíncrona.

## Notas adicionales:
Este archivo es crucial para la gestión y el control centralizado de NORA. Orquesta el ciclo de vida de los eventos y las interacciones de los módulos, asegurando que el sistema responda de manera coherente ante las acciones del usuario. El ciclo principal de eventos supervisa el flujo de información entre módulos y agentes, y permite la transición de estados del sistema según los eventos y el contexto recibidos.

## Archivos previstos del módulo:
- `sistema_main.py`: Orquestador general del sistema, inicialización, ciclo principal de eventos (este archivo).
- Archivos adicionales como `fsm_control.py`, `eventos_sistema.py`, `gestion_eventos.py`.
