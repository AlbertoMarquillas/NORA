# Condiciones de salida – Estado: Error

El sistema NORA abandona el estado **Error** únicamente cuando se valida que la condición crítica que lo originó ha sido resuelta, contenida o superada. Esta decisión es tomada por la FSM principal (`sistema/`), en coordinación con el módulo `control/`, los agentes y, si está disponible, la intervención manual vía `gui/`.

---

## 1. Recuperación automática exitosa

- **Evento:** `EVT_RECOVERY_SUCCESS`  
  Emitido por el módulo `control/` tras verificación periódica del recurso fallido.  
  Implica que el módulo afectado ha sido reinicializado correctamente y responde a peticiones básicas.

---

## 2. Intervención manual

- **Comando:** `CMD_FORCE_RESUME`  
  Emitido desde la interfaz de supervisión `gui/` por el operador o desarrollador.  
  Permite forzar el retorno a estado `Activado` tras validación externa, incluso si el error persiste parcialmente.

---

## 3. Restablecimiento contextual

- **Evento:** `EVT_ENV_RESTORED`  
  En caso de error ambiental (`EVT_ENV_UNSAFE`), este evento indica que los sensores han vuelto a niveles seguros.  
  Ejemplo: temperatura reducida por debajo de umbral crítico, aire restablecido, etc.

---

## 4. Timeout sin agravamiento

- **Condición:** `t_error_recovery_timeout` alcanzado + estado estable  
  Si se cumple el tiempo máximo definido para intentar la recuperación automática (e.g. 30 segundos), y no se han recibido nuevos eventos de error, el sistema puede reiniciar el ciclo de activación.

---

## Consideraciones adicionales

- La transición desde `Error` solo puede realizarse hacia `Activado`.  
- No se permite el paso directo a `Escucha`, `Atencion` o `Procesando` tras error.  
- Si el error persiste tras 3 ciclos de recuperación, el sistema puede emitir `EVT_CRITICAL_FAILURE` y entrar en modo seguro si está implementado.
