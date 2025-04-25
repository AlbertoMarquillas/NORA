# Ficha Funcional – `gestion_fallos.py`

## Nombre del archivo:
`gestion_fallos.py`

## Responsabilidad principal:
Supervisar y manejar los fallos internos del sistema NORA, categorizando los errores detectados y tomando las acciones correctivas apropiadas. Este archivo es responsable de identificar fallos en el sistema, evaluar su severidad y activar procedimientos de recuperación o notificación.

## Entradas esperadas:
- **Tipo de entrada:** Registros de error, eventos de fallo, señales de desincronización o malfuncionamiento de módulos.
- **Fuente:** Módulos `sistema/`, `agentes/`, `interfaz/`, `voz/`, `sensores/`, que emiten eventos relacionados con errores o fallos en el sistema.
- **Formato o protocolo:** Eventos de error (`EVT_MODULE_FAILURE`, `EVT_SYSTEM_ERROR`), comandos de diagnóstico o recuperación.

## Salidas generadas:
- **Tipo de salida:** Notificaciones de error, acciones correctivas, comandos para reiniciar módulos o sistemas.
- **Destinatario:** `sistema/` (para reiniciar módulos o restablecer el sistema), `interfaz/` (para mostrar alertas o notificaciones al usuario).
- **Ejemplo de salida:**
  - `EVT_SYSTEM_RECOVERY` (Evento que indica que se ha tomado una acción correctiva y el sistema ha recuperado su funcionamiento).
  - `CMD_RESTART_MODULE` (Instrucción para reiniciar un módulo que ha fallado).
  - `AGT_ERROR_NOTIFIED` (Notificación de que un fallo ha sido reportado y manejado).

## Módulos relacionados:
- **Entrada desde:** `sistema/`, `agentes/`, `interfaz/`, `voz/` (para recibir eventos de fallos en el sistema o los módulos).
- **Salida hacia:** `sistema/`, `agentes/`, `interfaz/` (para activar la recuperación de fallos, reiniciar módulos, o notificar al usuario sobre el fallo).
- **Comunicación bidireccional con:** `sistema/`, `agentes/`, `interfaz/` para coordinar la recuperación de fallos y la notificación al usuario.

## Dependencias técnicas:
- **Librerías externas:** `logging` (para registrar eventos de fallo), `pyee` o `eventbus` (para gestionar eventos de recuperación o fallos).
- **Hardware gestionado:** Ninguno directamente (gestiona la recuperación lógica de módulos y componentes del sistema).
- **Protocolos:** Comunicación basada en eventos internos, gestión de errores y fallos, recuperación de sistemas.

## Notas adicionales:
Este archivo es crucial para asegurar la fiabilidad y la estabilidad del sistema NORA. Al monitorizar los módulos en busca de errores y fallos, `gestion_fallos.py` puede tomar medidas correctivas automáticamente, como reiniciar módulos fallidos o notificar al usuario de que se ha producido un error. La gestión de fallos permite que el sistema continúe funcionando de manera eficiente incluso cuando se presenten problemas técnicos, garantizando la continuidad del servicio.

## Archivos previstos del módulo:
- `gestion_fallos.py`: Supervisión y manejo de fallos internos, categorización y respuesta ante errores (este archivo).
- Archivos adicionales como `monitor_consistencia.py`, `gestion_eventos.py`.
