# Ficha Funcional – `modelo_asr_loader.py`

## Nombre del archivo:
`modelo_asr_loader.py`

## Responsabilidad principal:
Gestionar la carga de modelos de Reconocimiento Automático del Habla (ASR) personalizados o adaptativos dentro del sistema NORA. Este archivo permite cargar modelos de ASR preentrenados, configurarlos según el entorno y las necesidades del sistema, y adaptarlos progresivamente a los patrones de habla del usuario, mejorando la precisión del reconocimiento de voz.

## Entradas esperadas:
- **Tipo de entrada:** Parámetros de configuración del modelo, modelos ASR preentrenados o personalizados.
- **Fuente:** Archivos de modelo de ASR, configuraciones de usuario o sistema (`config_voz.py`).
- **Formato o protocolo:** Modelos de ASR en formato binario o JSON, configuraciones de parámetros de modelo.

## Salidas generadas:
- **Tipo de salida:** Carga de modelos de ASR, eventos de éxito o error en la carga del modelo.
- **Destinatario:** `asr.py` (para utilizar el modelo cargado en el proceso de reconocimiento de voz).
- **Ejemplo de salida:**
  - `EVT_MODEL_LOADED` (Evento que indica que un modelo de ASR ha sido cargado correctamente).
  - `CMD_LOAD_MODEL` (Instrucción para cargar un modelo ASR específico).
  - `AGT_MODEL_ERROR` (Evento que indica un error al intentar cargar un modelo ASR).

## Módulos relacionados:
- **Entrada desde:** Archivos de modelo de ASR, configuraciones del sistema (`config_voz.py`).
- **Salida hacia:** `asr.py` (para aplicar el modelo de ASR cargado en el reconocimiento de voz).
- **Comunicación bidireccional con:** `voz_main.py`, `asr.py` para asegurar que el modelo cargado se integre correctamente en el sistema de reconocimiento de voz.

## Dependencias técnicas:
- **Librerías externas:** `vosk`, `whisper`, `pyaudio` (para trabajar con modelos de ASR y audio).
- **Hardware gestionado:** Ninguno directamente (gestiona el modelo de ASR a nivel lógico).
- **Protocolos:** PCM para captura de audio, eventos internos para gestionar la carga y el uso del modelo de ASR.

## Notas adicionales:
Este archivo es esencial para permitir la personalización y adaptación del sistema NORA al reconocimiento de voz. A través de `modelo_asr_loader.py`, el sistema puede cargar diferentes modelos de ASR, permitiendo una mayor precisión en la transcripción del habla, especialmente cuando se utilizan modelos personalizados o adaptativos para mejorar la comprensión de un usuario específico. Este enfoque también facilita el soporte de varios idiomas y variaciones en la pronunciación o el acento.

## Archivos previstos del módulo:
- `modelo_asr_loader.py`: Carga de modelos de ASR personalizados o adaptativos (este archivo).
- Archivos adicionales como `asr.py`, `voz_main.py`, `config_voz.py`.
