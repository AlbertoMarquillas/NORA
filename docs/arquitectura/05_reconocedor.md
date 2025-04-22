## 05. `reconocedor.py` – Simulación de reconocimiento de voz (ASR)

**Ubicación:** `software/src/voz/reconocedor.py`

**Rol en el sistema:**
Este módulo define la clase `ReconocedorVoz`, que simula la entrada de comandos de voz del usuario. No graba audio ni usa micrófono real, sino que genera eventos a partir de una lógica probabilística interna.

---

### ✳️ Funcionalidad principal
- Método `escuchar_simulado()` activa la simulación de voz.
- Con una probabilidad determinada (por defecto 70%), elige aleatoriamente un comando válido.
- Si no se reconoce, emite un evento `EVT_COMMAND_UNKNOWN`.

---

### 🔗 Eventos generados
- `EVT_COMMAND_RECOGNIZED` (con campo `texto`)
- `EVT_COMMAND_UNKNOWN` (sin datos, respuesta genérica)

---

### 🧩 Lógica de simulación
```python
if exito:
    texto = random.choice([...])
    em.emitir(Evento("EVT_COMMAND_RECOGNIZED", datos={"texto": texto}))
else:
    em.emitir(Evento("EVT_COMMAND_UNKNOWN"))
```

---

### 📌 Observaciones
- Permite validar el flujo FSM, voz y visual sin hardware real.
- Sustituible por un ASR real en el futuro (Vosk, Whisper, etc.).
- Integra bien con `main.py`, `sistema.py` y el sistema de eventos.

