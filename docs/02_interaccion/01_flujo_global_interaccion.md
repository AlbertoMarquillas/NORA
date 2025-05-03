# Diagrama Global de Interacción Usuario–NORA

Este documento acompaña al archivo `diagrama_global_interaccion.drawio`, que representa de forma integral todos los flujos principales de interacción definidos entre el usuario y el sistema NORA.

---

## 1. Objetivo

Concentrar en un único esquema visual los estados principales de NORA, los eventos de entrada que causan transiciones entre dichos estados y las respuestas multimodales esperadas, ofreciendo una visión de conjunto para la lógica de control.

---

## 2. Contenido del diagrama

### Estados representados:

* **STATE\_SLEEP** (reposo)
* **STATE\_IDLE** (activo sin usuario)
* **STATE\_ACTIVE\_WAIT** (activo, atento)
* **STATE\_ATTENTION** (presencia detectada)
* **STATE\_DIALOGUE** (procesamiento de comando)
* **STATE\_ERROR** (respuesta a fallo crítico)

### Eventos clave:

* Lectura NFC válida → `EVT_ACTIVACION_NFC`
* Comando de voz → `EVT_COMANDO_RECONOCIDO`
* Presencia detectada → `EVT_VISUAL_DETECCION_PRESENCIA`
* Ausencia prolongada → `EVT_AUTONOMOUS_SLEEP`
* Error de ejecución → `EVT_AUTONOMOUS_ERROR_MSG`
* Registro de nota → `EVT_NOTA_GUARDADA`

### Transiciones:

* Del reposo al modo activo mediante NFC o hotword
* De activo a reposo por inactividad prolongada
* De atención a diálogo por voz
* De diálogo a error por fallo
* De error a espera tras recuperación

### Salidas multimodales:

* **Voz**: TTS con mensajes adaptados al contexto
* **Pantalla**: Ojos, expresiones visuales, animaciones
* **LEDs**: Colores según estado, animaciones de confirmación o alerta
* **Movimiento**: Giro de cabeza, asentimientos, orientación facial

---

## 3. Archivos vinculados

* `diagrama_global_interaccion.drawio` – Esquema editable completo
* `diagrama_global_interaccion.png` – Imagen estática para consulta rápida

---

Este diagrama es la referencia central para diseñar la lógica FSM (máquina de estados finitos) de NORA y coordinar la arquitectura entre módulos perceptivos, de acción y expresivos.
