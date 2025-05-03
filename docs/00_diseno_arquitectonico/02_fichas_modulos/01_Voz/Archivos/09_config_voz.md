# Ficha Funcional – `config_voz.py`

## Nombre del archivo:
`config_voz.py`

## Responsabilidad principal:
Definir y gestionar los parámetros configurables del módulo de voz dentro del sistema NORA. Este archivo permite la personalización de los comportamientos de los componentes de voz, como el idioma, la sensibilidad de los modelos de ASR y TTS, y la configuración de motores de síntesis de voz. Facilita la adaptación del sistema a diferentes entornos y preferencias del usuario.

## Entradas esperadas:
- **Tipo de entrada:** Parámetros de configuración (idioma, sensibilidad, motores de TTS).
- **Fuente:** Archivos de configuración (`config.json` o similares), entradas del usuario, módulos de voz que requieren ajustes de configuración.
- **Formato o protocolo:** Archivos de configuración JSON, comandos internos de actualización de configuración.

## Salidas generadas:
- **Tipo de salida:** Actualización de configuraciones, parámetros ajustados para el ASR y TTS, cambios en las configuraciones globales.
- **Destinatario:** `asr.py`, `tts.py`, `voz_main.py`, `sistema/`, `agentes/` (para aplicar las configuraciones ajustadas).
- **Ejemplo de salida:**
  - `EVT_CONFIG_UPDATED` (Evento que indica que las configuraciones han sido actualizadas).
  - `CMD_UPDATE_CONFIGURATION` (Instrucción para aplicar la nueva configuración del sistema).
  - `AGT_VOICE_PARAMS_UPDATED` (Confirmación de que los parámetros de voz han sido actualizados correctamente).

## Módulos relacionados:
- **Entrada desde:** Archivos de configuración (`config.json`), parámetros definidos por el usuario, eventos de actualización del sistema.
- **Salida hacia:** `asr.py`, `tts.py`, `voz_main.py`, `agentes/` (para aplicar las configuraciones a los módulos correspondientes).
- **Comunicación bidireccional con:** `sistema/`, `agentes/` para asegurar que las configuraciones sean consistentes con el comportamiento global de NORA.

## Dependencias técnicas:
- **Librerías externas:** `json` (para leer y escribir archivos de configuración), `pyaudio`, `pyttsx3` (para los motores de ASR y TTS).
- **Hardware gestionado:** Ninguno directamente (gestiona la configuración de los motores de voz).
- **Protocolos:** Comunicación basada en eventos internos, carga y aplicación de configuraciones dinámicas.

## Notas adicionales:
Este archivo es fundamental para configurar el comportamiento de voz dentro del sistema NORA. Al permitir la modificación de parámetros como el idioma, la sensibilidad de los motores de ASR y TTS, y la personalización de las respuestas vocales, `config_voz.py` hace que el sistema sea adaptable a diferentes entornos, condiciones acústicas y preferencias del usuario. Es un archivo clave para mejorar la interacción y la experiencia auditiva con el sistema.

## Archivos previstos del módulo:
- `config_voz.py`: Parámetros configurables del módulo (idioma, sensibilidad, motores de TTS) (este archivo).
- Archivos adicionales como `asr.py`, `tts.py`, `voz_main.py`.
