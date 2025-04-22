## 03. `interfaz.py` – Representación visual simbólica del estado

**Ubicación:** `software/src/interfaz/interfaz.py`

**Rol en el sistema:**
Este módulo define la clase `InterfazSimulada`, encargada de representar de forma visual (en consola) los eventos y estados funcionales de NORA mediante símbolos y mensajes. Es la interfaz visual simbólica del asistente en modo de simulación.

---

### ✳️ Funcionalidad principal
- Se suscribe a eventos del sistema para representar cambios de estado o reacciones.
- Muestra iconos (emojis) y mensajes según el tipo de evento recibido.
- Proporciona retroalimentación simbólica que acompaña la voz y el comportamiento del asistente.

---

### 🔗 Eventos gestionados
- `EVT_COMMAND_RECOGNIZED`
- `EVT_COMMAND_UNKNOWN`
- `EVT_IDLE_TIMEOUT`
- `EVT_FACE_DETECTED`
- `EVT_NFC_ACTIVATE`
- `EVT_SHUTDOWN_REQUEST`
- `EVT_MOSTRAR_ESTADO`

---

### 🧩 Lógica de visualización
Para cada tipo de evento o estado, se asocia un emoji y una frase descriptiva. Ejemplo:
- 👂 Presencia detectada
- 🟢 Comando ejecutado correctamente
- ❓ Comando no reconocido
- 💤 Estado REPOSO

Estos mensajes aparecen por consola junto con los eventos, generando una sensación de expresividad.

---

### 📌 Observaciones
- Aunque simple, este módulo es fundamental para el feedback visual sin hardware.
- En el futuro podría evolucionar hacia una GUI completa (Tkinter, Pygame, etc.).
- Puede usarse también para logging simbólico o debug emocional del sistema.

