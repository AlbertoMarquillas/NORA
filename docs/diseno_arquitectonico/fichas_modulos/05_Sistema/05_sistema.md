# Ficha Funcional – Módulo de Sistema

## Nombre del módulo:
`sistema/`

## Responsabilidad principal:
Orquesta el comportamiento global del asistente NORA mediante una máquina de estados finita (FSM) y un sistema de gestión de eventos. Coordina la activación de módulos, la transición entre estados y la reacción coherente del sistema ante los estímulos recibidos.

## Entradas esperadas:
- Tipo de entrada: eventos generados por módulos perceptivos, agentes, configuraciones dinámicas
- Fuente: `vision/`, `voz/`, `sensores/`, `activacion/`, `agentes/`
- Formato o protocolo: eventos internos (`EVT_...`), comandos estructurados (`CMD_...`)

## Salidas generadas:
- Tipo de salida: comandos de actuación, transiciones de estado, registros de actividad
- Destinatario: `interfaz/`, `voz/`, `dialogo/`, `datos/`, `agentes/`
- Ejemplo de salida:
  - `CMD_EXPRESAR`
  - `CMD_RESPONDER`
  - `CMD_GUARDAR`
  - `EVT_STATE_CHANGED`

## Módulos relacionados:
- Entrada desde: `vision/`, `voz/`, `sensores/`, `activacion/`, `agentes/`
- Salida hacia: `interfaz/`, `voz/`, `dialogo/`, `datos/`, `agentes/`
- Comunicación bidireccional con: todos los módulos funcionales principales

## Dependencias técnicas:
- Librerías externas: `transitions` (FSM), `asyncio`, `queue`, `pyee` o `eventbus`
- Hardware gestionado: ninguno directamente (coordina módulos que sí interactúan con hardware)
- Protocolos: eventos internos, colas de mensajes, FSM estructurada

## Notas adicionales:
Este módulo actúa como el núcleo lógico de NORA. Define los modos de operación (`ESPERA`, `ACTIVO`, `INTERACTIVO`, `DORMIDO`, etc.), gestiona las prioridades del sistema, y asegura la coherencia intermodular. Integra inputs de múltiples fuentes para evaluar transiciones y acciones.

## Archivos previstos del módulo:
Listado de archivos `.py` que se espera implementar dentro del directorio `sistema/` para estructurar sus funcionalidades.

- `sistema_main.py`: Orquestador general del sistema, inicialización, ciclo principal de eventos.
- `fsm_control.py`: Definición de la máquina de estados y sus transiciones.
- `eventos_sistema.py`: Definición estandarizada de eventos y comandos internos.
- `gestion_eventos.py`: Captura, enrutamiento y distribución de eventos entre módulos.
- `control_prioridades.py`: Gestión de prioridades dinámicas y resolución de conflictos.
- `control_emocional.py`: Mantenimiento del estado emocional global e influencia sobre decisiones.
- `coordinacion_modular.py`: Asegura la coherencia entre módulos activos y estados del sistema.
- `monitor_consistencia.py`: Detección de desincronización o fallos lógicos, autocorrección.
- `planificador_tareas.py`: Programación y ejecución de acciones futuras o periódicas basadas en eventos o tiempos configurados.
- `gestion_fallos.py`: Supervisión y manejo de fallos internos, categorización y respuesta ante errores.
- `modulacion_estado.py`: Control dinámico de transiciones de estado basado en tendencias, históricos o patrones de comportamiento.
- `analisis_contextual.py`: Evaluación compleja de la situación global considerando múltiples factores simultáneamente.
- `perfil_dinamico_usuario.py`: Ajuste progresivo del comportamiento del sistema basado en la interacción histórica y preferencias del usuario.
- `config_sistema.py`: Definición de parámetros globales (tiempos, umbrales, configuraciones dinámicas).
- `utils_sistema.py`: Funciones auxiliares de tiempo, logging estructurado, conversión de estados.

