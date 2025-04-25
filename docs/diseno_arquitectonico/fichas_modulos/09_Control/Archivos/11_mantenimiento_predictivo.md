# Ficha Funcional – `mantenimiento_predictivo.py`

## Nombre del archivo:
`mantenimiento_predictivo.py`

## Responsabilidad principal:
Analizar los patrones de funcionamiento y degradación de componentes para predecir posibles fallos futuros en el sistema NORA. Genera alertas preventivas, optimiza el mantenimiento y prolonga la vida útil de los dispositivos supervisados.

## Entradas esperadas:
- **Tipo de entrada:** Historial de supervisión de estado, registros de temperatura, carga de CPU, fallos menores, patrones de uso.
- **Fuente:** `supervision_estado.py`, `gestion_logs.py`, `control_main.py`.
- **Formato o protocolo:** Análisis de datos internos, lectura de logs, eventos de operación.

## Salidas generadas:
- **Tipo de salida:** Alertas de mantenimiento predictivo, recomendaciones de intervención, eventos de advertencia.
- **Destinatario:** `control_main.py`, `sistema/`, `gui/`.
- **Ejemplo de salida:**
  - `EVT_MAINTENANCE_REQUIRED`
  - `EVT_HARDWARE_DEGRADATION_DETECTED`

## Módulos relacionados:
- **Entrada desde:** `supervision_estado.py`, `gestion_logs.py`.
- **Salida hacia:** `control_main.py`, `sistema/`, `gui/`.
- **Comunicación bidireccional con:** Bases de datos de historial interno.

## Dependencias técnicas:
- **Librerías externas:** `datetime`, `statistics`, `logging`, `os`.
- **Hardware gestionado:** Supervisión indirecta de todos los dispositivos físicos.
- **Protocolos:** Análisis interno de registros.

## Notas adicionales:
`mantenimiento_predictivo.py` debe permitir detectar tendencias anómalas antes de que se produzcan fallos críticos, minimizando el tiempo de inactividad y optimizando la planificación de reparaciones o reemplazos. Sus alertas deben integrarse visualmente en `gui/` y registrarse en los logs del sistema para seguimiento histórico y auditoría técnica.