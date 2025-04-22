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

### 🟢 Paso 5: Creación del `EventManager` para gestión de eventos internos

**Fecha:** [22/04/2025]

**Acción:** Se implementa el archivo `event_manager.py` en el módulo `sistema/`, con las clases `EventManager` y `Evento`.

**Contenido principal:**
- `Evento`: estructura de evento con tipo, origen, datos, timestamp y prioridad
- `EventManager`: subscripción y distribución de eventos a módulos receptores

**Características técnicas:**
- Uso de `PriorityQueue` para orden por prioridad (1 a 5)
- Distribución asincrónica y desacoplada vía callbacks
- Registro de subscripciones por tipo de evento
- Consola informativa de encolado y despacho de eventos

**Motivación técnica:** Establecer el sistema de mensajería interna para garantizar modularidad y permitir que los distintos componentes interactúen sin acoplamiento directo.

**Referencias:**
- `06.documento_eventos.md`
- Archivo: `software/src/sistema/event_manager.py`

---

### 🟢 Paso 6: Integración de FSM con EventManager en `main.py`

**Fecha:** [22/04/2025]

**Acción:** Se reemplaza la lógica de simulación directa en `main.py` por una arquitectura basada en `EventManager`, suscribiendo la FSM como receptora de eventos.

**Cambios clave:**
- Se instancia `EventManager` en `main.py`
- Se registra `FSM.transicion()` como callback de múltiples eventos (`EVT_NFC_ACTIVATE`, `EVT_FACE_DETECTED`, etc.)
- Los eventos simulados se emiten y se procesan con el EventManager en lugar de llamar directamente a la FSM

**Resultado:**
- El sistema responde a eventos mediante el canal de distribución previsto
- La arquitectura se vuelve desacoplada y lista para integración progresiva de módulos

**Referencias:**
- `main.py` actualizado (software/)
- `event_manager.py` limpio sin bloque de pruebas
- `test_event_manager_fsm.py` en `software_tests/` para pruebas externas

---

### 🟢 Paso 7: Creación del módulo `voz/reconocedor.py` para simulación de voz

**Fecha:** [22/04/2025]

**Acción:** Se implementa el archivo `reconocedor.py` dentro del módulo `voz/`, con una clase `ReconocedorVoz` encargada de simular el reconocimiento de voz.

**Funcionamiento:**
- Simula un comando de voz con probabilidad de éxito (70%).
- Emite evento `EVT_COMMAND_RECOGNIZED` con el texto si el reconocimiento tiene éxito.
- Emite `EVT_COMMAND_UNKNOWN` en caso contrario.
- Todos los eventos se emiten mediante el `EventManager`, integrándose con la FSM.

**Motivación técnica:** Permite probar el sistema de interacción por voz de forma modular, controlada y sin requerir micrófono ni ASR real, en preparación para su sustitución futura por Vosk o Whisper.

**Observación:** Este módulo ha sido diseñado para ser fácilmente reemplazado por reconocimiento real, y podrá escalar hacia IA conversacional conectando la transcripción a un modelo LLM externo o interno.

**Referencias:**
- Archivo: `software/src/voz/reconocedor.py`
- Documento: `01.plan_implementacion_software.md`, sección "Observaciones técnicas futuras"

---

### 🟢 Paso 8: Integración del Reconocedor de Voz en `main.py`

**Fecha:** [22/04/2025]

**Acción:** Se ha integrado el módulo `ReconocedorVoz` dentro de `main.py`, permitiendo que el sistema simule el reconocimiento de voz como parte del flujo principal.

**Cambios realizados:**
- Se importa la clase `ReconocedorVoz` desde `src.voz.reconocedor`
- Se instancia un objeto `voz = ReconocedorVoz(em)` conectado al `EventManager`
- Tras eventos clave (`EVT_FACE_DETECTED` y `EVT_COMMAND_RECOGNIZED`), se activa `voz.escuchar_simulado()`
- El resultado del reconocimiento simulado genera un evento `EVT_COMMAND_RECOGNIZED` o `EVT_COMMAND_UNKNOWN`

**Motivación técnica:** Integrar de forma natural el módulo de voz como un productor activo de eventos dentro del sistema. Permite simular flujos completos de interacción sin hardware ni entrada real de voz, y probar la reacción de la FSM.

**Resultado esperado:**
- Transición FSM → ESCUCHA
- Reconocimiento simulado (con 70% éxito)
- Evento emitido por voz → FSM cambia estado según lógica definida

**Referencias:**
- Archivo: `software/main.py`
- Archivo: `software/src/voz/reconocedor.py`
- Documento: `01.plan_implementacion_software.md`

---

### 🔜 Próximos pasos previstos

1. Implementar síntesis de voz (TTS) para responder con salida hablada
2. Extender `FSM` para gestionar respuestas y reacciones adicionales
3. Preparar pruebas específicas del flujo de voz completo

Este archivo se actualizará de forma incremental conforme se ejecuten nuevas acciones en el entorno local del proyecto.