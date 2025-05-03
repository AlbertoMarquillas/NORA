# Ficha Funcional – Módulo de GUI

## Nombre del módulo:
`gui/`

## Responsabilidad principal:
Proporciona una interfaz gráfica de usuario (GUI) para el control, monitoreo, diagnóstico y configuración de los diferentes módulos del sistema NORA, tanto en modo local como remoto.

## Entradas esperadas:
- Tipo de entrada: comandos del usuario, peticiones de estado, órdenes de configuración
- Fuente: interacción humana vía GUI
- Formato o protocolo: eventos GUI, comandos internos, formularios de configuración

## Salidas generadas:
- Tipo de salida: actualizaciones visuales, registros de eventos, órdenes de control
- Destinatario: `sistema/`, `control/`, `voz/`, `interfaz/`, `datos/`
- Ejemplo de salida:
  - Comando de reinicio de un módulo
  - Visualización del estado de sensores
  - Configuración de preferencias del usuario

## Módulos relacionados:
- Entrada desde: eventos del usuario (GUI)
- Salida hacia: `sistema/`, `control/`, `voz/`, `interfaz/`, `datos/`
- Comunicación bidireccional con: todos los módulos principales operativos

## Dependencias técnicas:
- Librerías externas: `tkinter`, `PyQt5`, `PySide2`, `flask`, `dash`, `streamlit` (opcional)
- Hardware gestionado: ninguno directamente (interacción indirecta con hardware a través de otros módulos)
- Protocolos: eventos internos, sockets web opcionales

## Notas adicionales:
El módulo `gui/` permite lanzar manualmente pruebas, visualizar el estado del sistema en tiempo real, modificar configuraciones dinámicamente, registrar logs y eventos críticos, así como administrar remotamente acciones de mantenimiento o control del sistema.

Además, ofrece control modular completo: permite encender, apagar, reiniciar o diagnosticar módulos individuales del sistema (`vision/`, `voz/`, `interfaz/`, `sensores/`, etc.), de forma manual o programada. La gestión modular se realiza mediante el envío de comandos específicos (`CMD_MODULE_START`, `CMD_MODULE_STOP`, `CMD_MODULE_RESTART`, `CMD_MODULE_DIAGNOSE`) hacia el núcleo del sistema o los módulos afectados.

## Archivos previstos del módulo:
Listado de archivos `.py` que se espera implementar dentro del directorio `gui/` para estructurar sus funcionalidades.

- `gui_main.py`: Coordinador principal de la interfaz gráfica.
- `panel_control.py`: Panel principal para control de estados del sistema.
- `monitor_eventos.py`: Monitor de eventos en tiempo real generado por los módulos.
- `configuracion_manual.py`: Edición de configuraciones dinámicas (preferencias, parámetros).
- `panel_diagnostico.py`: Herramientas de diagnóstico, control de sensores y visualización de hardware.
- `gestion_usuarios_gui.py`: Administración de perfiles de usuario desde la GUI.
- `monitor_salud_sistema.py`: Visualización del estado del sistema operativo y recursos.
- `panel_intervenciones.py`: Lanzamiento manual de pruebas, reinicios de módulos, acciones de mantenimiento.
- `simulador_interacciones.py`: Simulación de interacciones de usuario para pruebas y demostraciones.
- `servidor_web_gui.py`: Exposición opcional de la GUI a través de un servidor web local.
- `alertas_gui.py`: Visualización prioritaria de alertas y fallos críticos en la GUI.
- `historial_eventos_gui.py`: Historial visual filtrable de eventos y acciones del sistema.
- `editor_escenas_gui.py`: Edición gráfica de combinaciones expresivas (pantalla, LEDs, servos).
- `simulador_estados_gui.py`: Simulación manual de estados del sistema para pruebas FSM.
- `dashboard_rendimiento_gui.py`: Gráficas en tiempo real del rendimiento del sistema.
- `utils_gui.py`: Funciones auxiliares para renderizado, gestión de formularios y validación de entradas.

