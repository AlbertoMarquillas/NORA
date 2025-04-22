## 06. `event_manager.py` – Sistema interno de eventos (pub/sub)

**Ubicación:** `software/src/sistema/event_manager.py`

**Rol en el sistema:**
Este módulo define el `EventManager`, un sistema de publicación y suscripción de eventos que permite comunicación desacoplada entre los distintos módulos del asistente NORA. También define la clase `Evento`, usada para encapsular la información transmitida.

---

### ✳️ Funcionalidad principal
- Registrar oyentes para tipos de evento (suscripción).
- Encolar eventos con prioridad.
- Procesar eventos entregándolos a los módulos registrados.

---

### 🔗 Clases definidas
- `Evento`: contiene `tipo`, `origen`, `datos`, `timestamp`, `prioridad`.
- `EventManager`: maneja la cola y distribución de eventos.

---

### 🧩 Lógica de flujo
```python
self.cola.put((evento.prioridad, evento))
...
while not self.cola.empty():
    _, evento = self.cola.get()
    for callback in self.oyentes.get(evento.tipo, []):
        callback(evento)
```

---

### 📌 Observaciones
- Es el corazón de la arquitectura desacoplada.
- Permite que los módulos sean reactivos y escalables.
- El orden de procesamiento está regulado por prioridad (1 a 5).
- Se utiliza en `sistema.py`, `main.py`, y todos los módulos funcionales.