# Condiciones de entrada – Estado: Activado

El sistema NORA entra en el estado **Activado** cuando se cumplen una o más de las siguientes condiciones de activación, verificadas mediante eventos estructurados del sistema o inferencias de agentes perceptivos:

---

## 1. Evento directo de activación

- **`EVT_NFC_ACTIVATE`**  
  Emisión desde el módulo `sensores/` tras lectura válida de un identificador NFC mediante el PN532.  
  Validado por el módulo `activacion/` y, opcionalmente, por agentes de identificación si el perfil está registrado.

- **`EVT_WAKEWORD`**  
  Evento generado por el módulo `voz/` al detectar la palabra clave definida (ej: “oye NORA”) mediante hotword detector en segundo plano.

---

## 2. Evaluación combinada de contexto

- **`EVT_ATTENTION_GAINED`**  
  Emisión desde el módulo `vision/`, indicando que el usuario ha dirigido su atención visual hacia el asistente.  
  La transición se permite si la atención es sostenida durante un umbral mínimo (`attention_sustain_threshold`) evaluado por agentes visuales.

- **`EVT_PRESENCE_CONFIRMED` + `EVT_ENV_OK`**  
  Detección de presencia física (sensor ultrasónico) junto a validación ambiental básica (temperatura, luminosidad, etc.).  
  Esta condición debe ser confirmada por un agente de contexto (`/agentes/`) para evitar falsos positivos.

---

## 3. Transición FSM desde Reposo

- **`STATE_REPOSO → STATE_ACTIVADO`**  
  La FSM `sistema/` permite esta transición si se recibe al menos uno de los eventos anteriores, el sistema no está ocupado (`STATE_BUSY = False`), y no se detectan inhibiciones activas (`CMD_INHIBIR_ACTIVACION`).

---

## Consideraciones adicionales

- Las condiciones de entrada pueden depender del perfil del usuario. Por ejemplo, un perfil configurado en modo “privado” puede requerir una validación NFC antes de permitir transición por atención visual o voz.
- El sistema de agentes puede modificar dinámicamente los umbrales de activación (tiempo, intensidad, combinatoria de señales) según historial, horario o contexto ambiental.
