# Acciones realizadas – Estado: Activado

Durante el estado **Activado**, NORA ejecuta un conjunto de acciones orientadas a la preparación operacional del sistema y al monitoreo pasivo del entorno, manteniéndose a la espera de eventos que habiliten una transición hacia estados interactivos. Este estado implica un cambio de contexto desde la pasividad energética al modo de disponibilidad activa, sin iniciar aún un ciclo conversacional.

---

## 1. Inicialización de subsistemas activos

- Activación no intensiva de los módulos `voz/`, `vision/` y `sensores/` en modo de espera (`standby-ready`).
- Confirmación de estado operativo por parte del módulo `control/`, incluyendo supervisión básica de temperatura, carga del sistema, y estado de red local.

---

## 2. Preparación de canales expresivos

- Módulo `interfaz/`: visualización de un rostro neutro o gesto simbólico de atención (ej: ojos abiertos, parpadeo lento).
- Iluminación de LEDs RGB en color fijo (ej: azul suave o blanco tenue) para indicar disponibilidad.
- Posicionamiento inicial de servomotores si se emplean gestos de "despertar" (opcional).

---

## 3. Evaluación de contexto

- Recepción continua de eventos `EVT_PRESENCE_CONFIRMED`, `EVT_ATTENTION_GAINED`, `EVT_ENV_STATE`.
- Delegación de análisis contextual al módulo `/agentes/` para determinar si se cumplen las condiciones para transición a estados `Escucha` o `Atencion`.

---

## 4. Registro y logging

- Emisión del evento `EVT_STATE_CHANGED` hacia el sistema de logging (`control/`) y almacenamiento en `datos/`.
- Inicio del temporizador de inactividad (`inactivity_timer_start`) para evaluar posibles transiciones a `Reposo`.

---

## 5. Reglas internas y comportamiento

- No se ejecuta síntesis de voz ni interpretación de comandos en este estado.
- No se inicia seguimiento facial ni análisis de emociones hasta que se entre en `Escucha` o `Atencion`.
- El sistema puede responder a eventos de emergencia o diagnóstico sin salir del estado.

---

## Indicadores activos del sistema

| Componente        | Estado durante Activado               |
|-------------------|----------------------------------------|
| Micrófono         | Inicializado, en espera de señal       |
| Cámara            | En modo de previsualización pasiva     |
| Pantalla OLED/TFT | Expresión neutra                       |
| LEDs RGB          | Color suave continuo (ej. azul claro)  |
| Servomotores      | Posición base (mirada al frente)       |
