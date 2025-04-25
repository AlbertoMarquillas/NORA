# Ficha Funcional – `agente_seguridad.py`

## Nombre del archivo:
`agente_seguridad.py`

## Responsabilidad principal:
Gestionar la seguridad del sistema NORA, evaluando eventos relacionados con accesos no autorizados, anomalías en el comportamiento y posibles amenazas al sistema. Este agente es responsable de activar medidas preventivas o correctivas cuando se detectan comportamientos sospechosos o riesgos para la integridad del sistema.

## Entradas esperadas:
- **Tipo de entrada:** Eventos relacionados con accesos, monitoreo de comportamientos y señales de seguridad.
- **Fuente:** Módulos `sensores/` (sensores de proximidad, NFC), `sistema/` (estados de seguridad del sistema), otros agentes que generen eventos relacionados con la seguridad del sistema.
- **Formato o protocolo:** Eventos internos (`EVT_UNAUTHORIZED_ACCESS`, `EVT_SECURITY_ALERT`), registros de eventos en formato JSON que indican comportamientos sospechosos.

## Salidas generadas:
- **Tipo de salida:** Respuestas de seguridad, medidas preventivas o correctivas, alertas de seguridad.
- **Destinatario:** `sistema/` (para activar medidas de seguridad como la desactivación de sistemas o el bloqueo de accesos), `interfaz/` (para mostrar alertas o notificaciones de seguridad al usuario).
- **Ejemplo de salida:**
  - `AGT_SECURITY_ALERT` (Evento que indica que se ha detectado una posible amenaza o acceso no autorizado).
  - `CMD_BLOCK_ACCESS` (Instrucción para bloquear un acceso no autorizado o suspender una función de seguridad).
  - `AGT_SECURITY_MONITOR` (Evento que activa el monitoreo continuo para detectar comportamientos sospechosos).

## Módulos relacionados:
- **Entrada desde:** `sensores/` (para detectar accesos o proximidad de dispositivos), `sistema/` (para evaluar el estado de seguridad), otros agentes que puedan generar señales de riesgo.
- **Salida hacia:** `sistema/` (para bloquear accesos, suspender funciones o activar medidas de seguridad), `interfaz/` (para mostrar alertas de seguridad al usuario).
- **Comunicación bidireccional con:** `agentes/`, `sistema/` para realizar evaluaciones de seguridad y ejecutar respuestas adecuadas.

## Dependencias técnicas:
- **Librerías externas:** `paho-mqtt` (para comunicación con sistemas externos de monitoreo o alerta en tiempo real), `json` (para manejar eventos y configuraciones).
- **Hardware gestionado:** Ninguno directamente (se maneja a nivel lógico).
- **Protocolos:** Comunicación basada en eventos internos, integración con sistemas de monitoreo de seguridad y protección de accesos.

## Notas adicionales:
Este agente juega un papel crucial en garantizar la integridad y seguridad de NORA. Su función es detectar y reaccionar ante cualquier acceso no autorizado o comportamiento anómalo dentro del sistema. A través de sus interacciones con otros módulos de seguridad, el agente puede activar protocolos de defensa, como el bloqueo de acceso o la suspensión de funciones críticas. Además, puede generar alertas para que el sistema o el usuario estén al tanto de las amenazas detectadas.

## Archivos previstos del módulo:
- `agente_seguridad.py`: Detección de anomalías, protección del sistema frente a accesos o comportamientos anómalos (este archivo).
- Archivos adicionales de agentes como `agente_habitos.py`, `agente_base.py`.
