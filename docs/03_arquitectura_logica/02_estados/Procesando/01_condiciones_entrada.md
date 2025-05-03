# Condiciones de entrada – Estado: Procesando

El sistema NORA entra en el estado **Procesando** cuando ha recibido una entrada estructurada que requiere interpretación, análisis o inferencia. La transición es gestionada por la FSM `sistema/` y está condicionada a la disponibilidad de los módulos de procesamiento requeridos (`dialogo/`, `models/`, `datos/`, etc.).

---

## 1. Reconocimiento de comando verbal

- **Evento:** `EVT_SPEECH_RECOGNIZED`  
  Emitido por el módulo `voz/` al completar con éxito el análisis fonético y semántico de una entrada vocal.  
  El contenido se almacena temporalmente para su interpretación en `dialogo/`.

---

## 2. Reconocimiento de gesto o entrada visual

- **Evento:** `EVT_GESTURE_COMMAND`  
  Reportado por el módulo `vision/` al identificar una señal gestual con significado asociado (por ejemplo, gesto de saludo, número, silencio, etc.).  
  Se requiere que `vision/` y `models/` estén activos.

---

## 3. Petición interna de procesamiento

- **Comando:** `CMD_PROCESS_INPUT`  
  Generado por un agente o módulo secundario (como `interfaz/` o `activacion/`) al detectar una condición que requiere evaluación contextual o planificación de respuesta.

---

## 4. Transición desde estado `Escucha` o `Atencion`

- Solo se permite entrada a `Procesando` desde estados que suponen una interacción reciente activa, como:
  - `Escucha` (tras comando verbal)
  - `Atencion` (tras gesto)
  - `Activado` (si hay entrada programada o eventos internos)

---

## Consideraciones adicionales

- La entrada al estado `Procesando` queda inhibida si existe una condición de error activa (`EVT_MODULE_FAILURE`) o si `models/` no está disponible.
- El sistema debe suspender temporalmente la entrada de nuevas interacciones mientras se procesa la actual (`FSM_LOCK = True`).
