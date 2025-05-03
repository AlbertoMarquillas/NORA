# Ficha Funcional – `logger_sistema.py`

## Nombre del archivo:
`logger_sistema.py`

## Responsabilidad principal:
Inicializar y gestionar el sistema de logging estructurado principal de NORA. Permite registrar eventos, errores, advertencias y mensajes informativos de forma consistente en todo el sistema.

## Entradas esperadas:
- **Tipo de entrada:** Solicitudes de registro de logs, mensajes de eventos.
- **Fuente:** Todos los módulos funcionales (`sistema/`, `control/`, `voz/`, `vision/`, `interfaz/`, etc.).
- **Formato o protocolo:** Mensajes de texto estructurados, niveles de severidad (`INFO`, `WARNING`, `ERROR`, `CRITICAL`).

## Salidas generadas:
- **Tipo de salida:** Entradas en archivos de log estructurados, salida a consola opcional.
- **Destinatario:** Sistema de archivos, consola.
- **Ejemplo de salida:**
  - Registro de evento `INFO: Sistema iniciado correctamente`
  - Registro de error `ERROR: Fallo de conexión con módulo de visión`

## Módulos relacionados:
- **Entrada desde:** Todos los módulos funcionales.
- **Salida hacia:** Archivos de log, consola.
- **Comunicación bidireccional con:** No aplica (registro unidireccional).

## Dependencias técnicas:
- **Librerías externas:** `logging`, `os`, `datetime`.
- **Hardware gestionado:** Almacenamiento local para logs.
- **Protocolos:** Formato estándar de logging (timestamp, nivel, mensaje).

## Notas adicionales:
`logger_sistema.py` debe implementar rotación de archivos de log para evitar saturación del almacenamiento, niveles configurables de detalle (modo debug, producción) y ser resiliente ante fallos de escritura. El sistema de logging es esencial para el diagnóstico, la auditoría y el mantenimiento seguro de NORA.