## 01. `main.py` – Lanzador del sistema

**Ubicación:** `software/main.py`

**Rol en el sistema:**
Archivo mínimo de entrada. No contiene lógica de flujo ni reglas del sistema. Su única responsabilidad es interpretar los argumentos de ejecución y delegar todo el comportamiento en una instancia de la clase `Sistema`.

---

### ✳️ Funcionalidad principal
- Recibe el argumento `--simulacion` para determinar el modo de ejecución.
- Instancia `Sistema(simulacion=args.simulacion)`.
- Llama a `sistema.ejecutar_simulacion()`.

---

### 🔗 Dependencias
- `argparse`: para gestión de argumentos de consola.
- `from src.sistema.sistema import Sistema`: para cargar la clase principal del asistente.

---

### ⚙️ Interacción con otros módulos
- No tiene acceso directo a FSM, voz, eventos ni interfaz.
- No importa `event_manager`, `fsm`, ni módulos de entrada/salida.
- Es completamente desacoplado del comportamiento interno del asistente.

---

### 📌 Ejemplo de uso
```bash
python main.py --simulacion
```
Esto ejecuta la simulación completa con todos los módulos de voz, FSM e interfaz conectados.

---

### 🧩 Relación con `sistema.py`
Este archivo fue simplificado tras la creación del módulo `sistema.py`, que encapsula toda la lógica del asistente. Antes, `main.py` contenía todas las llamadas y suscripciones directamente.

Ahora es simplemente un lanzador limpio.

