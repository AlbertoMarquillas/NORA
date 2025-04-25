# Ficha Funcional – `ajuste_formalidad.py`

## Nombre del archivo:
`ajuste_formalidad.py`

## Responsabilidad principal:
Gestionar el ajuste del nivel de formalidad en las respuestas de NORA según el perfil del usuario, la situación o el contexto de la conversación. Este archivo se encarga de adaptar el tono y estilo del lenguaje para que las respuestas sean apropiadas, ya sea en un tono formal, semiformal o informal, dependiendo de las preferencias del usuario o del entorno conversacional.

## Entradas esperadas:
- **Tipo de entrada:** Perfil de usuario, contexto de la conversación, eventos emocionales, cambios en el tono de la interacción.
- **Fuente:** `perfil_usuario_dialogo.py` (para obtener las preferencias de formalidad del usuario), `dialogo_main.py` (para gestionar el contexto de la conversación y ajustar el tono).
- **Formato o protocolo:** Datos del perfil de usuario en formato JSON, eventos internos relacionados con la formalidad (`CMD_...`).

## Salidas generadas:
- **Tipo de salida:** Respuestas adaptadas al nivel de formalidad, ajustes en el estilo del lenguaje.
- **Destinatario:** `dialogo_main.py` (para aplicar el ajuste de formalidad en las respuestas generadas), `voz/` (para modificar el tono de voz sintetizada si es necesario).
- **Ejemplo de salida:**
  - `"¿En qué puedo asistirte hoy, estimado?"` (Respuesta formal).
  - `"¡Claro, dime qué necesitas!"` (Respuesta informal).
  - `EVT_FORMALITY_ADJUSTED` (Evento que indica que el nivel de formalidad ha sido ajustado correctamente).
  - `CMD_ADJUST_FORMALITY` (Instrucción para ajustar el nivel de formalidad en la respuesta).

## Módulos relacionados:
- **Entrada desde:** `perfil_usuario_dialogo.py` (para obtener el perfil del usuario y ajustar el estilo conversacional), `dialogo_main.py` (para recibir el contexto de la conversación y decidir el tono adecuado).
- **Salida hacia:** `dialogo_main.py` (para aplicar el ajuste de formalidad en las respuestas generadas), `voz/` (para ajustar el tono en la síntesis de voz).
- **Comunicación bidireccional con:** `sistema/`, `agentes/` para asegurar que el ajuste de formalidad sea coherente con el contexto general y el estilo de interacción del sistema.

## Dependencias técnicas:
- **Librerías externas:** `nltk`, `spacy` (para procesar y adaptar el texto de acuerdo con el nivel de formalidad).
- **Hardware gestionado:** Ninguno directamente (se maneja el ajuste de formalidad a nivel lógico).
- **Protocolos:** Comunicación basada en eventos internos, adaptación del estilo conversacional según el perfil y el contexto.

## Notas adicionales:
Este archivo es fundamental para hacer que NORA se adapte al estilo de interacción del usuario. El ajuste de formalidad permite que NORA se comunique de manera más apropiada en función de la relación con el usuario, ya sea formal en entornos profesionales o informal en interacciones más personales. Este tipo de personalización mejora la experiencia del usuario, haciendo las conversaciones más naturales y adecuadas a las diferentes situaciones.

## Archivos previstos del módulo:
- `ajuste_formalidad.py`: Adaptación del nivel de formalidad en las respuestas según perfil o situación (este archivo).
- Archivos adicionales como `dialogo_main.py`, `perfil_usuario_dialogo.py`, `nlg.py`.
