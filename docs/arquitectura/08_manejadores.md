## 08. `manejadores.py` – Gestión externa de eventos FSM

**Ubicación:** `software/src/sistema/manejadores.py`

**Rol en el sistema:**
Define funciones externas que reaccionan a eventos del sistema, en particular para gestionar la FSM de NORA. Actúa como capa de lógica modular que transforma eventos en acciones coordinadas (transiciones, voz, visualización).

---

### ✳️ Funcionalidad principal
- La función `manejar_evento_fsm(evento, fsm, em)` recibe un evento y:
  - Aplica una transición en la FSM
  - Emite `EVT_MOSTRAR_ESTADO` para visualización simbólica
  - Emite `EVT_DECIR_TEXTO` como respuesta verbal si corresponde

---

### 🔁 Eventos gestionados
- `EVT_COMMAND_RECOGNIZED`
- `EVT_COMMAND_UNKNOWN`
- `EVT_NFC_ACTIVATE`
- `EVT_FACE_DETECTED`
- `EVT_IDLE_TIMEOUT`
- `EVT_SHUTDOWN_REQUEST`

---

### 🧩 Estructura típica
```python
nuevo_estado = fsm.transicion(evento.tipo)
em.emitir(Evento("EVT_MOSTRAR_ESTADO", datos={"estado": nuevo_estado.name}))
if evento.tipo == "EVT_COMMAND_RECOGNIZED":
    em.emitir(Evento("EVT_DECIR_TEXTO", datos={"texto": respuesta}))
```

---

### 📌 Observaciones
- Este módulo permite mantener el `main.py` y `sistema.py` limpios y centrados en orquestación.
- Facilita el testeo de comportamiento por tipo de evento.
- Se puede extender fácilmente con nuevos tipos de manejadores según los eventos introducidos en el futuro.

