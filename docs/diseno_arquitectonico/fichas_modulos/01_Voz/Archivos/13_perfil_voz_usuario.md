# Ficha Específica – `perfil_voz_usuario.py`

## Nombre del archivo:
`perfil_voz_usuario.py`

## Responsabilidad principal:
Ajustar el sistema de procesamiento de voz a las características acústicas individuales de cada usuario registrado, mejorando la precisión del reconocimiento de voz y adaptando la síntesis TTS de forma personalizada.

## Entradas esperadas:
- Datos de audio del usuario (capturados previamente o en sesiones de entrenamiento).
- Configuraciones dinámicas (preferencias de voz, sensibilidad personalizada, perfil acústico).

## Salidas generadas:
- Perfil acústico personalizado (umbral de sensibilidad, adaptaciones específicas).
- Ajustes aplicados al ASR y TTS basados en el perfil del usuario.

## Funcionalidades principales:
- Extracción de características individuales (tono medio, velocidad de habla, rango dinámico).
- Generación de perfiles acústicos para usuarios conocidos.
- Aplicación de ajustes de preprocesamiento adaptativo en ASR (normalización específica).
- Selección de voces personalizadas para TTS.
- Actualización progresiva del perfil basado en nuevos datos de interacción.

## Dependencias técnicas:
- `numpy`, `scipy` – Procesamiento de señales de audio.
- `sounddevice`, `pyaudio` – Captura de audio para perfiles.
- `json` – Almacenamiento de configuraciones de perfil de usuario.

