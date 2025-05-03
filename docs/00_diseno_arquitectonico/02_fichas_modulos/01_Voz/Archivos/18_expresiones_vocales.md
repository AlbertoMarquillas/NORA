# Ficha Funcional – `expresiones_vocales.py`

## Nombre del archivo:
`expresiones_vocales.py`

## Responsabilidad principal:
Gestionar la inserción de expresiones vocales naturales, como suspiros, risas, pausas emocionales y otros sonidos que mejoran la naturalidad de la síntesis de voz (TTS). Este archivo se encarga de enriquecer las respuestas de NORA con expresiones auditivas que reflejan emociones o reacciones del sistema, haciendo que las respuestas vocales sean más humanas y dinámicas.

## Entradas esperadas:
- **Tipo de entrada:** Comandos para insertar expresiones vocales, parámetros emocionales, instrucciones de modulación de voz.
- **Fuente:** `sistema/`, `voz_main.py`, `agentes/` (para recibir instrucciones sobre qué tipo de expresión vocal insertar en la respuesta).
- **Formato o protocolo:** Eventos de control (`CMD_INSERT_VOCAL_EXPRESSION`), parámetros emocionales en formato JSON.

## Salidas generadas:
- **Tipo de salida:** Expresiones vocales insertadas en la voz sintetizada, como suspiros, risas, o pausas naturales.
- **Destinatario:** `tts.py` (para insertar las expresiones vocales en la salida de voz sintetizada).
- **Ejemplo de salida:**
  - `CMD_INSERT_EXPRESSION` (Instrucción para insertar una expresión vocal, como un suspiro o una risa, en la salida de voz).
  - `EVT_VOCAL_EXPRESSION_INSERTED` (Evento que confirma que la expresión vocal ha sido correctamente insertada en la síntesis de voz).
  - `AGT_VOCAL_EXPRESSIONS` (Confirmación de que las expresiones vocales se han aplicado correctamente en la respuesta generada).

## Módulos relacionados:
- **Entrada desde:** `voz_main.py` (para recibir instrucciones sobre cuándo insertar expresiones vocales en las respuestas de NORA).
- **Salida hacia:** `tts.py` (para aplicar las expresiones vocales a la voz sintetizada).
- **Comunicación bidireccional con:** `sistema/`, `agentes/` para coordinar la inserción de expresiones vocales con la modulación emocional del sistema.

## Dependencias técnicas:
- **Librerías externas:** `pyttsx3` (para la síntesis de voz y el control de modulación), `pyaudio` (para la captura y la manipulación del audio generado).
- **Hardware gestionado:** Ninguno directamente (se gestiona la modulación de voz a nivel lógico).
- **Protocolos:** PCM para la captura y reproducción de audio, eventos internos para coordinar las expresiones vocales.

## Notas adicionales:
Este archivo es clave para darle a NORA una voz más expresiva y natural. La inserción de expresiones vocales, como suspiros, risas o pausas, mejora la interacción con el usuario, haciendo que las respuestas de voz sean más humanas y emocionalmente adaptativas. Además, al integrar estas expresiones de manera dinámica, el sistema puede reaccionar de forma más empática a diferentes situaciones.

## Archivos previstos del módulo:
- `expresiones_vocales.py`: Inserción de expresiones auditivas naturales (suspiros, risas) en la síntesis de voz (este archivo).
- Archivos adicionales como `tts.py`, `voz_main.py`, `config_voz.py`.
