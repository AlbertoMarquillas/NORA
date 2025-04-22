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


### 🟢 Paso 9: Diseño del módulo de síntesis de voz (TTS)

**Fecha:** [22/04/2025]

**Acción:** Se define la necesidad funcional y la estructura inicial del módulo `voz/sintetizador.py`, responsable de convertir texto en voz para emitir respuestas habladas por parte de NORA.

**Planteamiento técnico:**
- Se utilizará `pyttsx3` como motor TTS inicial por ser offline, multiplataforma y ligero.
- El módulo se integrará con el `EventManager` mediante suscripción al evento `EVT_DECIR_TEXTO`.
- Cada evento contendrá un campo `datos['texto']` con el contenido a sintetizar.

**Motivación técnica:** Proveer a NORA de capacidad de respuesta verbal coordinada, manteniendo el enfoque desacoplado mediante eventos. Este módulo complementa el flujo iniciado por `ReconocedorVoz`, cerrando el ciclo de entrada-salida verbal.

**Flujo previsto:**
1. Usuario activa escucha → Reconocedor genera `EVT_COMMAND_RECOGNIZED`
2. FSM u otro módulo decide respuesta → emite `EVT_DECIR_TEXTO`
3. Sintetizador recibe evento → habla el texto proporcionado

**Referencias:**
- Futuro archivo: `software/src/voz/sintetizador.py`
- Motor propuesto: `pyttsx3`
- Formato de evento: `Evento(tipo="EVT_DECIR_TEXTO", datos={"texto": "Son las 4 en punto"})`

---

### 🟢 Paso 10: Integración del módulo de síntesis de voz (TTS) en `main.py`

**Fecha:** [22/04/2025]

**Acción:** Se ha integrado el módulo `SintetizadorVoz` al flujo principal del sistema, utilizando `pyttsx3` para emitir respuestas habladas al recibir eventos `EVT_DECIR_TEXTO`.

**Cambios realizados:**
- Creación del archivo `voz/sintetizador.py` con clase `SintetizadorVoz`
- Registro en `main.py` para que escuche eventos `EVT_DECIR_TEXTO`
- El `main.py` emite una respuesta simulada al detectar un comando de voz válido (`EVT_COMMAND_RECOGNIZED`)

**Motivación técnica:** Completar el ciclo de interacción verbal: reconocimiento simulado + respuesta hablada. Este paso permite validar el subsistema de salida por voz y prepara el sistema para coordinación con expresiones faciales y emocionales en el futuro.

**Resultado esperado:**
- Evento de voz simulado → FSM responde → emite texto a decir → `SintetizadorVoz` habla la respuesta con `pyttsx3`

**Referencias:**
- Archivo: `software/src/voz/sintetizador.py`
- Archivo: `software/main.py`
- Evento gestionado: `EVT_DECIR_TEXTO`

---

### 🟢 Paso 11: Modularización de `main.py` con manejadores externos

**Fecha:** [22/04/2025]

**Acción:** Se ha refactorizado `main.py` para extraer la lógica de manejo de eventos FSM a un módulo externo, con el objetivo de mejorar la modularidad, limpieza y reutilización del código.

**Cambios realizados:**
- Creación del archivo `sistema/manejadores.py` con la función `manejar_evento_fsm()`
- Uso de `functools.partial()` en `main.py` para registrar `manejar_evento_fsm()` como manejador de eventos, manteniendo acceso a `fsm` y `em`
- Limpieza del cuerpo de `iniciar_sistema()` eliminando funciones internas

**Motivación técnica:** Facilitar la escalabilidad y mantenimiento del sistema al separar responsabilidades y encapsular manejadores por módulo. Esta práctica permite centralizar todos los manejadores futuros en un único archivo.

**Resultado esperado:**
- Lógica de transición FSM + emisión de respuestas movida fuera del `main.py`
- Suscripción clara y declarativa de eventos en el bloque de inicialización

**Referencias:**
- Archivo: `software/main.py`
- Archivo: `software/src/sistema/manejadores.py`

---

### 🟢 Paso 12: Diseño del módulo `interfaz/` para representación simbólica

**Fecha:** [22/04/2025]

**Acción:** Se planifica la creación del módulo `interfaz/` con una clase `InterfazSimulada`, cuyo propósito será representar gráficamente (de forma textual o visual) los estados y emociones del asistente NORA.

**Motivación técnica:** Complementar la interacción verbal con retroalimentación visual simbólica, incluso en modo de simulación. Este módulo podrá mostrar expresiones, colores simbólicos o mensajes que acompañen el comportamiento del sistema.

**Objetivos principales del módulo:**
- Mostrar visualmente el estado actual de NORA (REPOSO, ESCUCHA, ACTIVO, ERROR, etc.)
- Representar emociones básicas (neutro, alegre, confundido, dormido)
- Responder a eventos tipo `EVT_COMMAND_RECOGNIZED`, `EVT_COMMAND_UNKNOWN`, `EVT_FACE_DETECTED`, `EVT_IDLE_TIMEOUT`, etc.
- Mantener una lógica desacoplada, escuchando eventos desde el `EventManager`

**Representación prevista (modo texto):**
- 😐 Neutro (estado PASIVO)
- 🟢 Activo (tras comando entendido)
- ❓ Confuso (tras comando no reconocido)
- 💤 Inactivo (tras timeout o reposo)

**Referencias:**
- Futuro archivo: `software/src/interfaz/interfaz.py`
- EventManager ya preparado para distribuir eventos

---

### 🟢 Paso 13: Integración indirecta de TTS e InterfazSimulada vía EventManager

**Fecha:** [Especificar]

**Acción:** Se confirma la integración completa de los módulos `SintetizadorVoz` y `InterfazSimulada` dentro de `main.py`, aunque no son invocados directamente. Ambos actúan como módulos pasivos, suscritos al `EventManager`, reaccionando a eventos específicos.

**Detalles técnicos:**
- `SintetizadorVoz` escucha `EVT_DECIR_TEXTO` y convierte el contenido en voz con `pyttsx3`.
- `InterfazSimulada` escucha múltiples eventos (`EVT_COMMAND_RECOGNIZED`, `UNKNOWN`, etc.) y muestra representaciones simbólicas (emojis + mensajes) por consola.
- Ambos módulos **no requieren llamadas explícitas en `main.py`**, sino que actúan cuando reciben sus eventos registrados.

**Motivación técnica:** Confirmar y documentar el diseño desacoplado basado en eventos. Esta integración demuestra que el sistema es modular, extensible y que cada componente responde solo a los estímulos que le corresponden.

**Resultado esperado:**
- El sistema habla al reconocer comandos válidos.
- Informa visualmente en consola al detectar presencia, reconocer o no comandos, o entrar en reposo.

**Referencias:**
- Archivos: `software/src/voz/sintetizador.py`, `software/src/interfaz/interfaz.py`
- Integración comprobada en `main.py` mediante instanciación indirecta

---

### 🔜 Próximos pasos previstos

1. Añadir visualización basada en estado actual (FSM → interfaz)
2. Emitir eventos emocionales simbólicos (`EVT_EMOCION_ALEGRE`, etc.)
3. Desacoplar `main.py` en una clase `Sistema` para escalabilidad y pruebas unitarias

Este archivo se actualizará de forma incremental conforme se ejecuten nuevas acciones en el entorno local del proyecto.