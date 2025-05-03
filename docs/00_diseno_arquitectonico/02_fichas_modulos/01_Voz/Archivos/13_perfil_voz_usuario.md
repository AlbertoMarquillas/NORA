# Ficha Funcional – `perfil_voz_usuario.py`

## Nombre del archivo:
`perfil_voz_usuario.py`

## Responsabilidad principal:
Ajustar el sistema a las características acústicas individuales del usuario. Este archivo se encarga de crear y gestionar un perfil personalizado de voz basado en las características acústicas del usuario, mejorando la precisión y la naturalidad del reconocimiento de voz (ASR) y la síntesis de voz (TTS) para el usuario individual. Además, ajusta el sistema a las variaciones en la pronunciación, tono y velocidad de habla del usuario.

## Entradas esperadas:
- **Tipo de entrada:** Datos acústicos del usuario, grabaciones de voz, características fonéticas y lingüísticas.
- **Fuente:** `asr.py` (para recibir características acústicas del usuario), grabaciones de entrenamiento o muestras de voz del usuario.
- **Formato o protocolo:** Audio en formato PCM, parámetros de perfil de voz en formato JSON, eventos internos para ajustar las características de voz.

## Salidas generadas:
- **Tipo de salida:** Ajustes en el perfil acústico del usuario, parámetros para mejorar el ASR y TTS basados en las características de la voz del usuario.
- **Destinatario:** `asr.py` (para ajustar el modelo de reconocimiento de voz a las características acústicas del usuario), `tts.py` (para personalizar la voz sintetizada según las características del usuario).
- **Ejemplo de salida:**
  - `EVT_USER_VOICE_PROFILE_UPDATED` (Evento que indica que el perfil de voz del usuario ha sido actualizado).
  - `CMD_UPDATE_VOICE_PROFILE` (Instrucción para aplicar el perfil acústico actualizado a los sistemas de ASR y TTS).
  - `AGT_PROFILE_ADJUSTED` (Confirmación de que el perfil de voz ha sido ajustado y aplicado correctamente).

## Módulos relacionados:
- **Entrada desde:** `asr.py` (para recibir datos de audio del usuario y sus características acústicas), `tts.py` (para aplicar los ajustes personalizados en la síntesis de voz).
- **Salida hacia:** `asr.py`, `tts.py` (para aplicar los ajustes en el modelo de voz y la síntesis de voz).
- **Comunicación bidireccional con:** `sistema/`, `agentes/` para asegurar que el perfil de voz se adapte correctamente en todas las interacciones del sistema.

## Dependencias técnicas:
- **Librerías externas:** `librosa` (para la extracción de características acústicas de las grabaciones de voz), `numpy`, `scipy` (para el procesamiento de señales de audio y la normalización).
- **Hardware gestionado:** Micrófono USB (para capturar las muestras de voz del usuario), altavoces o salida de audio para la reproducción personalizada.
- **Protocolos:** PCM para la captura de audio, eventos internos para manejar la adaptación del perfil de voz.

## Notas adicionales:
Este archivo es crucial para personalizar la interacción de NORA con el usuario, adaptando tanto el reconocimiento de voz como la síntesis de voz a las características individuales del usuario. El perfil de voz permitirá que el sistema sea más preciso al reconocer comandos y más natural al generar respuestas, ajustándose a las particularidades del habla de cada usuario, lo que mejora la interacción y la experiencia de uso.

## Archivos previstos del módulo:
- `perfil_voz_usuario.py`: Ajuste del sistema a características acústicas individuales del usuario (este archivo).
- Archivos adicionales como `asr.py`, `tts.py`, `voz_main.py`.
