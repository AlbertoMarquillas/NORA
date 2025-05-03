# Condiciones de Disparo – Interacción Contextual o Ambiental

Este documento establece las reglas y umbrales que determinan cuándo un cambio ambiental se considera suficientemente relevante como para generar un evento de contexto en NORA. Estas condiciones se aplican sobre los datos recogidos por los sensores, y pueden depender del estado del sistema o de la combinación de factores.

---

## 1. Regla general de evaluación

Todo sensor registrado genera una lectura periódica. Cada valor se compara con un umbral o condición definida. Si se cumple y persiste durante un tiempo mínimo, se genera un `EVT_CONTEXT_XXX` asociado.

* Se evita la emisión de eventos espurios por ruido o picos breves.
* La lógica se gestiona desde `agentes/contexto.py`.

---

## 2. Tabla de condiciones por tipo

| Sensor              | Condición                 | Tiempo mínimo | Evento generado               |
| ------------------- | ------------------------- | ------------- | ----------------------------- |
| LDR (luz)           | Lux < 20                  | 3 s           | `EVT_CONTEXT_LOW_LIGHT`       |
| DHT22 (temperatura) | Temp > 30 °C              | 5 s           | `EVT_CONTEXT_TEMP_HIGH`       |
| DHT22 (humedad)     | Hum < 30 %                | 10 s          | `EVT_CONTEXT_HUMID_LOW`       |
| Micrófono           | RMS > 70 dB (media móvil) | 2 s           | `EVT_CONTEXT_NOISE_HIGH`      |
| PIR                 | Señal HIGH detectada      | instantáneo   | `EVT_CONTEXT_MOTION_DETECTED` |
| Sistema interno     | Estado = ERROR\_CRITICO   | persistente   | `EVT_CONTEXT_SYS_FAILURE`     |

---

## 3. Condiciones compuestas (futuro)

* `Luz baja + presencia + silencio` → activar modo de atención discreta
* `Temperatura alta + CPU alta` → emitir advertencia y reducir carga

Estas reglas se podrán definir mediante un sistema declarativo tipo JSON o YAML para facilitar ajustes sin recompilar.

---

## 4. Modulación por estado del sistema

Algunas condiciones solo deben dispararse si el sistema está en un estado compatible:

* `EVT_CONTEXT_NOISE_HIGH` solo se procesa en `STATE_ATTENTION` o `STATE_DIALOGUE`
* `EVT_CONTEXT_LOW_LIGHT` puede ser ignorado en `STATE_SLEEP`

---

## 5. Supresión y ventana de retardo

* Cada evento tiene un *tiempo de silencio* tras su emisión para evitar repeticiones (ej. 10 s para `NOISE_HIGH`).
* Se pueden combinar condiciones mediante lógica de agentes para evitar reacciones incoherentes.

---

Estas condiciones de disparo aseguran que NORA reaccione solo ante cambios ambientales significativos, reduciendo ruido operativo y aumentando la relevancia de sus respuestas contextuales.
