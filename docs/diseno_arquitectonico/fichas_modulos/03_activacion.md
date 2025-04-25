# Ficha Funcional – Módulo de Activación

## Nombre del módulo:
`activacion/`

## Responsabilidad principal:
Gestiona la activación del sistema NORA a partir de múltiples fuentes de entrada físicas y lógicas. Centraliza la evaluación de eventos de activación como presencia física, atención visual, comandos de voz o identificación NFC, determinando si el sistema debe pasar a estado activo o interactivo.

## Entradas esperadas:
- Tipo de entrada: eventos de activación provenientes de sensores o módulos perceptivos
- Fuente: `sensores/`, `vision/`, `voz/`, botón físico GPIO
- Formato o protocolo: eventos internos del sistema (`EVT_PRESENCE_CONFIRMED`, `EVT_NFC_UID_DETECTED`, `EVT_WAKEWORD`, `EVT_ATTENTION_GAINED`, pulsaciones GPIO)

## Salidas generadas:
- Tipo de salida: eventos de activación o reposo
- Destinatario: `sistema/`, `agentes/`
- Ejemplo de salida:
  - `EVT_ACTIVATION_CONFIRMED`
  - `EVT_ACTIVATION_DENIED`
  - `EVT_REST_MODE_TRIGGERED`

## Módulos relacionados:
- Entrada desde: `sensores/`, `vision/`, `voz/`, lectura directa de GPIO (botón físico)
- Salida hacia: `sistema/`, `agentes/`
- Comunicación bidireccional con: `agentes/` (evaluación contextual de activación)

## Dependencias técnicas:
- Librerías externas: `gpiozero` (para botón físico), `pyee` o `eventbus` (para gestión de eventos internos)
- Hardware gestionado: botón físico de activación
- Protocolos: eventos internos, señales GPIO

## Notas adicionales:
Este módulo aplica una lógica combinada de activación, evaluando múltiples condiciones simultáneamente para minimizar falsos positivos. Puede delegar la decisión final de activación a los agentes cuando se requiera un análisis contextual más avanzado.

## Archivos previstos del módulo:
Listado de archivos `.py` que se espera implementar dentro del directorio `activacion/` para estructurar sus funcionalidades.

- `activacion_main.py`: Punto de entrada del módulo, escucha y evaluación de eventos de activación.
- `gestion_nfc.py`: Manejo específico de eventos provenientes del lector NFC.
- `gestion_presencia.py`: Evaluación de eventos de presencia detectada (ultrasónico, PIR).
- `gestion_atencion.py`: Análisis de atención visual detectada.
- `gestion_hotword.py`: Manejo de eventos de activación por palabra clave de voz.
- `gestion_boton.py`: Gestión de activación manual mediante botón físico.
- `decision_activacion.py`: Aplicación de lógica combinada para confirmar o rechazar la activación.
- `registro_fallos.py`: Registro de intentos fallidos de activación para análisis posterior.
- `control_hysteresis.py`: Gestión de tiempos de espera para evitar reactivaciones rápidas.
- `modo_no_molestar.py`: Implementación de modo de suspensión manual o programada de activación.
- `eventos_activacion.py`: Definición y emisión de eventos estándar del módulo.
- `config_activacion.py`: Parámetros configurables (tiempos de espera, prioridades, fuentes válidas).
- `utils_activacion.py`: Funciones auxiliares (validación de eventos, debounce de botones, etc.).

