## xx. Ejecución del Proyecto NORA – Bitácora Técnica

Este documento sirve como registro paso a paso del proceso de ejecución técnica del proyecto NORA, en orden cronológico y estructurado. Permite trazar cómo se ha ido implementando y desplegando cada parte del sistema.

Se actualizará progresivamente con cada acción relevante, incluyendo comandos ejecutados, archivos creados, estructura establecida y decisiones técnicas documentadas.

---

### 🟢 Paso 1: Generación de estructura de carpetas lógicas (`src/`)

**Fecha:** [22/04/2025]

**Acción:** Creación de la estructura modular del sistema dentro de `src/` mediante script automatizado.

**Ubicación del script:** `src/utils/estructura_src.py`

**Comando ejecutado:**
```bash
cd src
python utils/estructura_src.py
```

**Resultado:**
- Carpetas creadas: `vision/`, `voz/`, `interfaz/`, `control/`, `sistema/`, `datos/`
- Cada una incluye su `__init__.py`

**Motivación técnica:** Permite comenzar con un diseño desacoplado y extensible. Cada carpeta corresponde a un módulo lógico autónomo del sistema.

**Notas adicionales:**
- El script ha sido corregido para **no crear la carpeta `src/`**, ya que se ejecuta desde dentro de ella.
- Ver `utils/estructura_src.py` para la versión actual.

**Referencias:**
- `02.arquitectura_logica.md`
- `estructura_src.py`

---

### 🟢 Paso 2: Reestructuración del software bajo carpeta dedicada `software/`

**Fecha:** [22/04/2025]

**Acción:** Reubicación de la lógica principal dentro de una nueva carpeta `software/`, incluyendo `main.py` y la carpeta `src/` como subdirectorio.

**Estructura resultante:**
```bash
software/
├── main.py
└── src/
    ├── vision/
    ├── voz/
    ├── interfaz/
    ├── control/
    ├── sistema/
    └── datos/
```

**Detalles:**
- Se ha creado `software/main.py` como punto de entrada del sistema.
- Se ha añadido `software/src/__init__.py` para declarar `src/` como paquete Python.
- Los imports dentro de `main.py` podrán usar `from src.<> import ...`

**Motivación técnica:** Agrupar todo el software operativo en una única carpeta para aislarlo de documentación, hardware y otros recursos. Mejora la portabilidad y claridad de propósito.

**Referencias:**
- `README.md` actualizado con nueva estructura
- `main.py` inicializado como lanzador del sistema en modo simulación

---

### 🟢 Paso 3: Creación del módulo `sistema/fsm.py` con la FSM de NORA

**Fecha:** [22/04/2025]

**Acción:** Se define el archivo `fsm.py` dentro del módulo `sistema/` para gestionar los estados funcionales de NORA mediante una máquina de estados finita (FSM).

**Contenido principal:**
- Enumeración `EstadoNora` con los estados: `REPOSO`, `PASIVO`, `ESCUCHA`, `ACTIVO`, `DESPEDIDA`, `ERROR`.
- Clase `FSM` con atributo `estado_actual` y método `transicion(evento)` para gestionar las reglas de paso entre estados según eventos del sistema.

**Motivación técnica:** La FSM es el núcleo lógico que define el comportamiento global del asistente. Determina cómo debe reaccionar a cada evento y qué módulo debe activarse en cada estado.

**Referencias:**
- `04.estados_y_emociones.md` (para coherencia funcional)
- `06.documento_eventos.md` (para mapeo de eventos válidos)
- Archivo: `software/src/sistema/fsm.py`

---

### 🟢 Paso 4: Integración de la FSM en `main.py` con eventos simulados

**Fecha:** [22/04/2025]

**Acción:** Se modifica `main.py` para importar la clase `FSM` y ejecutar una simulación de eventos, verificando las transiciones de estado.

**Eventos simulados:**
- `EVT_NFC_ACTIVATE`
- `EVT_FACE_DETECTED`
- `EVT_COMMAND_RECOGNIZED`
- `EVT_IDLE_TIMEOUT`
- `EVT_SHUTDOWN_REQUEST`

**Resultado observado:**
```plaintext
[main.py] Estado inicial: REPOSO
→ Enviando evento: EVT_NFC_ACTIVATE → PASIVO
→ Enviando evento: EVT_FACE_DETECTED → ESCUCHA
→ Enviando evento: EVT_COMMAND_RECOGNIZED → ACTIVO
→ Enviando evento: EVT_IDLE_TIMEOUT → PASIVO
→ Enviando evento: EVT_SHUTDOWN_REQUEST → PASIVO (sin efecto)
```

**Motivación técnica:** Verificar el flujo de transición y preparar la base para conectar el sistema de eventos reales.

**Referencias:**
- `main.py` actualizado en `software/`
- Salida de consola del entorno virtual (`python main.py --simulacion`)

---

### 🔜 Próximos pasos previstos

1. Desarrollo de un `EventManager` para distribuir eventos entre módulos.
2. Registro y logging de eventos y estados.
3. Incorporación de interacción real desde `voz/` y `vision/`.

Este archivo se actualizará de forma incremental conforme se ejecuten nuevas acciones en el entorno local del proyecto.