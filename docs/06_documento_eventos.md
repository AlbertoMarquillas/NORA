## 06. Especificación del Bus de Eventos Internos en NORA

### Propósito del documento

Este documento define el sistema de eventos que estructura la comunicación entre módulos funcionales de NORA. Sirve como eje transversal que permite desacoplar los componentes, garantizar coherencia en el comportamiento y facilitar la sincronización multimodal.

Se especifican los tipos de eventos, su formato, mecanismos de distribución y prioridades.

---

### Principios del sistema de eventos

- **Modularidad:** cada módulo emite y escucha eventos sin conocer la lógica interna del resto.
- **Asincronía:** los eventos no bloquean el flujo del sistema; pueden gestionarse en paralelo.
- **Multicanal:** un evento puede generar múltiples respuestas (voz, luz, expresión).
- **Auditabilidad:** todos los eventos deben poder registrarse para depuración o análisis.

---

### Formato general de un evento

```json
{
  "tipo": "EVT_...",
  "origen": "modulo_emisor",
  "timestamp": "YYYY-MM-DD HH:MM:SS",
  "datos": { ... opcional ... },
  "prioridad": 1-5
}
```

- `tipo`: identificador único del evento
- `origen`: módulo que genera el evento
- `timestamp`: hora de emisión
- `datos`: diccionario con contenido relevante
- `prioridad`: nivel de atención requerida (1 = crítica, 5 = baja)

---

### Categorías de eventos

#### 1. Eventos de sistema (`sistema/`)
- `EVT_NFC_ACTIVATE`
- `EVT_NFC_DEACTIVATE`
- `EVT_INIT_COMPLETED`
- `EVT_SHUTDOWN_REQUEST`
- `EVT_IDLE_TIMEOUT`

#### 2. Eventos de visión (`vision/`)
- `EVT_FACE_DETECTED`
- `EVT_FACE_LOST`
- `EVT_POSTURE_ALERT`
- `EVT_PRESENCE_DETECTED`
- `EVT_ATTENTION_REQUEST`

#### 3. Eventos de voz (`voz/`)
- `EVT_COMMAND_RECOGNIZED`
- `EVT_COMMAND_UNKNOWN`
- `EVT_VOICE_INPUT_START`
- `EVT_VOICE_INPUT_END`

#### 4. Eventos de interacción (`interfaz/`)
- `EVT_EXPRESSION_REQUESTED`
- `EVT_LIGHT_COLOR_SET`
- `EVT_MOTION_TRIGGER`

#### 5. Eventos de datos (`datos/`)
- `EVT_RECORD_SAVED`
- `EVT_PROFILE_LOADED`
- `EVT_NOTE_REQUESTED`

---

### Mecanismo de distribución

Los eventos son distribuidos mediante un componente central `EventManager`, encargado de:
- Registrar oyentes (callbacks) por tipo de evento
- Encapsular eventos como objetos
- Asignar una cola prioritaria (por `asyncio.Queue` o equivalente)
- Ejecutar los manejadores correspondientes en el hilo o tarea adecuada

Ejemplo en pseudocódigo:

```python
evento = Evento(tipo="EVT_FACE_DETECTED", origen="vision", datos={...})
EventManager.emit(evento)
```

---

### Prioridades y gestión de concurrencia

| Prioridad | Uso típico                                 | Ejecución         |
|----------:|---------------------------------------------|-------------------|
| 1         | Apagado, errores críticos                   | Inmediata         |
| 2         | Activación, comandos validados              | Prioritaria       |
| 3         | Interacciones normales                      | Secuencial normal |
| 4         | Animaciones expresivas no esenciales        | Aplazable         |
| 5         | Logs, registros, retroalimentación tardía   | Bajas o en batch  |

---

### Ejemplo de flujo completo

1. `EVT_NFC_ACTIVATE` → `sistema/` activa modo `PASIVO`
2. `EVT_FACE_DETECTED` → `interfaz/` cambia a expresión atenta + `voz/` habilita escucha
3. `EVT_COMMAND_RECOGNIZED` → `datos/` guarda nota + `interfaz/` emite respuesta + luz verde
4. `EVT_IDLE_TIMEOUT` → `interfaz/` despide + `sistema/` entra en reposo

---

### Herramientas para monitoreo y depuración

- Consola con logs estructurados (`log_event(evento)`)
- Archivo de registro rotativo (`event_log.json`)
- Herramienta GUI de seguimiento en tiempo real (futura)

---

Este documento sirve como base para implementar el `EventManager`, definir interfaces de emisión y suscripción, y mantener la coherencia del comportamiento distribuido de NORA.