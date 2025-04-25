# Ficha Funcional – `parser_comandos.py`

## Nombre del archivo:
`parser_comandos.py`

## Responsabilidad principal:
Procesar y extraer comandos estructurados a partir del texto reconocido por el sistema NORA. Este archivo se encarga de interpretar el texto transcrito (por ejemplo, desde el ASR o desde el análisis del diálogo), identificar las intenciones del usuario y extraer comandos específicos que el sistema debe ejecutar, como peticiones, solicitudes o instrucciones.

## Entradas esperadas:
- **Tipo de entrada:** Texto reconocido del habla o texto ingresado por el usuario.
- **Fuente:** `asr.py` (para recibir texto transcrito del habla), `dialogo/` (para recibir entradas de texto en una conversación).
- **Formato o protocolo:** Texto plano, eventos de control para estructurar el comando (`CMD_...`).

## Salidas generadas:
- **Tipo de salida:** Comandos estructurados extraídos del texto, eventos de interpretación de comandos.
- **Destinatario:** `voz_main.py`, `sistema/`, `interfaz/`, `agentes/` (para ejecutar los comandos interpretados).
- **Ejemplo de salida:**
  - `EVT_COMMAND_PARSED` (Evento que indica que se ha extraído un comando válido del texto).
  - `CMD_EXECUTE_COMMAND` (Instrucción para ejecutar el comando extraído del texto).
  - `AGT_COMMAND_INTERPRETED` (Confirmación de que un comando ha sido correctamente interpretado y está listo para ejecutarse).

## Módulos relacionados:
- **Entrada desde:** `asr.py` (para recibir texto transcrito), `dialogo/` (para procesar entradas de texto y generar comandos).
- **Salida hacia:** `voz_main.py` (para enviar los comandos que deben ser procesados y ejecutados), `sistema/`, `interfaz/`, `agentes/` (para ejecutar los comandos relacionados con las acciones del sistema).
- **Comunicación bidireccional con:** `sistema/`, `agentes/`, `interfaz/` para coordinar la ejecución de comandos y asegurarse de que el sistema responda adecuadamente a los comandos.

## Dependencias técnicas:
- **Librerías externas:** `spacy`, `nltk` o `transformers` (para el procesamiento del lenguaje natural y la extracción de comandos).
- **Hardware gestionado:** Ninguno directamente (gestiona el análisis de texto y la extracción de comandos).
- **Protocolos:** Comunicación basada en eventos internos, análisis de texto para extraer las intenciones y los comandos.

## Notas adicionales:
Este archivo es esencial para interpretar correctamente las entradas de texto y convertirlas en comandos ejecutables por NORA. Utilizando procesamiento de lenguaje natural (PLN), `parser_comandos.py` permite que NORA entienda lo que el usuario desea hacer con el texto que ha pronunciado o escrito. Esto es clave para permitir una interacción fluida y eficiente en el sistema de control por voz de NORA.

## Archivos previstos del módulo:
- `parser_comandos.py`: Extracción estructurada de comandos desde el texto (este archivo).
- Archivos adicionales como `asr.py`, `voz_main.py`, `eventos_voz.py`.
