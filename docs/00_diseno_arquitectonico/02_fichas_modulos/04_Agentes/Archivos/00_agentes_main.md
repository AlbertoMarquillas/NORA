# Ficha Funcional – `agentes_main.py`

## Nombre del archivo:
`agentes_main.py`

## Responsabilidad principal:
Coordinar la activación, desactivación y comunicación entre los agentes activos del sistema NORA. Este módulo gestiona el ciclo de vida de los agentes, monitorea sus eventos y asegura que las decisiones contextuales y expresivas sean tomadas de manera eficiente, actuando como el cerebro central de la arquitectura de agentes.

## Entradas esperadas:
- **Tipo de entrada:** Eventos internos, configuración de agentes, estados globales.
- **Fuente:** Módulos de percepción como `vision/`, `voz/`, `sensores/`, `sistema/`, configuraciones definidas en `config_agentes.py`.
- **Formato o protocolo:** Eventos internos (`EVT_...`), configuraciones en formato JSON, colas de mensajes para sincronización.

## Salidas generadas:
- **Tipo de salida:** Activación de agentes, distribución de eventos a agentes específicos, modulación de prioridades.
- **Destinatario:** `agentes/` (coordina y distribuye eventos entre los agentes específicos), `sistema/`, `interfaz/`, `voz/`, `dialogo/`.
- **Ejemplo de salida:**
  - `EVT_AGENT_ACTIVE` (Evento de activación de un agente específico).
  - `CMD_AGENT_DEACTIVATE` (Instrucción para desactivar un agente específico).
  - `AGT_CONTEXTUAL_DECISION` (Decisión tomada por agentes en función del contexto).
  - `AGT_PRIORITY_EVENT` (Prioridad de acción dada a un agente).

## Módulos relacionados:
- **Entrada desde:** `vision/`, `voz/`, `sensores/`, `sistema/` (recibe eventos y decisiones del sistema).
- **Salida hacia:** `agentes/`, `sistema/`, `interfaz/`, `voz/`, `dialogo/` (distribuye decisiones contextuales y respuestas de los agentes).
- **Comunicación bidireccional con:** Todos los módulos funcionales principales a través del sistema de eventos.

## Dependencias técnicas:
- **Librerías externas:** `pyee` (sistema de eventos), `asyncio` (gestión asíncrona), `eventbus` (colas de mensajes y comunicación entre módulos).
- **Hardware gestionado:** Ninguno directamente (opera a nivel lógico y coordina módulos).
- **Protocolos:** Manejo de eventos internos, colas de mensajes, y sincronización asíncrona entre agentes.

## Notas adicionales:
Este archivo actúa como un "orquestador" de los agentes del sistema. Utiliza un sistema de eventos basado en `pyee` para manejar la comunicación entre los agentes y sus interacciones con el resto del sistema. También se encarga de manejar la configuración y prioridad de los agentes a través de `config_agentes.py`, permitiendo flexibilidad en su comportamiento y ajuste según el contexto y los requisitos del sistema. Este módulo permite crear o eliminar agentes dinámicamente si es necesario, lo que facilita la ampliación del sistema con nuevos agentes sin alterar la estructura central.

## Archivos previstos del módulo:
- `agentes_main.py`: Coordinador central de los agentes activos (este archivo).
- `agente_base.py`: Clase base abstracta para definir agentes.
