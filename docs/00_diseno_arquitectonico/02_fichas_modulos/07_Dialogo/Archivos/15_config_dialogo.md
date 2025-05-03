# Ficha Funcional – `config_dialogo.py`

## Nombre del archivo:
`config_dialogo.py`

## Responsabilidad principal:
Gestionar la configuración de los parámetros del sistema de diálogo de NORA, permitiendo la personalización de los modelos, los parámetros de respuesta, la longitud máxima de las respuestas y la sensibilidad del sistema ante distintos tipos de entradas. Este archivo es crucial para ajustar el comportamiento de NORA en función de diferentes contextos, preferencias del usuario y necesidades del sistema.

## Entradas esperadas:
- **Tipo de entrada:** Parámetros de configuración (modelo de NLU, longitud de respuestas, sensibilidad).
- **Fuente:** Archivos de configuración (`config.json` o similares), entradas del usuario, módulos de diálogo que requieren ajustes de comportamiento.
- **Formato o protocolo:** Archivos de configuración JSON, configuraciones internas de parámetros de diálogo.

## Salidas generadas:
- **Tipo de salida:** Configuraciones ajustadas para el sistema de diálogo, parámetros actualizados para el procesamiento de texto y la respuesta.
- **Destinatario:** `dialogo_main.py` (para aplicar las configuraciones del sistema de diálogo), `nlu.py`, `nlg.py` (para gestionar los parámetros de los modelos de lenguaje natural).
- **Ejemplo de salida:**
  - `EVT_DIALOGUE_CONFIG_UPDATED` (Evento que indica que la configuración del sistema de diálogo ha sido actualizada).
  - `CMD_UPDATE_DIALOGUE_PARAMS` (Instrucción para actualizar los parámetros de diálogo según las nuevas configuraciones).
  - `AGT_CONFIG_UPDATED` (Confirmación de que los parámetros configurables han sido actualizados correctamente).

## Módulos relacionados:
- **Entrada desde:** Archivos de configuración, configuraciones definidas por el sistema (`sistema/`), eventos internos del sistema.
- **Salida hacia:** `dialogo_main.py` (para aplicar las configuraciones de diálogo al flujo de conversación), `nlu.py`, `nlg.py` (para adaptar los modelos de lenguaje natural).
- **Comunicación bidireccional con:** `sistema/`, `agentes/` para asegurar que las configuraciones sean coherentes con el comportamiento general del sistema.

## Dependencias técnicas:
- **Librerías externas:** `json` (para leer y escribir archivos de configuración), `nltk`, `spacy` (para el procesamiento de texto y ajuste de parámetros de respuesta).
- **Hardware gestionado:** Ninguno directamente (se maneja la configuración a nivel lógico).
- **Protocolos:** Comunicación basada en eventos internos, carga y aplicación de configuraciones dinámicas.

## Notas adicionales:
Este archivo es esencial para permitir que el sistema de diálogo de NORA sea flexible y adaptable. **`config_dialogo.py`** permite cambiar el comportamiento del sistema de acuerdo con el contexto o las necesidades del usuario, como ajustar la sensibilidad, la longitud de las respuestas o el modelo utilizado para la interpretación y generación del lenguaje natural. Es fundamental para mantener la coherencia y personalización en las interacciones, adaptando el sistema a diversas situaciones.

## Archivos previstos del módulo:
- `config_dialogo.py`: Configuración de modelos, parámetros de respuesta, longitud máxima, sensibilidad (este archivo).
- Archivos adicionales como `dialogo_main.py`, `nlg.py`, `nlu.py`.
