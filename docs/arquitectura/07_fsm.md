## 07. `fsm.py` – Máquina de estados finita de NORA

**Ubicación:** `software/src/sistema/fsm.py`

**Rol en el sistema:**
Este módulo define la FSM (Finite State Machine) que regula el comportamiento lógico general del asistente. Cada entrada (evento) provoca una transición entre estados internos, que guían la activación de otros módulos.

---

### ✳️ Estados definidos (`EstadoNora`)
- `REPOSO`
- `PASIVO`
- `ESCUCHA`
- `ACTIVO`
- `DESPEDIDA`
- `ERROR`

Cada estado representa un modo de funcionamiento simbólico del asistente.

---

### 🔁 Lógica de transición
- La FSM comienza en `REPOSO`.
- El método `transicion(evento: str)` aplica las reglas para determinar el nuevo estado.
- La transición es inmediata y retorna el nuevo estado.

---

### 🧩 Ejemplo de transición
```python
if self.estado_actual == EstadoNora.ESCUCHA:
    if evento == "EVT_COMMAND_RECOGNIZED":
        self.estado_actual = EstadoNora.ACTIVO
```

---

### 📌 Observaciones
- Es la base lógica del comportamiento del sistema.
- Reacciona a eventos emitidos desde reconocimiento, sistema o entrada física.
- Permite emitir eventos derivados (`EVT_MOSTRAR_ESTADO`) desde manejadores externos.
- Fácilmente ampliable para nuevos estados (por ejemplo: `EMOCIONAL`, `ANALISIS`, etc.).