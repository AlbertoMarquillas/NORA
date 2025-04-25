# Ficha Funcional – `escenas_expresivas.py`

## Nombre del archivo:
`escenas_expresivas.py`

## Responsabilidad principal:
Definir y gestionar las combinaciones sincronizadas de respuestas físicas, visuales y verbales en el sistema NORA. Este archivo se encarga de coordinar las distintas expresiones del sistema (gestos, expresiones faciales, respuestas vocales) para crear respuestas más naturales y coherentes a los eventos que afectan el sistema.

## Entradas esperadas:
- **Tipo de entrada:** Eventos de interacción del usuario, cambios en el estado emocional o contexto.
- **Fuente:** Módulos como `agentes/`, `voz/`, `interfaz/`, `vision/`, que generan eventos relacionados con las emociones, la atención y las interacciones del usuario.
- **Formato o protocolo:** Eventos de percepción (`EVT_EMOTION_CHANGED`, `EVT_ATTENTION_GAINED`), eventos de interacción con el sistema (`EVT_USER_INTERACTION`).

## Salidas generadas:
- **Tipo de salida:** Instrucciones para coordinar expresiones visuales, auditivas y físicas del sistema de manera sincronizada.
- **Destinatario:** `interfaz/` (para actualizar las expresiones visuales y los movimientos físicos), `voz/` (para generar una respuesta vocal sincronizada con las expresiones físicas y visuales).
- **Ejemplo de salida:**
  - `AGT_SYNCHRONIZE_EXPRESSIONS` (Instrucción para sincronizar las respuestas físicas, visuales y verbales).
  - `CMD_PLAY_SCENE` (Instrucción para ejecutar una escena expresiva, como un saludo o una respuesta empática).
  - `AGT_EMOTIONAL_EXPRESSION` (Evento que ajusta las expresiones visuales y vocales de acuerdo con el estado emocional detectado).

## Módulos relacionados:
- **Entrada desde:** `agentes/` (información sobre el estado emocional y la atención del usuario), `voz/` (respuestas vocales), `interfaz/` (movimientos físicos y visuales de NORA).
- **Salida hacia:** `interfaz/` (para actualizar las expresiones visuales y movimientos), `voz/` (para generar una respuesta vocal sincronizada), `agentes/` (para asegurar que las respuestas sean coherentes).
- **Comunicación bidireccional con:** `agentes/`, `sistema/`, `voz/`, `interfaz/` para coordinar respuestas multimodales y generar escenas expresivas.

## Dependencias técnicas:
- **Librerías externas:** `Pillow` (para gestionar las expresiones visuales de la pantalla), `PyGame` o `Tkinter` (para crear animaciones o gestos), `pyttsx3` (para síntesis de voz).
- **Hardware gestionado:** Ninguno directamente (se maneja a nivel lógico).
- **Protocolos:** Comunicación basada en eventos internos, sincronización de respuestas físicas, visuales y vocales.

## Notas adicionales:
Este archivo es crucial para hacer que las respuestas de NORA sean más naturales y coherentes, proporcionando interacciones que combinan expresiones visuales, vocales y físicas. Al coordinar estas respuestas, NORA puede crear una experiencia más inmersiva y empática para el usuario. Las escenas expresivas pueden ser predefinidas o generadas dinámicamente en función de los eventos y el estado emocional del usuario.

## Archivos previstos del módulo:
- `escenas_expresivas.py`: Definición de combinaciones sincronizadas de expresión física, visual y verbal (este archivo).
- Archivos adicionales de agentes como `agente_emocional.py`, `agente_base.py`.
