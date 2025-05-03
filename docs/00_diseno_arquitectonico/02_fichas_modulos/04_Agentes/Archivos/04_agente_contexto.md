# Ficha Funcional – `agente_contexto.py`

## Nombre del archivo:
`agente_contexto.py`

## Responsabilidad principal:
Gestionar el contexto global del sistema NORA, evaluando eventos relacionados con el entorno del usuario, el contexto temporal (hora, día, situación) y otros factores que puedan influir en el comportamiento del sistema. Este agente toma decisiones basadas en el contexto y activa o desactiva funciones del sistema según las condiciones establecidas.

## Entradas esperadas:
- **Tipo de entrada:** Eventos de contexto temporal, configuración de usuario, datos ambientales.
- **Fuente:** Módulos como `sensores/` (temperatura, calidad del aire), `sistema/` (hora, modo de operación), configuraciones de usuario desde `config_agentes.py`.
- **Formato o protocolo:** Eventos internos (`EVT_TIME_OF_DAY`, `EVT_USER_PREFERENCE`), configuraciones en formato JSON.

## Salidas generadas:
- **Tipo de salida:** Decisiones basadas en el contexto (activación o inhibición de funciones del sistema), modulación de la configuración del sistema.
- **Destinatario:** `sistema/` (para cambiar el modo de operación), `interfaz/` (para modificar las respuestas visuales o de interacción).
- **Ejemplo de salida:**
  - `AGT_CONTEXTUAL_ADJUSTMENT` (Ajuste de la configuración o comportamiento según el contexto).
  - `CMD_ENABLE_FUNCTIONALITY` (Instrucción para activar una función en base al contexto).
  - `AGT_CONTEXT_INHIBIT` (Instrucción para desactivar una función según el contexto, por ejemplo, si es de noche).

## Módulos relacionados:
- **Entrada desde:** `sensores/` (datos de temperatura, humedad, calidad del aire), `sistema/` (hora, configuraciones globales), `interfaz/` (preferencias de usuario).
- **Salida hacia:** `sistema/` (para activar o desactivar funcionalidades del sistema), `interfaz/` (para modificar las respuestas visuales o interacciones).
- **Comunicación bidireccional con:** `agentes/`, `sistema/`, `interfaz/`.

## Dependencias técnicas:
- **Librerías externas:** `datetime` (para gestionar eventos temporales), `json` (para cargar configuraciones).
- **Hardware gestionado:** Ninguno directamente (se maneja a nivel lógico).
- **Protocolos:** Comunicación basada en eventos internos, gestión de configuraciones dinámicas y evaluación de contexto.

## Notas adicionales:
Este agente evalúa el contexto global en el que se encuentra el sistema, tomando en cuenta factores como la hora del día, las preferencias del usuario y las condiciones ambientales. Basándose en esta información, puede activar o desactivar funcionalidades del sistema de manera dinámica, adaptando el comportamiento del sistema a las necesidades actuales del entorno y del usuario. La interacción con otros agentes permite una respuesta contextualizada y multimodal que mejora la interacción global del sistema.

## Archivos previstos del módulo:
- `agente_contexto.py`: Gestión de activación combinada, inhibiciones, contexto horario (este archivo).
- Archivos adicionales de agentes como `agente_visual.py`, `agente_base.py`.
