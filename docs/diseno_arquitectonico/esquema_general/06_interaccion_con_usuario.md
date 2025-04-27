# 06 – Paso a paso de la interacción del usuario con NORA

Este documento detalla el flujo completo de interacción del usuario con el sistema NORA, desde la percepción inicial hasta la respuesta del asistente. Está basado en los documentos de hardware, software y relaciones funcionales del sistema, con el objetivo de proporcionar una visión clara, estructurada y ejecutable de cada etapa del ciclo usuario ↔ sistema.

---

## 1. Inicio: presencia del usuario

**Condición inicial:** NORA se encuentra en estado `ESPERA` o `REPOSO`.

### Posibles disparadores:
- Usuario se aproxima (detectado por el sensor ultrasónico HC-SR04 → `sensores/`).
- Usuario se posiciona delante de la cámara → `vision/` detecta rostro (`EVT_FACE_DETECTED`).
- Usuario activa por **NFC**, **botón físico** o **hotword** → `activacion/` emite `EVT_ACTIVATION_TRIGGERED`.

**Procesamiento:**
- `activacion/` agrupa señales de activación y las valida (por tiempo o simultaneidad).
- Se lanza `EVT_SYSTEM_WAKE` hacia `sistema/`, que cambia a estado `ACTIVO` o `INTERACTIVO`.


---

## 2. Inicio de interacción verbal o gestual

### A. Por voz:
- Usuario pronuncia una frase.
- `voz/` captura el audio con el micrófono → módulo ASR lo convierte en texto (`EVT_SPEECH_RECOGNIZED`).
- Se analiza emoción en voz → genera eventos como `EVT_EMOTION_VOICE_HAPPY`.

### B. Por gestos / visual:
- `vision/` detecta orientación, gesto o emoción facial (`EVT_ATTENTION_GAINED`, `EVT_GESTURE_WAVE`, `EVT_EMOTION_CHANGED`).
- Estos eventos se reenvían a `agentes/` para interpretación.

**Procesamiento:**
- `agentes/` modulan la atención, priorizan el tipo de entrada.
- `sistema/` define el estado interno y pasa el texto/parámetro a `dialogo/` si es una frase.


---

## 3. Procesamiento semántico y contextual

- El texto reconocido se envía a `dialogo/`.
- `dialogo/` interpreta la intención (NLU), consulta contexto, historial o perfil.
- Opcional: consulta `datos/` si se requiere información persistente (rutinas, agenda).
- Se genera una respuesta textual (`EVT_DIALOGUE_RESPONSE`).


---

## 4. Respuesta multimodal del sistema

### A. Canal auditivo
- `voz/` convierte el texto en audio (TTS) → se reproduce por altavoz.

### B. Canal visual y expresivo
- `interfaz/` muestra expresión facial (pantalla), color emocional (LEDs RGB) y gestos físicos (servos).
- `agentes/` pueden modular tono, expresión, sincronización de salida.

### Resultado:
- El usuario recibe una respuesta hablada, visualmente reforzada y emocionalmente expresiva.


---

## 5. Cierre o continuación del ciclo

### A. Continuación:
- Si el usuario responde, se mantiene el estado `INTERACTIVO`.
- Se reinicia el ciclo de percepción de voz o visión.

### B. Cierre:
- Si no hay input durante un tiempo (`TIMEOUT_INTERACCION`), se genera `EVT_IDLE_TIMEOUT`.
- `sistema/` transita a `ESPERA`, `REPOSO` o `SUSPENDIDO`.
- `interfaz/` apaga expresión, LEDs o pantalla.

---

## 6. Visualización en diagrama

Este flujo se representa gráficamente en el archivo:

- `diagrama_nora_interaccion.drawio`
- `diagrama_nora_interaccion.png`
- `diagrama_nora_interaccion.pdf`

Ubicación: `docs/diagramas/`

---

## 7. Conclusión

El sistema NORA sigue un modelo de interacción **reactiva-multimodal**, donde la presencia y los estímulos del usuario desencadenan respuestas coherentes y emocionalmente moduladas. Este flujo garantiza que la experiencia sea natural, adaptativa y comprensible tanto para el usuario como para los desarrolladores que lo implementan.