# Ficha Funcional – `monitor_salud_sistema.py`

## Nombre del archivo:
`monitor_salud_sistema.py`

## Responsabilidad principal:
Visualizar en la GUI el estado de salud del sistema operativo de NORA en tiempo real, incluyendo temperatura de CPU, uso de RAM, carga de CPU, estado de la red, y uptime. Permite al usuario identificar rápidamente condiciones críticas o subóptimas.

## Entradas esperadas:
- **Tipo de entrada:** Datos de supervisión del sistema operativo.
- **Fuente:** `supervision_estado.py`, `control_main.py`.
- **Formato o protocolo:** Lecturas de sensores internos, consultas al sistema operativo.

## Salidas generadas:
- **Tipo de salida:** Visualización en GUI de parámetros de salud, alertas de sobrecarga o fallo.
- **Destinatario:** Usuario (GUI).
- **Ejemplo de salida:**
  - Indicador de temperatura excesiva de CPU
  - Barra de progreso de uso de RAM
  - Semáforo de estado de conectividad

## Módulos relacionados:
- **Entrada desde:** `supervision_estado.py`, `control_main.py`.
- **Salida hacia:** Usuario (GUI).
- **Comunicación bidireccional con:** `gui_main.py` para actualización visual dinámica.

## Dependencias técnicas:
- **Librerías externas:** `tkinter`, `PyQt5`, `PySide2`, `psutil`.
- **Hardware gestionado:** CPU, RAM, interfaz de red.
- **Protocolos:** Consultas internas a sistema operativo.

## Notas adicionales:
`monitor_salud_sistema.py` debe representar visualmente los parámetros de manera clara, utilizando elementos como gráficas, indicadores de color y barras de progreso. Debe ser capaz de actualizar los datos en tiempo real o en intervalos cortos, sin bloquear la interacción general de la GUI.

