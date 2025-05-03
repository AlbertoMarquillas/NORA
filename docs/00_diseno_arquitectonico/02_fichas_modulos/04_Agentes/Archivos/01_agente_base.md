# Ficha Funcional – `agente_base.py`

## Nombre del archivo:
`agente_base.py`

## Responsabilidad principal:
Definir la clase base abstracta para todos los agentes del sistema NORA. Establece los métodos y propiedades comunes que deben implementar los agentes especializados, como la gestión de eventos, la toma de decisiones contextuales y la interacción con otros módulos del sistema.

## Entradas esperadas:
- **Tipo de entrada:** Eventos del sistema, configuraciones específicas del agente.
- **Fuente:** Módulos de percepción (como `vision/`, `voz/`, `sensores/`), configuraciones de usuario, parámetros definidos en `config_agentes.py`.
- **Formato o protocolo:** Eventos internos (`EVT_...`), configuraciones en formato JSON.

## Salidas generadas:
- **Tipo de salida:** Eventos internos que activan la lógica del agente, decisiones contextuales, respuestas a eventos.
- **Destinatario:** Dependiendo del tipo de agente, puede generar eventos para `sistema/`, `interfaz/`, `voz/`, `agentes/`, etc.
- **Ejemplo de salida:**
  - `AGT_DECISION_MADE` (Evento generado tras tomar una decisión basada en un evento recibido).
  - `AGT_UPDATE_STATE` (Instrucción para actualizar el estado interno del agente).

## Módulos relacionados:
- **Entrada desde:** Módulos perceptivos y otros agentes que envían eventos y parámetros configurables.
- **Salida hacia:** Otros agentes y módulos que gestionan los eventos y respuestas generadas.
- **Comunicación bidireccional con:** `agentes/`, `sistema/`, `interfaz/`, y otros módulos responsables de ejecutar las acciones.

## Dependencias técnicas:
- **Librerías externas:** `abc` (para definir clases abstractas en Python).
- **Hardware gestionado:** Ninguno directamente (se maneja a nivel lógico).
- **Protocolos:** Comunicación basada en eventos internos, gestión de estados y transiciones.

## Notas adicionales:
Este archivo proporciona la infraestructura básica para la implementación de agentes especializados en el sistema NORA. Los agentes heredan de esta clase base y sobrescriben los métodos específicos para realizar tareas como la toma de decisiones contextuales, la modulación emocional o la activación de acciones. La clase base asegura que todos los agentes compartan una interfaz común y un comportamiento estructurado.

## Archivos previstos del módulo:
- `agente_base.py`: Clase base abstracta para definir agentes (este archivo).
- Archivos adicionales de agentes especializados como `agente_visual.py`, `agente_auditivo.py`, etc.
