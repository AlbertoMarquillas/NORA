# Ficha Funcional – `config_agentes.py`

## Nombre del archivo:
`config_agentes.py`

## Responsabilidad principal:
Gestionar la configuración dinámica de los agentes dentro del sistema NORA. Este archivo define los parámetros de sensibilidad, umbrales de activación, y otros parámetros configurables que determinan el comportamiento de los agentes según el contexto o las preferencias del usuario.

## Entradas esperadas:
- **Tipo de entrada:** Archivos de configuración, parámetros de sensibilidad, umbrales de activación, configuraciones de comportamiento de los agentes.
- **Fuente:** Archivos de configuración en formato JSON o similares, parámetros definidos por el usuario o el sistema.
- **Formato o protocolo:** Archivos de configuración (`config.json`), valores numéricos o de texto para parámetros específicos de los agentes.

## Salidas generadas:
- **Tipo de salida:** Parámetros configurados y ajustados que se distribuyen entre los agentes para modificar su comportamiento.
- **Destinatario:** `agentes/` (para distribuir las configuraciones a cada agente según su funcionalidad).
- **Ejemplo de salida:**
  - `AGT_CONFIG_UPDATED` (Evento que indica que las configuraciones de los agentes han sido actualizadas).
  - `CMD_UPDATE_AGENT_PARAMETER` (Instrucción para actualizar los parámetros de un agente específico).
  - `AGT_SENSITIVITY_LEVEL` (Instrucción para ajustar los umbrales de sensibilidad de los agentes).

## Módulos relacionados:
- **Entrada desde:** Archivos de configuración (`config.json`), parámetros definidos por el usuario, otras configuraciones del sistema.
- **Salida hacia:** `agentes/` (para aplicar las configuraciones a los agentes específicos), `sistema/` (para modificar el comportamiento global del sistema en función de las configuraciones de los agentes).
- **Comunicación bidireccional con:** `agentes/`, `sistema/` para asegurar que las configuraciones sean aplicadas de manera correcta y coherente.

## Dependencias técnicas:
- **Librerías externas:** `json` (para gestionar la lectura y escritura de configuraciones).
- **Hardware gestionado:** Ninguno directamente (se maneja a nivel lógico).
- **Protocolos:** Manejo de configuraciones dinámicas y distribución de parámetros a través de eventos internos.

## Notas adicionales:
Este archivo permite la personalización del comportamiento de los agentes dentro del sistema NORA. Al proporcionar una forma centralizada de gestionar los parámetros de cada agente, `config_agentes.py` facilita la adaptación del sistema a las preferencias del usuario o a cambios en las condiciones externas. Es esencial para crear una experiencia más personalizada y flexible, asegurando que los agentes actúen de acuerdo con las configuraciones definidas en cada momento.

## Archivos previstos del módulo:
- `config_agentes.py`: Parámetros configurables de sensibilidad, umbrales y perfiles de agentes (este archivo).
- Archivos adicionales de agentes como `agente_priorizacion.py`, `agente_base.py`.
