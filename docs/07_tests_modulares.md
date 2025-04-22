## 07. Plan de Pruebas Modulares para el Sistema NORA

### Propósito del documento

Este documento detalla las pruebas unitarias y funcionales previstas para cada uno de los módulos del sistema NORA. Tiene como objetivo garantizar la estabilidad, coherencia y verificabilidad del comportamiento de cada componente tanto en modo simulado como en hardware real.

Cada prueba sigue un patrón definido, con entradas esperadas, comportamiento observado y criterios de éxito.

---

### Estructura de carpetas de prueba

```
/tests/
|-- test_vision.py
|-- test_voz.py
|-- test_interfaz.py
|-- test_control.py
|-- test_sistema.py
|-- test_datos.py
|-- test_eventos.py
|-- recursos/         # Imágenes, audios, perfiles para prueba
```

---

### Pruebas por módulo

#### 1. `vision/`
- **Test: detección facial básica**
  - Entrada: imagen/video con rostro
  - Salida esperada: `EVT_FACE_DETECTED`
- **Test: pérdida de rostro**
  - Entrada: desaparición de rostro en escena
  - Salida esperada: `EVT_FACE_LOST`
- **Test: detección postural**
  - Entrada: postura inclinada mantenida
  - Salida esperada: `EVT_POSTURE_ALERT`

#### 2. `voz/`
- **Test: reconocimiento de comando claro**
  - Entrada: "recuérdame beber agua"
  - Salida esperada: `EVT_COMMAND_RECOGNIZED` + texto esperado
- **Test: entrada confusa o incompleta**
  - Entrada: ruido o frase parcial
  - Salida esperada: `EVT_COMMAND_UNKNOWN`
- **Test: síntesis de voz**
  - Entrada: texto arbitrario
  - Salida esperada: audio generado correctamente

#### 3. `interfaz/`
- **Test: cambio de expresión facial**
  - Entrada: `EVT_EXPRESSION_REQUESTED` con parámetro
  - Resultado: cambio visual observable en GUI
- **Test: luz RGB**
  - Entrada: `EVT_LIGHT_COLOR_SET` con color
  - Resultado: color actualizado en GUI de simulación

#### 4. `control/`
- **Test: movimiento físico simulado**
  - Entrada: `EVT_MOTION_TRIGGER`
  - Resultado: log de servo virtual, cambio de orientación

#### 5. `sistema/`
- **Test: ciclo de activación completo**
  - Entrada: `EVT_NFC_ACTIVATE`
  - Resultado: estado `REPOSO → PASIVO → ESCUCHA`
- **Test: cierre ordenado**
  - Entrada: `EVT_SHUTDOWN_REQUEST`
  - Resultado: transición a `DESPEDIDA` y reposo

#### 6. `datos/`
- **Test: guardar nota por voz**
  - Entrada: `EVT_COMMAND_RECOGNIZED` con texto válido
  - Resultado: entrada añadida a SQLite
- **Test: recuperación de eventos**
  - Entrada: `EVT_NOTE_REQUESTED`
  - Resultado: consulta satisfactoria y retorno por voz

#### 7. `eventos/`
- **Test: emisión y propagación de evento**
  - Entrada: objeto `Evento`
  - Resultado: ejecución del callback suscrito correspondiente
- **Test: orden en cola por prioridad**
  - Entrada: varios eventos con prioridades distintas
  - Resultado: ejecución en orden correcto

---

### Herramientas recomendadas

- `pytest` para ejecución de pruebas automáticas
- `unittest` como marco base
- `coverage` para medición de líneas ejecutadas
- `mock` para sustitución de módulos de hardware
- `logging` con nivel DEBUG para trazabilidad

---

### Ejemplo de ejecución

```bash
$ pytest tests/test_voz.py -v
TEST reconocimiento OK
TEST síntesis OK
```

---

### Criterios de validación

- Cada módulo debe ser verificable de forma independiente
- Las salidas deben poder observarse vía logs, GUI o voz
- No se permiten dependencias cruzadas sin mediación por eventos
- Los fallos deben ser gestionados con eventos `ERROR` o logs controlados

---

Este plan de pruebas se actualizará conforme se implementen nuevos submódulos o se amplíe el alcance del sistema NORA.