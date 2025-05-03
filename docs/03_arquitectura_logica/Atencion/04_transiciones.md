# Transiciones posibles desde el estado – Atencion

Las siguientes transiciones pueden producirse desde el estado **Atencion**, en función de eventos percibidos, acciones del usuario o fallos del sistema. La FSM `sistema/` gestiona estas transiciones, y los agentes (`/agentes/`) pueden intervenir para modular su prioridad o viabilidad.

---

| Estado destino | Evento o condición                | Origen del evento  | Observaciones                                                             |
|----------------|-----------------------------------|---------------------|---------------------------------------------------------------------------|
| Escucha        | `EVT_SPEECH_START`                | voz/                | Entrada de voz válida, posterior al contacto visual sostenido.            |
| Procesando     | `EVT_GESTURE_COMMAND`             | vision/             | Interpretación de gesto como comando directo.                             |
| Activado       | `EVT_ATTENTION_LOST`              | vision/             | El contacto visual se interrumpe antes de iniciar interacción.            |
| Error          | `EVT_CAMERA_FAILURE`              | control/, vision/   | Fallo crítico de cámara o pérdida continua del tracking facial.           |

---

## Notas

- La transición a `Procesando` sin pasar por `Escucha` solo está permitida si el sistema soporta reconocimiento de gestos predefinidos.
- La duración máxima del estado `Atencion` está definida por `T_ATTENTION_MAX` (recomendado: 10–15 segundos).
- Si se superpone `EVT_SPEECH_START` con `EVT_ATTENTION_LOST`, el sistema prioriza la voz si la señal es suficientemente confiable (`VAD_CONFIDENCE > threshold`).
