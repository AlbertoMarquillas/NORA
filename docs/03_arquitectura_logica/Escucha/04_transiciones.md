# Transiciones posibles desde el estado – Escucha

Las transiciones desde el estado **Escucha** dependen de la calidad de la entrada de voz, la respuesta del módulo `voz/`, y la supervisión de eventos internos y externos. Todas las decisiones son evaluadas por la FSM (`sistema/`), que modula el comportamiento mediante eventos estructurados.

---

| Estado destino | Evento o condición              | Origen del evento | Observaciones                                                               |
|----------------|---------------------------------|-------------------|----------------------------------------------------------------------------|
| Procesando     | `EVT_SPEECH_RECOGNIZED`         | voz/              | Reconocimiento exitoso de un comando o frase válida.                        |
| Activado       | `EVT_LISTEN_TIMEOUT`            | sistema/          | Tiempo de escucha agotado sin captar voz útil.                             |
| Error          | `EVT_MIC_FAILURE`               | voz/              | Fallo en el dispositivo o entrada de micrófono no válida.                  |
| Activado       | `CMD_CANCEL_LISTENING`          | gui/ o agentes/   | Cancelación explícita por parte del usuario o lógica contextual.           |

---

## Reglas y prioridades

- La transición a `Procesando` tiene prioridad sobre cualquier otra si se completa la decodificación de voz.
- Si `EVT_MIC_FAILURE` ocurre antes del reconocimiento, la transición a `Error` es inmediata.
- `CMD_CANCEL_LISTENING` debe ser autorizado por el agente activo para evitar cancelaciones arbitrarias.

