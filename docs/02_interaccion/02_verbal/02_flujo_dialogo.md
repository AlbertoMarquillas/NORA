# Flujo de Diálogo – Interacción Verbal

Este documento describe el flujo lógico completo de una interacción verbal típica en NORA, desde la captura del audio hasta la respuesta hablada, pasando por la interpretación de intención, validación contextual y ejecución del comando.

---

## 1. Diagrama general

```plaintext
[Micrófono] 
    ↓
voz/asr.py → texto
    ↓
dialogo/interpretador.py → intención
    ↓
agentes/contexto.py → validación
    ↓
[Módulo destino] → ejecución de acción
    ↓
voz/tts.py → respuesta hablada
```

---

## 2. Estados del sistema que permiten entrada verbal

* `STATE_ACTIVE_WAIT`
* `STATE_DIALOGUE`
* `STATE_CONFIRMATION`

> El sistema no interpreta voz en `STATE_IDLE` a menos que sea hotword.

---

## 3. Componentes implicados

* **voz/asr.py**: convierte audio en texto (STT)
* **dialogo/interpretador.py**: determina la intención del usuario
* **agentes/contexto.py**: ajusta, filtra o confirma la acción
* **datos/**, **accionadores/**, etc.: módulos que ejecutan el comando
* **voz/tts.py**: genera la respuesta verbal

---

## 4. Diálogo secuencial (multi-turn)

Algunas interacciones requieren más de un turno de diálogo:

**Ejemplo:**

* Usuario: “Apunta una nota”
* NORA: “¿Qué quieres que apunte?”
* Usuario: “Tengo que comprar pilas”

> En este caso, el motor de diálogo retiene el contexto (`esperando_contenido_nota`) hasta recibir la entrada completa.

---

## 5. Manejo de errores

* Si la transcripción falla → `voz/tts.py` responde: “No te he entendido.”
* Si no se reconoce la intención → “No sé cómo ayudarte con eso.”
* Si se reconoce pero está fuera de contexto → el agente bloquea y responde con sugerencia

---

## 6. Temporizadores

* Si no se recibe respuesta en `STATE_DIALOGUE`, se agota el contexto tras X segundos
* Se puede reactivar automáticamente si el usuario vuelve a hablar

---

Este flujo asegura robustez, continuidad y capacidad de extender la interacción mediante lógica de turnos, manteniendo coherencia modular y expresividad natural.
