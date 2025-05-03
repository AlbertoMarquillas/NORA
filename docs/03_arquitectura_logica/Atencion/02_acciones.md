# Acciones realizadas – Estado: Atencion

Durante el estado **Atencion**, NORA ejecuta acciones específicas orientadas a establecer una sintonía visual con el usuario, optimizar la percepción contextual y preparar la transición hacia estados de interacción verbal (`Escucha`) o procesamiento directo (`Procesando`).

---

## 1. Focalización visual y postural

- Activación del seguimiento facial mediante el módulo `vision/`, ajustando la posición de la cámara y los servomotores (si están presentes) para mantener el rostro centrado.
- Control activo de los ejes de movimiento (servo-pan, servo-tilt) para mantener alineación suave y natural.
- Actualización continua de la posición relativa del usuario y su distancia.

---

## 2. Ajustes expresivos

- El módulo `interfaz/` muestra una expresión facial receptiva (mirada fija, gesto neutro activo).
- LEDs RGB indican modo de atención (por ejemplo, blanco cálido estático o animación de pulso lento).
- Opcional: emisión de un breve gesto no verbal (parpadeo, inclinación de cabeza) si la atención se mantiene.

---

## 3. Sensibilización de entrada auditiva

- El módulo `voz/` se prepara para transición a `Escucha`, ajustando parámetros del detector de actividad de voz (VAD).
- Activación de temporizador de pre-escucha si se detectan movimientos labiales o signos de inminente vocalización.

---

## 4. Evaluación contextual

- Los agentes (`/agentes/`) analizan métricas contextuales para determinar la intención del usuario, basándose en:
  - Persistencia de la atención
  - Estado emocional estimado (si visión lo permite)
  - Historial reciente de interacción

---

## 5. Gestión de estados internos

- Se detiene el temporizador de inactividad global (`inactivity_timer_stop`).
- Se emite el evento `EVT_STATE_CHANGED` hacia el sistema de log (`control/`) y `datos/`.
- Se monitorean eventos inhibidores: `CMD_CANCEL_ATTENTION`, `EVT_DISTRACTION_DETECTED`.

---

## Indicadores activos del sistema

| Componente        | Estado durante Atencion                  |
|-------------------|-------------------------------------------|
| Cámara            | Seguimiento facial activo                |
| Servos            | Movimiento adaptativo continuo           |
| Pantalla facial   | Expresión de atención no verbal          |
| LEDs RGB          | Color cálido o pulso suave               |
| Micrófono         | Inicializado, sensibilidad aumentada     |
