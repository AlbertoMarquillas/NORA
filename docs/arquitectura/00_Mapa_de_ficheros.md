## 00. Mapa de Ficheros

Este documento describe de forma individual cada uno de los archivos fuente del proyecto NORA, explicando su propósito, ubicación y cómo interactúa con el resto del sistema.

Los documentos individuales por archivo se encuentran en la carpeta: `docs/arquitectura/`.

Archivos incluidos:
- `01_main.md`
- `02_sistema.md`
- `03_interfaz.md`
- `04_sintetizador.md`
- `05_reconocedor.md`
- `06_event_manager.md`
- `07_fsm.md`
- `08_manejadores.md`

---

### 🔹 `main.py`
**Ubicación:** `software/main.py`

**Descripción:**
Punto de entrada del sistema NORA. Instancia la clase `Sistema` y lanza la simulación o ejecución real según los argumentos pasados por línea de comandos. No contiene lógica funcional, delega todo en `Sistema`.

**Responsabilidad:**
- Análisis de argumentos (`--simulacion`)
- Lanzamiento de `Sistema.ejecutar_simulacion()`

**Dependencias:**
- `from src.sistema.sistema import Sistema`

---

### 🔹 `sistema.py`
**Ubicación:** `software/src/sistema/sistema.py`

**Descripción:**
Clase central del proyecto que encapsula toda la lógica de inicialización, coordinación e interacción entre módulos. Reemplaza al `main.py` anterior, centralizando la FSM, el bus de eventos, la interfaz visual y los módulos de entrada/salida.

**Responsabilidad:**
- Instanciar y conectar: `FSM`, `EventManager`, `ReconocedorVoz`, `SintetizadorVoz`, `InterfazSimulada`
- Emitir y procesar eventos
- Ejecutar simulaciones de flujo completo

**Dependencias:**
- `fsm.py`, `event_manager.py`, `reconocedor.py`, `sintetizador.py`, `interfaz.py`, `manejadores.py`

---

### 🔹 `interfaz.py`
**Ubicación:** `software/src/interfaz/interfaz.py`

**Descripción:**
Módulo responsable de representar visualmente (en consola) los estados funcionales y respuestas simbólicas del asistente. Utiliza emojis y mensajes descriptivos para simular una interfaz expresiva.

**Responsabilidad:**
- Escuchar eventos visuales (`EVT_COMMAND_RECOGNIZED`, `EVT_MOSTRAR_ESTADO`, etc.)
- Mostrar símbolos coherentes con el estado o emoción de NORA

**Dependencias:**
- `Evento` desde `event_manager`

---

### 🔹 `sintetizador.py`
**Ubicación:** `software/src/voz/sintetizador.py`

**Descripción:**
Módulo de síntesis de texto a voz. Reacciona a eventos de tipo `EVT_DECIR_TEXTO`, convirtiendo el contenido en voz mediante `pyttsx3`.

**Responsabilidad:**
- Subscribirse al evento `EVT_DECIR_TEXTO`
- Leer el texto recibido y emitirlo en voz

**Dependencias:**
- `pyttsx3`
- `Evento` desde `event_manager`

---

### 🔹 `reconocedor.py`
**Ubicación:** `software/src/voz/reconocedor.py`

**Descripción:**
Módulo que simula el reconocimiento de voz. Genera eventos `EVT_COMMAND_RECOGNIZED` o `EVT_COMMAND_UNKNOWN` con probabilidad variable para testear el flujo de eventos y reacciones del sistema.

**Responsabilidad:**
- Simular entrada de comandos por voz
- Emitir eventos de comandos reconocidos o fallidos

**Dependencias:**
- `random`
- `Evento` desde `event_manager`

---

### 🔹 `event_manager.py`
**Ubicación:** `software/src/sistema/event_manager.py`

**Descripción:**
Bus interno de eventos desacoplado. Permite que cualquier componente se registre como oyente de eventos y reaccione sin conocer al emisor.

**Responsabilidad:**
- Registrar oyentes (callbacks) por tipo de evento
- Encolar y procesar eventos por prioridad

**Dependencias:**
- `PriorityQueue`, `datetime`

---

### 🔹 `fsm.py`
**Ubicación:** `software/src/sistema/fsm.py`

**Descripción:**
Módulo que implementa la máquina de estados finita de NORA. Gestiona transiciones según eventos recibidos y mantiene el estado actual.

**Responsabilidad:**
- Definir estados (`Enum EstadoNora`)
- Ejecutar transiciones según eventos (`transicion()`)

**Dependencias:**
- `Enum`, `auto`

---

### 🔹 `manejadores.py`
**Ubicación:** `software/src/sistema/manejadores.py`

**Descripción:**
Archivo que agrupa funciones manejadoras externas para eventos. En concreto, define cómo reacciona la FSM a ciertos eventos y cómo se generan respuestas secundarias como TTS o visualización del estado.

**Responsabilidad:**
- Reaccionar a `EVT_COMMAND_RECOGNIZED`, `EVT_COMMAND_UNKNOWN`, etc.
- Emitir respuestas de voz y eventos `EVT_MOSTRAR_ESTADO`

**Dependencias:**
- `Evento` desde `event_manager`

---

