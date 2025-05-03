# Ficha Funcional – `dashboard_rendimiento_gui.py`

## Nombre del archivo:
`dashboard_rendimiento_gui.py`

## Responsabilidad principal:
Mostrar un dashboard visual en tiempo real del rendimiento del sistema NORA. Representa gráficamente métricas como uso de CPU, memoria, actividad de red, y tiempos de respuesta de módulos activos.

## Entradas esperadas:
- **Tipo de entrada:** Datos de supervisión del sistema operativo y métricas internas.
- **Fuente:** `supervision_estado.py`, `control_main.py`, `sistema/`.
- **Formato o protocolo:** Datos de monitoreo estructurados.

## Salidas generadas:
- **Tipo de salida:** Gráficos de rendimiento, alertas visuales por sobrecarga, logs opcionales de rendimiento.
- **Destinatario:** Usuario (GUI).
- **Ejemplo de salida:**
  - Gráfico de uso de CPU en tiempo real
  - Histórico de carga de red
  - Alerta de memoria crítica

## Módulos relacionados:
- **Entrada desde:** `supervision_estado.py`, `control_main.py`, `sistema/`.
- **Salida hacia:** Usuario (GUI).
- **Comunicación bidireccional con:** `gui_main.py` para sincronización de actualizaciones.

## Dependencias técnicas:
- **Librerías externas:** `tkinter`, `PyQt5`, `PySide2`, `matplotlib`, `plotly`, `psutil`.
- **Hardware gestionado:** CPU, RAM, interfaces de red (supervisión).
- **Protocolos:** Interno basado en métricas de sistema operativo.

## Notas adicionales:
`dashboard_rendimiento_gui.py` debe garantizar una visualización fluida y eficiente de las métricas, utilizando actualizaciones asíncronas o por intervalos para evitar sobrecargar la GUI. Debe permitir escalabilidad futura para añadir nuevas métricas o adaptar la visualización a distintos modos operativos o perfiles de usuario.