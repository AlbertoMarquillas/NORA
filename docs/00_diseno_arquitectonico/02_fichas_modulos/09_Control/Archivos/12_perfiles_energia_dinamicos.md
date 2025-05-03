# Ficha Funcional – `perfiles_energia_dinamicos.py`

## Nombre del archivo:
`perfiles_energia_dinamicos.py`

## Responsabilidad principal:
Gestionar perfiles de consumo energético dinámicos en el sistema NORA, ajustando de forma automática la configuración de hardware y software según el contexto operativo (actividad del usuario, carga del sistema, estado de la red o condiciones ambientales).

## Entradas esperadas:
- **Tipo de entrada:** Datos de supervisión de estado, eventos de uso del sistema, condiciones externas (temperatura, conectividad).
- **Fuente:** `supervision_estado.py`, `control_main.py`, `sistema/`.
- **Formato o protocolo:** Eventos internos (`EVT_...`), evaluaciones de condiciones, reglas de contexto.

## Salidas generadas:
- **Tipo de salida:** Activación de perfiles energéticos, comandos de reducción de consumo, logs de transición de perfil.
- **Destinatario:** `control_main.py`, `gestion_energia.py`, `sistema/`.
- **Ejemplo de salida:**
  - `CMD_ACTIVAR_PERFIL_AHORRO`
  - `CMD_ACTIVAR_PERFIL_NORMAL`
  - `CMD_ACTIVAR_PERFIL_CRITICO`

## Módulos relacionados:
- **Entrada desde:** `supervision_estado.py`, `sistema/`.
- **Salida hacia:** `control_main.py`, `gestion_energia.py`, `sistema/`.
- **Comunicación bidireccional con:** `gestion_energia.py` (ejecución de medidas energéticas).

## Dependencias técnicas:
- **Librerías externas:** `datetime`, `logging`, `os`.
- **Hardware gestionado:** Comportamiento indirecto sobre sensores, actuadores y CPU.
- **Protocolos:** Interno al sistema operativo y GPIO.

## Notas adicionales:
`perfiles_energia_dinamicos.py` permite a NORA adaptarse inteligentemente a las condiciones de uso, garantizando un equilibrio óptimo entre rendimiento y eficiencia energética. Los perfiles deben ser configurables y modulables en tiempo real, y toda transición de perfil debe ser registrada y reflejada visualmente si es relevante para la experiencia del usuario.

