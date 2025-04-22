## 02. `sistema.py` – Núcleo de coordinación del asistente

**Ubicación:** `software/src/sistema/sistema.py`

**Rol en el sistema:**
Encapsula toda la lógica funcional del asistente NORA. La clase `Sistema` es responsable de inicializar, conectar y coordinar todos los módulos: FSM, voz, interfaz, eventos, y flujo de simulación.

---

### ✳️ Funcionalidad principal
- Instancia y conecta los componentes clave: `FSM`, `EventManager`, `ReconocedorVoz`, `SintetizadorVoz`, `InterfazSimulada`.
- Registra los manejadores de eventos (`manejar_evento_fsm`) mediante `functools.partial`.
- Ejecuta una simulación completa con una secuencia de eventos definidos.
- Verifica el estado FSM y activa el reconocedor de voz solo cuando se encuentra en `ESCUCHA`.

---

### 🔗 Dependencias
- `fsm.py`: lógica de transición de estados.
- `event_manager.py`: distribución de eventos.
- `reconocedor.py`: simulación de entrada de voz.
- `sintetizador.py`: salida de voz con pyttsx3.
- `interfaz.py`: visualización simbólica por consola.
- `manejadores.py`: lógica de reacción a eventos.
- `functools.partial`: para vincular FSM y EventManager en los manejadores.

---

### ⚙️ Interacción con otros módulos
- Es el punto de unión de todos los módulos funcionales.
- No expone detalles internos, solo su método `ejecutar_simulacion()`.
- Permite separar la lógica del sistema del punto de entrada (`main.py`).

---

### 🧩 Relación con `main.py`
`main.py` simplemente instancia esta clase y ejecuta `sistema.ejecutar_simulacion()`.
Toda la lógica de comportamiento, gestión de estados y eventos se define en esta clase.

---

### 📌 Observaciones
- Esta clase permite preparar el sistema para otras modalidades: GUI, entorno físico, o pruebas unitarias.
- También puede evolucionar para incluir ciclos de ejecución continua o hilos concurrentes en modo real.

