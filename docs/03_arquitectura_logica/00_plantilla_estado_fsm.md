# Plantilla de Definición de Estados – FSM del Sistema NORA

Esta plantilla sirve como referencia formal para documentar los estados operativos del sistema NORA dentro de su máquina de estados finitos (FSM). Su uso garantiza una descripción homogénea, útil para implementación, mantenimiento y análisis del comportamiento del asistente.

---

## Estado: [NOMBRE DEL ESTADO]

### 1. Descripción funcional

[Describir en una o dos frases la función principal de este estado. Qué representa para el sistema. Qué condiciones generales define.]

---

### 2. Condiciones de entrada

Indicar los eventos, señales o condiciones internas que activan este estado:

- Evento o condición 1  
- Evento o condición 2  
- Estado previo válido: [nombre del estado anterior]

---

### 3. Acciones realizadas

Mientras el sistema permanece en este estado:

- Acción 1 (por ejemplo, activar micrófono)
- Acción 2 (por ejemplo, mostrar expresión facial asociada)
- Indicadores visibles: [ej. LED color azul, pantalla animada, etc.]
- Activación de módulos: [ej. voz/, sensores/]

---

### 4. Condiciones de salida

Este estado termina cuando se produce alguna de las siguientes condiciones:

- Evento o condición 1 → transición
- Evento o condición 2 → transición
- Timeout / error / entrada válida, etc.

---

### 5. Estados posibles de destino

Enumerar las transiciones salientes desde este estado:

- [Nombre del estado destino] ← [Evento/Condición que causa la transición]
- [Otro destino] ← [Otra condición]

---

### 6. Notas adicionales (opcional)

- Relevancia para otros módulos: [agentes/, sistema/, interfaz/, etc.]
- Casos de excepción o errores comunes
- Observaciones sobre sincronización o prioridad

---

**Ejemplo aplicado:**

## Estado: Escucha

### 1. Descripción funcional

NORA permanece atenta esperando un comando de voz tras haber sido activada por presencia o atención visual.

### 2. Condiciones de entrada

- Evento `EVT_ATTENTION_GAINED`
- Transición desde estado: Activado
- Micrófono disponible y sin error

### 3. Acciones realizadas

- Activar micrófono (ASR)
- Monitoreo VAD y detección de palabra clave
- LED azul tenue (modo espera)
- Bloqueo de entrada por NFC mientras se escucha

### 4. Condiciones de salida

- Evento `EVT_SPEECH_RECOGNIZED` → Procesando
- Evento `EVT_IDLE_TIMEOUT` → Activado
- Evento `EVT_MIC_FAILURE` → Error

### 5. Estados posibles de destino

- Procesando ← voz detectada  
- Activado ← timeout sin voz  
- Error ← fallo en ASR o micrófono

### 6. Notas adicionales

- Este estado puede reiniciarse en bucle si hay interrupción continua de atención.
- Módulo `voz/` tiene prioridad operativa.
