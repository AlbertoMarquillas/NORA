# Ficha Funcional – `interrupcion_semantica.py`

## Nombre del archivo:
`interrupcion_semantica.py`

## Responsabilidad principal:
Gestionar la detección de interrupciones basadas en cambios semánticos durante la conversación. Este archivo se encarga de analizar el contenido semántico de la interacción en curso para identificar cuándo es apropiado interrumpir o alterar el flujo de la conversación, mejorando la capacidad de NORA para reaccionar de forma proactiva y natural a los cambios de contexto.

## Entradas esperadas:
- **Tipo de entrada:** Texto transcrito o audio reconocido, análisis semántico de las interacciones previas.
- **Fuente:** `asr.py` (para recibir texto transcrito desde la señal de audio), `voz_main.py` (para gestionar las interacciones y detectar cambios semánticos).
- **Formato o protocolo:** Texto plano, eventos internos (`CMD_...`), configuraciones de interrupción en formato JSON.

## Salidas generadas:
- **Tipo de salida:** Instrucciones para interrumpir o cambiar el flujo de la conversación, eventos de interrupción semántica.
- **Destinatario:** `voz_main.py` (para activar la interrupción o ajustar la respuesta de voz), `sistema/`, `agentes/` (para tomar decisiones sobre la interacción en curso).
- **Ejemplo de salida:**
  - `CMD_INTERRUPT_CONVERSATION` (Instrucción para interrumpir la conversación o cambiar el flujo de respuesta).
  - `EVT_SEMANTIC_INTERRUPT` (Evento que indica que una interrupción semántica ha sido detectada y procesada).
  - `AGT_INTERRUPT_HANDLED` (Confirmación de que la interrupción semántica ha sido gestionada correctamente).

## Módulos relacionados:
- **Entrada desde:** `asr.py` (para recibir las transcripciones de voz que serán analizadas semánticamente), `voz_main.py` (para gestionar las interacciones y las posibles interrupciones).
- **Salida hacia:** `voz_main.py` (para gestionar el cambio de flujo de la conversación), `sistema/`, `agentes/` (para tomar decisiones y modificar el comportamiento de NORA).
- **Comunicación bidireccional con:** `sistema/`, `agentes/` para coordinar las interrupciones y asegurar que NORA responda adecuadamente a los cambios semánticos.

## Dependencias técnicas:
- **Librerías externas:** `nltk`, `spaCy` (para el procesamiento de lenguaje natural y el análisis semántico de las interacciones).
- **Hardware gestionado:** Ninguno directamente (se gestiona el análisis semántico a nivel lógico).
- **Protocolos:** Comunicación basada en eventos internos, análisis de contenido semántico de las interacciones.

## Notas adicionales:
Este archivo es crucial para permitir que NORA reaccione de manera adecuada a los cambios contextuales en las conversaciones. La capacidad de realizar interrupciones semánticas asegura que el sistema pueda adaptarse a cambios rápidos en el tema o flujo de la conversación, haciendo la interacción más fluida y natural. Este enfoque es clave para mejorar la experiencia del usuario, permitiendo una comunicación más eficiente y menos rígida.

## Archivos previstos del módulo:
- `interrupcion_semantica.py`: Detección de interrupciones basadas en cambios semánticos durante la conversación (este archivo).
- Archivos adicionales como `asr.py`, `voz_main.py`, `parser_comandos.py`.
