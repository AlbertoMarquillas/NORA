# Ficha Funcional – `panel_intervenciones.py`

## Nombre del archivo:
`panel_intervenciones.py`

## Responsabilidad principal:
Proporcionar un panel en la GUI para ejecutar manualmente intervenciones técnicas sobre el sistema NORA. Permite al usuario lanzar pruebas específicas, reiniciar módulos de forma individual, exportar logs de sistema y forzar acciones de mantenimiento.

## Entradas esperadas:
- **Tipo de entrada:** Acciones de usuario (selección de prueba, comandos manuales, solicitudes de exportación).
- **Fuente:** Usuario (interacción GUI).
- **Formato o protocolo:** Eventos GUI, comandos estructurados.

## Salidas generadas:
- **Tipo de salida:** Comandos de intervención, resultados de pruebas, confirmaciones de acción.
- **Destinatario:** `control/`, `sistema/`, `gestion_logs.py`, `gui_main.py`.
- **Ejemplo de salida:**
  - `CMD_EXPORT_LOGS`
  - `CMD_RESTART_MODULE('voz')`
  - Resultado de prueba de sensores

## Módulos relacionados:
- **Entrada desde:** Usuario (GUI).
- **Salida hacia:** `control/`, `sistema/`, `gestion_logs.py`.
- **Comunicación bidireccional con:** `gui_main.py` para gestión de interfaz y resultados.

## Dependencias técnicas:
- **Librerías externas:** `tkinter`, `PyQt5`, `PySide2`, `os`, `subprocess`.
- **Hardware gestionado:** Indirectamente a través de acciones sobre módulos.
- **Protocolos:** Comandos internos, sistema operativo.

## Notas adicionales:
`panel_intervenciones.py` debe ofrecer una interfaz intuitiva y segura, solicitando confirmaciones en acciones críticas como reinicios o exportaciones, y mostrando resultados claros de cada intervención. Debe estar preparado para operar tanto en entorno de desarrollo como en entornos productivos donde se requiera mantenimiento programado o correctivo.