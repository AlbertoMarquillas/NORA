# Gestión de Fallos – Reacciones Autónomas del Sistema

Este documento recoge el protocolo que sigue NORA para detectar, clasificar y reaccionar de forma autónoma ante fallos internos del sistema o errores de módulo. La capacidad de gestionar fallos sin intervención directa permite mantener un nivel básico de operatividad y preservar la coherencia del sistema frente a condiciones adversas.

---

## 1. Objetivo

Identificar fallos internos o condiciones anómalas persistentes y generar acciones correctivas automáticas que reduzcan la necesidad de reinicio manual o intervención del usuario.

---

## 2. Tipos de fallos detectables

| Tipo de fallo                | Ejemplo típico                                | Acción esperada                       |
| ---------------------------- | --------------------------------------------- | ------------------------------------- |
| Caída de un módulo           | `voz/tts.py` no responde tras 3 intentos      | Reintento + aviso visual              |
| Congelación de estado        | FSM estancada en estado sin transición válida | Reinicio parcial                      |
| Error crítico del sistema    | Memoria baja, corrupción de archivo           | Entrada en `STATE_ERROR`              |
| Fallo en lectura de sensores | Valores NaN repetidos o desconexión física    | Notificación + desactivación temporal |

---

## 3. Módulos de supervisión

* `monitor/supervisor.py`: detección de fallos críticos y bloqueos funcionales
* `estado/fsm.py`: transiciones incorrectas o tiempo excesivo en un estado
* `voz/`, `sensores/`, `datos/`: cada uno puede notificar errores al supervisor central

---

## 4. Reacciones automáticas

| Evento generado            | Acción ejecutada                           |
| -------------------------- | ------------------------------------------ |
| `EVT_AUTONOMOUS_RESTART`   | Reinicio parcial del módulo o estado       |
| `EVT_AUTONOMOUS_ERROR_MSG` | Mensaje verbal o visual indicando el error |
| `EVT_AUTONOMOUS_DISABLE`   | Desactivación de módulo dañado             |

---

## 5. Registro y trazabilidad

* Todos los errores se registran en `logs/fallos.log` con timestamp y severidad
* El sistema puede emitir verbalmente un resumen si el `modo_diagnostico` está activo
* Se permite notificación diferida al usuario mediante `notas del sistema`

---

## 6. Recuperación y persistencia

* El reinicio parcial preserva estado y configuración cuando es seguro hacerlo
* Si el sistema se reinicia más de N veces por fallo similar → se bloquea y requiere validación manual (previsto)

---

Este subsistema de gestión de fallos asegura que NORA mantenga su fiabilidad, incluso cuando operan múltiples procesos y sensores en paralelo, aumentando la tolerancia a errores y la autonomía correctiva.
