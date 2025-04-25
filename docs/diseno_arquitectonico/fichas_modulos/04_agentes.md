# Ficha Funcional – Módulo de Agentes

## Nombre del módulo:
`agentes/`

## Responsabilidad principal:
Implementa la capa de coordinación inteligente entre módulos sensoriales y actuadores. Cada agente representa una entidad lógica especializada que procesa eventos, toma decisiones contextuales, modula respuestas expresivas y prioriza acciones del sistema NORA.

## Entradas esperadas:
- Tipo de entrada: eventos de percepción, estado global del sistema, configuraciones dinámicas
- Fuente: `vision/`, `voz/`, `sensores/`, `sistema/`, configuración de usuario
- Formato o protocolo: eventos internos (`EVT_...`), estados, configuraciones JSON

## Salidas generadas:
- Tipo de salida: eventos derivados, modulaciones expresivas, prioridades de acción
- Destinatario: `sistema/`, `interfaz/`, `voz/`, `dialogo/`, `datos/`
- Ejemplo de salida:
  - `AGT_ATTENTION_CONFIRMED`
  - `CMD_PRIORIDAD_ALTA`
  - `CMD_SUPRIMIR_EVENTO`
  - Activación de escenas expresivas combinadas

## Módulos relacionados:
- Entrada desde: `vision/`, `voz/`, `sensores/`, `sistema/`
- Salida hacia: `interfaz/`, `voz/`, `sistema/`, `datos/`, `dialogo/`
- Comunicación bidireccional con: todos los módulos funcionales principales

## Dependencias técnicas:
- Librerías externas: `pyee`, `asyncio`, `eventbus` (sistema de eventos interno)
- Hardware gestionado: ninguno directamente (opera a nivel lógico)
- Protocolos: eventos internos, colas de mensajes

## Notas adicionales:
Cada agente implementa reglas específicas: perceptivas (detección, evaluación de contexto), expresivas (modulación de salida), o de activación (cambio de estados). La arquitectura permite crear nuevos agentes fácilmente mediante herencia de una clase base común.

## Archivos previstos del módulo:
Listado de archivos `.py` que se espera implementar dentro del directorio `agentes/` para estructurar sus funcionalidades.

- `agentes_main.py`: Coordinador central de los agentes activos.
- `agente_base.py`: Clase base abstracta para definir agentes.
- `agente_visual.py`: Evaluación de atención, emociones y gestos visuales.
- `agente_auditivo.py`: Evaluación de voz, emociones acústicas, interrupciones.
- `agente_contexto.py`: Gestión de activación combinada, inhibiciones, contexto horario.
- `agente_emocional.py`: Modulación de expresividad basada en estado emocional detectado.
- `agente_priorizacion.py`: Gestión de prioridades y supresión de eventos en competencia.
- `agente_habitos.py`: Evaluación de patrones de comportamiento o hábitos de usuario.
- `agente_seguridad.py`: Detección de anomalías, protección del sistema frente a accesos o comportamientos anómalos.
- `agente_confort.py`: Evaluación del confort ambiental y sugerencias de actuación.
- `agente_mantenimiento.py`: Supervisión de salud del sistema y prevención de fallos.
- `agente_adaptativo.py`: Aprendizaje y ajuste dinámico en función del comportamiento del usuario.
- `agente_emocion_prioritaria.py`: Priorización de respuesta ante emociones detectadas de alta intensidad.
- `escenas_expresivas.py`: Definición de combinaciones sincronizadas de expresión física, visual y verbal.
- `decision_agentes.py`: Aplicación de reglas dinámicas de activación o supresión de acciones.
- `config_agentes.py`: Parámetros configurables de sensibilidad, umbrales y perfiles de agentes.
- `utils_agentes.py`: Funciones comunes de evaluación, normalización y temporización.

