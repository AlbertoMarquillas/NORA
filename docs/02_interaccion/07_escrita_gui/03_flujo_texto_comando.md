# Flujo de Texto a Comando – Interacción Escrita por GUI

Este documento describe el flujo lógico completo desde la entrada de texto escrita por el usuario hasta la ejecución del comando correspondiente dentro del sistema NORA. La arquitectura es equivalente a la del procesamiento de voz, pero adaptada a una entrada textual directa.

---

## 1. Diagrama del flujo

```plaintext
[Texto introducido en GUI] 
       ↓
interfaz_escrita/entrada.py → texto limpio
       ↓
dialogo/interpretador.py → intención
       ↓
agentes/contexto.py → validación
       ↓
[Módulo correspondiente] → ejecución
       ↓
interfaz_escrita/respuesta.py → salida textual en pantalla
```

---

## 2. Estados del sistema compatibles

* `STATE_ATTENTION`
* `STATE_DIALOGUE`

> A diferencia de la voz, esta entrada puede estar habilitada incluso en `STATE_SLEEP` si el login está activo.

---

## 3. Componentes implicados

* `entrada.py`: captura y limpia el texto del usuario
* `interpretador.py`: asigna intención y entidad
* `agentes/contexto.py`: aplica restricciones lógicas
* Módulos de acción: `datos/`, `accionadores/`, etc.
* `respuesta.py`: genera el mensaje textual mostrado en la interfaz

---

## 4. Manejo de errores

* Si el texto no es reconocible → “No he entendido lo que quieres decir.”
* Si la intención no está soportada → “Este comando no está disponible.”
* Si requiere contexto adicional → “¿Podrías concretar un poco más?”

---

## 5. Persistencia y trazabilidad

* Las entradas y respuestas pueden guardarse en `logs/interaccion_textual.log`
* Se puede usar un historial visible en GUI para mostrar las últimas interacciones

---

Este flujo garantiza que NORA interprete correctamente las órdenes escritas por el usuario, integrándolas sin fricciones con su arquitectura modular de diálogo y ejecución de comandos.
