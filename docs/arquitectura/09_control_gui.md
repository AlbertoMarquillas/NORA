## 09. `control_gui.py` – Interfaz gráfica de control en simulación

**Ubicación:** `software/src/gui/control_gui.py`

**Rol en el sistema:**
Proporciona una interfaz gráfica sencilla, clara y extensible para emitir eventos manuales al sistema NORA, observar el estado de la FSM, leer respuestas verbales y representar simbología visual en tiempo real.

---

### ✳️ Funcionalidad principal

- Botones para enviar eventos como `EVT_FACE_DETECTED`, `EVT_COMMAND_RECOGNIZED`, etc.
- Visualización del estado FSM mediante texto y emoji simbólico.
- Visualización de la respuesta verbal generada por el sistema.
- Área gráfica (`Canvas`) para visualizaciones futuras.

---

### 📐 Diseño gráfico

- Basado en `Tkinter`, estructura con `Frame` y `grid()`.
- Resolución inicial: `800x600`.
- Columna izquierda: estado + respuesta + controles.
- Columna derecha: canvas expandible para métricas o visualización.

---

### 🔗 Integración

- El sistema se suscribe automáticamente a:
  - `EVT_MOSTRAR_ESTADO`
  - `EVT_DECIR_TEXTO`
- Utiliza `EventManager` para emitir y reaccionar a eventos.
- Integrado en `Sistema.ejecutar_gui()`.

---

### ▶️ Ejecución

```bash
python software/main.py --gui
    