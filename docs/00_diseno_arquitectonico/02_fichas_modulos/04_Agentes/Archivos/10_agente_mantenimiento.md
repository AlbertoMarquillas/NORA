# Ficha Funcional – `agente_mantenimiento.py`

## Nombre del archivo:
`agente_mantenimiento.py`

## Responsabilidad principal:
Gestionar el mantenimiento preventivo y correctivo del sistema NORA, supervisando la salud de los componentes del sistema, como la memoria, el procesador, el almacenamiento y otros periféricos. Este agente detecta fallos potenciales y actúa para evitar problemas, además de generar alertas o tomar medidas correctivas cuando es necesario.

## Entradas esperadas:
- **Tipo de entrada:** Eventos de monitoreo del sistema, datos de sensores de hardware, registros de errores o fallos.
- **Fuente:** Módulos `control/` (para monitorear el estado del hardware), `sistema/` (para evaluar la carga y el rendimiento), sensores de diagnóstico.
- **Formato o protocolo:** Eventos internos (`EVT_MEMORY_ERROR`, `EVT_HARDWARE_FAILURE`), datos de estado del sistema en formato JSON.

## Salidas generadas:
- **Tipo de salida:** Alertas de mantenimiento, instrucciones para reiniciar componentes o realizar diagnósticos, medidas correctivas.
- **Destinatario:** `sistema/` (para reiniciar o ajustar el comportamiento de los módulos), `interfaz/` (para mostrar alertas de mantenimiento al usuario).
- **Ejemplo de salida:**
  - `AGT_MAINTENANCE_ALERT` (Evento que indica que se ha detectado un problema en el sistema que requiere atención).
  - `CMD_RESTART_COMPONENT` (Instrucción para reiniciar un componente del sistema, como el procesador o un módulo).
  - `AGT_SYSTEM_DIAGNOSTIC` (Instrucción para ejecutar un diagnóstico completo del sistema).

## Módulos relacionados:
- **Entrada desde:** `control/` (para obtener información sobre el estado y el rendimiento del sistema), `sistema/` (para verificar los logs de errores o fallos).
- **Salida hacia:** `sistema/` (para reiniciar o ajustar la configuración del sistema), `interfaz/` (para mostrar alertas y sugerencias de mantenimiento).
- **Comunicación bidireccional con:** `agentes/`, `sistema/` para coordinar acciones preventivas y correctivas en el sistema.

## Dependencias técnicas:
- **Librerías externas:** `psutil` (para monitoreo del sistema y recursos), `json` (para gestionar eventos y configuraciones de mantenimiento).
- **Hardware gestionado:** Ninguno directamente (se maneja a nivel lógico).
- **Protocolos:** Comunicación basada en eventos internos, integración con sistemas de monitoreo de hardware y gestión de fallos.

## Notas adicionales:
Este agente es fundamental para asegurar la estabilidad y fiabilidad de NORA. Monitorea continuamente los recursos del sistema, detectando posibles fallos o caídas en el rendimiento. Además de generar alertas de mantenimiento preventivo, puede ejecutar acciones correctivas, como reiniciar módulos o ajustar parámetros de funcionamiento para evitar problemas mayores. De esta forma, el agente garantiza que el sistema funcione de manera óptima a largo plazo.

## Archivos previstos del módulo:
- `agente_mantenimiento.py`: Supervisión de salud del sistema y prevención de fallos (este archivo).
- Archivos adicionales de agentes como `agente_confort.py`, `agente_base.py`.
