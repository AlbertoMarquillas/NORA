## 04. `sintetizador.py` – Módulo de salida de voz (TTS)

**Ubicación:** `software/src/voz/sintetizador.py`

**Rol en el sistema:**
Este módulo contiene la clase `SintetizadorVoz`, responsable de generar respuesta hablada mediante síntesis de texto a voz (TTS). Utiliza la librería `pyttsx3` para funcionar offline y multiplataforma.

---

### ✳️ Funcionalidad principal
- Se suscribe automáticamente al evento `EVT_DECIR_TEXTO` cuando se instancia.
- Al recibir un evento, extrae el campo `texto` y lo verbaliza.
- Informa en consola del contenido emitido.

---

### 🔗 Dependencias
- `pyttsx3`: motor de síntesis de voz
- `Evento` desde `event_manager`

---

### 🧩 Lógica de operación
```python
if texto:
    self.engine.say(texto)
    self.engine.runAndWait()
```
Esto convierte el texto a voz en tiempo real de forma sincrónica.

---

### 📌 Observaciones
- Es una pieza clave en el ciclo entrada-procesamiento-salida.
- Permite interacción verbal completa en simulación.
- Puede ser sustituido por motores más avanzados (Whisper, ElevenLabs, etc.)
- Compatible con cualquier plataforma que soporte `pyttsx3`.

