## 03. Protocolo de Interacción en NORA

### Propósito del documento

Este documento define el protocolo de interacción entre el usuario y NORA, estableciendo los flujos típicos de comunicación, los eventos que los desencadenan, los estados implicados en cada fase y la coordinación entre entradas y salidas multimodales.

Su objetivo es servir como referencia técnica para diseñar, simular e implementar lógicas de interacción coherentes, expresivas y no intrusivas.

---

### Modelo general de interacción

NORA funciona como un sistema basado en **eventos contextuales** y **estados internos**. Cada acción del usuario (voz, presencia, gesto) o del entorno genera un evento que puede modificar el estado del sistema e iniciar una respuesta coordinada.

El sistema se comporta como un agente activo pero respetuoso, que reacciona de forma coherente solo cuando hay intención expresa o condiciones claras.

---

### Fases de interacción típica

#### 1. Activación
- **Evento:** acercamiento de NFC o activación manual.
- **Reacción:** inicialización de módulos, cambio de estado a "activo", animación facial de bienvenida, color de luz de encendido, saludo verbal opcional.

#### 2. Observación pasiva
- **Evento:** presencia detectada sin interacción verbal.
- **Reacción:** expresión facial neutra o atenta, iluminación tenue, giro leve de cabeza hacia el usuario.

#### 3. Inicio de diálogo
- **Evento:** detección de palabra clave, frase dirigida o comando directo.
- **Reacción:** activación FSM de diálogo, iluminación de escucha activa, gesto de atención, transcripción y respuesta hablada.

#### 4. Desarrollo
- **Evento:** continuación del intercambio con preguntas o respuestas.
- **Reacción:** expresiones faciales acordes, uso del contexto almacenado, adaptación del tono de voz y de la iluminación.

#### 5. Cierre explícito o pasivo
- **Evento:** frase de cierre ("gracias", "hasta luego"), silencio prolongado, comando de reposo.
- **Reacción:** animación de despedida, disminución de luz, entrada a estado pasivo o reposo.

---

### Tipos de eventos reconocidos

#### Entrada verbal
- Palabras clave configurables
- Frases de comando ("recuérdame beber agua")
- Saludos, agradecimientos, confirmaciones

#### Entrada visual
- Presencia mantenida en campo de visión
- Detección de rostro mirando a NORA
- Expresiones faciales básicas (sonrisa, duda)

#### Entrada contextual
- Hora del día
- Duración sin interacción
- Objetivos del usuario pendientes

#### Entrada táctil o de sistema
- Lectura NFC (activación/desactivación)
- Comando por teclado (en simulación)
- Notificación interna de otro módulo

---

### Respuestas del sistema

#### Verbales
- Respuestas directas ("Anotado")
- Preguntas aclaratorias ("¿Quieres que te lo recuerde mañana también?")
- Comentarios empáticos ("Ánimo, estás haciendo un buen trabajo")

#### Visuales
- Cambios de expresión facial (alegría, espera, duda)
- Parpadeo o mirada dirigida
- Animaciones sincronizadas con la voz

#### Lumínicas
- Códigos de color por estado (escucha: azul; error: rojo; espera: blanco tenue)
- Transiciones suaves al cambiar de fase

#### Físicas
- Cabeceo de afirmación o atención
- Giro leve al detectar presencia lateral
- Reposicionamiento al entrar en espera

---

### Sincronización multimodal

Todo evento debe generar una respuesta **coherente en voz, luz, rostro y movimiento**, según el estado emocional y la intención del sistema.

Ejemplo:
- Evento: "Recuérdame beber agua a las 4"
- Respuesta: voz amable ("De acuerdo"), sonrisa visual, luz verde tenue, cabeceo breve.

---

### Estados implicados en la interacción

- `REPOSO`: sin actividad, solo escucha NFC.
- `PASIVO`: espera atenta, expresión neutra, sensores activos.
- `ESCUCHA`: reconocimiento activo, iluminación y gestos de atención.
- `ACTIVO`: ejecución de tareas, diálogo, reacciones.
- `DESPEDIDA`: cierre visual y verbal, transición a pasivo o reposo.

---

### Consideraciones de diseño

- Todas las interacciones deben estar mediadas por una intención clara.
- Las respuestas deben ser breves, coherentes, humanizadas y opcionalmente adaptables.
- Se debe garantizar la privacidad del usuario en cada fase.
- Se evitará toda reacción automática sin un evento definido o una condición contextual clara.

---

Este protocolo será la base para implementar los motores de interacción y para construir pruebas de experiencia de usuario antes del montaje físico del sistema.

