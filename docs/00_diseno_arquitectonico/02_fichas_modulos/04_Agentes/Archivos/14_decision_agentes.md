# Ficha Funcional – `decision_agentes.py`

## Nombre del archivo:
`decision_agentes.py`

## Responsabilidad principal:
Gestionar la lógica de decisión para los agentes del sistema NORA. Este archivo se encarga de aplicar reglas dinámicas para la activación o supresión de acciones de los agentes, tomando en cuenta los eventos recibidos, el contexto del sistema y las prioridades definidas. Permite a NORA tomar decisiones coherentes y en tiempo real basadas en la interacción y el estado del entorno.

## Entradas esperadas:
- **Tipo de entrada:** Eventos de los agentes, cambios en el contexto global, evaluaciones de prioridades.
- **Fuente:** Módulos como `agentes/`, `sistema/`, `interfaz/`, que generan eventos relacionados con el estado de los agentes y las decisiones contextuales.
- **Formato o protocolo:** Eventos internos (`EVT_...`), configuraciones de prioridades en formato JSON, eventos de toma de decisiones.

## Salidas generadas:
- **Tipo de salida:** Decisiones sobre qué agentes deben ser activados, desactivados o priorizados. Instrucciones para cambiar el comportamiento del sistema.
- **Destinatario:** `agentes/` (para activar o desactivar agentes específicos), `sistema/` (para tomar decisiones sobre el flujo de control global).
- **Ejemplo de salida:**
  - `AGT_DECISION_MADE` (Evento que indica que se ha tomado una decisión sobre un agente o una acción a realizar).
  - `CMD_ACTIVATE_AGENT` (Instrucción para activar un agente según la decisión tomada).
  - `AGT_SUPPRESS_EVENT` (Instrucción para suprimir un evento o acción de baja prioridad).
  - `CMD_PRIORITIZE_AGENT` (Instrucción para asignar mayor prioridad a un agente).

## Módulos relacionados:
- **Entrada desde:** `agentes/` (eventos y decisiones de los agentes), `sistema/` (información sobre el contexto y estado global del sistema), `interfaz/` (para recibir eventos que requieran decisiones contextuales).
- **Salida hacia:** `agentes/` (para activar, desactivar o priorizar agentes según la lógica de decisión), `sistema/` (para coordinar el flujo de decisiones del sistema).
- **Comunicación bidireccional con:** `agentes/`, `sistema/` para tomar decisiones dinámicas basadas en el contexto y prioridades del sistema.

## Dependencias técnicas:
- **Librerías externas:** `asyncio` (para gestionar las decisiones asíncronas), `json` (para gestionar configuraciones y reglas de decisión).
- **Hardware gestionado:** Ninguno directamente (se maneja a nivel lógico).
- **Protocolos:** Comunicación basada en eventos internos, reglas de decisión y gestión de prioridades.

## Notas adicionales:
Este archivo juega un papel clave en la toma de decisiones dentro de NORA, proporcionando la lógica necesaria para activar o desactivar agentes según el contexto y las prioridades. Utiliza un enfoque flexible que permite a NORA adaptarse a las interacciones del usuario y a las condiciones del entorno de manera dinámica. Al gestionar la toma de decisiones de manera centralizada, `decision_agentes.py` asegura que las respuestas del sistema sean siempre coherentes y bien coordinadas.

## Archivos previstos del módulo:
- `decision_agentes.py`: Aplicación de reglas dinámicas de activación o supresión de acciones (este archivo).
- Archivos adicionales de agentes como `agente_priorizacion.py`, `agente_base.py`.
