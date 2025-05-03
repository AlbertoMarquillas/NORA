# Ficha Funcional – `panel_diagnostico.py`

## Nombre del archivo:
`panel_diagnostico.py`

## Responsabilidad principal:
Proporcionar un panel gráfico desde el cual se puede acceder a herramientas de diagnóstico del sistema NORA. Permite al usuario consultar el estado de sensores, realizar pruebas de hardware, visualizar estados críticos y lanzar diagnósticos de integridad.

## Entradas esperadas:
- **Tipo de entrada:** Acciones del usuario (botones de prueba, selección de dispositivo, solicitud de estado).
- **Fuente:** Usuario (interacción GUI).
- **Formato o protocolo:** Eventos GUI, formularios de selección.

## Salidas generadas:
- **Tipo de salida:** Resultados de diagnóstico, logs de pruebas, eventos de error o confirmación de integridad.
- **Destinatario:** Usuario (visualización en GUI), `control/`, `sistema/`, `gestion_logs.py`.
- **Ejemplo de salida:**
  - Estado del sensor de temperatura
  - Prueba de conectividad WiFi
  - Diagnóstico del RTC externo

## Módulos relacionados:
- **Entrada desde:** Usuario (GUI).
- **Salida hacia:** `control/`, `sistema/`, `gestion_logs.py`.
- **Comunicación bidireccional con:** `gui_main.py` para coordinación y navegación.

## Dependencias técnicas:
- **Librerías externas:** `tkinter`, `PyQt5`, `PySide2`, `threading`.
- **Hardware gestionado:** Indirectamente sensores, módulo WiFi, RTC, GPIOs.
- **Protocolos:** Interno, basado en eventos y consultas a módulos de sistema.

## Notas adicionales:
`panel_diagnostico.py` debe permitir realizar diagnósticos tanto al arranque como a demanda, y mostrar los resultados de forma clara, incluyendo alertas visuales en caso de error. Debe ser capaz de lanzar diagnósticos automáticos o personalizados por componente y registrar los resultados en los logs del sistema para auditoría técnica posterior.

