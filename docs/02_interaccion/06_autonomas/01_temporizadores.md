# Temporizadores – Reacciones Autónomas del Sistema

Este documento describe el sistema de temporización que permite a NORA generar reacciones autónomas ante inactividad o condiciones internas prolongadas. Su implementación se basa en contadores de tiempo y evaluaciones periódicas por parte de módulos de control.

---

## 1. Objetivo

Activar eventos autónomos cuando se supera un umbral temporal sin actividad, interacción o resolución de un estado.

---

## 2. Tipos de temporizadores definidos

| Temporizador      | Descripción                              | Evento generado               |
| ----------------- | ---------------------------------------- | ----------------------------- |
| `timeout_idle`    | Tiempo sin interacción en `STATE_IDLE`   | `EVT_AUTONOMOUS_SLEEP`        |
| `timeout_dialogo` | Espera sin respuesta en `STATE_DIALOGUE` | `EVT_AUTONOMOUS_REPEAT_QUERY` |
| `timeout_error`   | Persistencia de error sin resolución     | `EVT_AUTONOMOUS_RESTART`      |

---

## 3. Configuración y archivo de parámetros

Los valores se configuran en `config/temporizadores.json`:

```json
{
  "timeout_idle": 120,
  "timeout_dialogo": 30,
  "timeout_error": 10
}
```

---

## 4. Módulos implicados

* `estado/temporizadores.py`: gestiona la cuenta atrás y notifica vencimientos.
* `agentes/gestor_tiempo.py`: evalúa las condiciones y genera los eventos EVT\_\*
* `estado/fsm.py`: transiciona de estado según los eventos recibidos.

---

## 5. Lógica de funcionamiento

* Cada temporizador se activa en un estado concreto del sistema.
* Se reinician al detectar una interacción o cambio de estado.
* Si el tiempo excede el valor configurado, se genera el evento correspondiente.
* Se evita emitir el mismo evento repetidamente mediante marcas de inhibición.

---

## 6. Comportamientos derivados

* Transición a `STATE_SLEEP` tras inactividad
* Repetición automática de última pregunta si no se recibe respuesta
* Reinicio parcial o aviso verbal ante fallos no resueltos

---

El sistema de temporización dota a NORA de un comportamiento más autónomo, resiliente y adaptativo, contribuyendo a la percepción de asistencia continua y conciencia operativa.
