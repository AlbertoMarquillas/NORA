# Acciones realizadas – Estado: Error

Durante el estado **Error**, el sistema NORA suspende temporalmente sus operaciones normales y ejecuta una rutina controlada de contención, diagnóstico y eventual recuperación. Este estado tiene prioridad máxima en la FSM y restringe el comportamiento a un conjunto limitado de acciones críticas, orientadas a garantizar la seguridad del sistema, la transparencia de la falla y la trazabilidad del incidente.

---

## 1. Notificación del error

- Activación de señal visual (LEDs en rojo fijo o intermitente) mediante `interfaz/`.
- Representación visual en pantalla: símbolo de advertencia, mensaje de estado o rostro neutro bloqueado.
- Emisión de señal acústica opcional (tono bajo, breve repetición) si el módulo `voz/` permanece operativo.

---

## 2. Aislamiento de módulos comprometidos

- Desactivación temporal del módulo afectado mediante `CMD_DISABLE_MODULE`.
- Suspensión del procesamiento en módulos dependientes para evitar efectos colaterales.

---

## 3. Registro de evento

- Generación del evento `EVT_ERROR_LOGGED` tras volcado de datos del incidente en el módulo `datos/`.
- Registro estructurado: timestamp, tipo de error, módulo afectado, descripción, posible causa.

---

## 4. Evaluación de recuperación

- Verificación periódica por parte del módulo `control/` sobre la disponibilidad del recurso afectado.
- Consulta a los agentes sobre la viabilidad de recuperación automática o manual.
- Inicio de temporizador de espera (`t_error_recovery_timeout`) para limitar el tiempo en este estado.

---

## 5. Supervisión y espera de intervención

- Activación del canal de monitorización en `gui/`, que permite al usuario consultar el estado, reiniciar módulos o forzar reinicio total.
- Emisión de eventos hacia el sistema de supervisión remota (si habilitado).

---

## Indicadores activos del sistema

| Componente        | Estado durante Error                         |
|-------------------|-----------------------------------------------|
| Pantalla facial   | Símbolo de error o rostro bloqueado          |
| LEDs RGB          | Rojo intermitente o patrón de advertencia    |
| Voz               | Silenciada o limitada a aviso de error       |
| FSM               | Congelada excepto transiciones de recuperación|
