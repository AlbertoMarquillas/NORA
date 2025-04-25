# Ficha Funcional – `variabilidad_prosodica.py`

## Nombre del archivo:
`variabilidad_prosodica.py`

## Responsabilidad principal:
Gestionar la variación dinámica de tono, velocidad y volumen en la voz sintetizada, adaptando la prosodia de NORA según el contexto emocional y la situación del usuario. Este archivo permite que la síntesis de voz se ajuste de manera natural y expresiva, variando estos parámetros para hacer la interacción más humana y empática.

## Entradas esperadas:
- **Tipo de entrada:** Señales emocionales, parámetros de modulación de voz, instrucciones de cambio en la prosodia.
- **Fuente:** `sistema/`, `agentes/`, `voz_main.py` (para recibir eventos emocionales y parámetros de modulación).
- **Formato o protocolo:** Eventos emocionales (`EVT_EMOTION_CHANGED`), parámetros de modulación de voz en formato JSON o PCM, comandos internos (`CMD_...`).

## Salidas generadas:
- **Tipo de salida:** Modulación de la voz sintetizada (ajustes en tono, velocidad y volumen).
- **Destinatario:** `tts.py` (para aplicar la variabilidad prosódica a la síntesis de voz).
- **Ejemplo de salida:**
  - `CMD_MODULATE_VOICE` (Instrucción para aplicar cambios en tono, velocidad y volumen de la voz sintetizada).
  - `EVT_PROSODIC_VARIABILITY_APPLIED` (Evento que indica que la variabilidad prosódica ha sido aplicada correctamente a la voz).
  - `AGT_VOICE_MODULATED` (Confirmación de que la voz ha sido ajustada según la prosodia emocional del contexto).

## Módulos relacionados:
- **Entrada desde:** `sistema/` (para recibir instrucciones de modulación prosódica basadas en el contexto), `agentes/` (para recibir las variaciones emocionales que afectarán la prosodia).
- **Salida hacia:** `tts.py` (para aplicar la variabilidad prosódica a la síntesis de voz).
- **Comunicación bidireccional con:** `voz_main.py`, `sistema/` para coordinar la modulación emocional de la voz con las respuestas generadas.

## Dependencias técnicas:
- **Librerías externas:** `pyttsx3` (para la síntesis de voz y control de modulación), `pyaudio` (para la captura de audio si es necesario en algunos contextos).
- **Hardware gestionado:** Ninguno directamente (gestiona la modulación de la voz a nivel lógico).
- **Protocolos:** PCM para la captura de audio en tiempo real, eventos internos para coordinar la modulación de la voz.

## Notas adicionales:
Este archivo es crucial para que NORA sea capaz de ajustar de manera dinámica la forma en que se expresa vocalmente. La variabilidad prosódica garantiza que la síntesis de voz no sea monótona y se pueda ajustar al contexto emocional y a las interacciones del usuario. Gracias a **`variabilidad_prosodica.py`**, NORA puede reflejar emociones de manera más natural, haciendo que las respuestas vocales sean más coherentes y agradables.

## Archivos previstos del módulo:
- `variabilidad_prosodica.py`: Variación dinámica de tono, velocidad y volumen en la voz sintetizada (este archivo).
- Archivos adicionales como `tts.py`, `config_voz.py`, `voz_main.py`.
