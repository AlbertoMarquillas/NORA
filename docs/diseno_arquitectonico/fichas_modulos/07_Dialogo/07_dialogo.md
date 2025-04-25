# Ficha Funcional – Módulo de Diálogo

## Nombre del módulo:
`dialogo/`

## Responsabilidad principal:
Gestiona el procesamiento de texto natural (NLU) y la generación de respuestas contextuales (NLG) para la interacción conversacional de NORA. Interpreta la intención del usuario, gestiona el contexto del diálogo y produce respuestas dinámicas adaptadas al estado emocional, ambiental y de interacción.

## Entradas esperadas:
- Tipo de entrada: texto reconocido, eventos emocionales, contexto de interacción
- Fuente: `voz/`, `agentes/`, `datos/`, `sistema/`
- Formato o protocolo: texto plano, eventos internos (`EVT_...`), estado conversacional

## Salidas generadas:
- Tipo de salida: texto generado para síntesis, comandos contextuales
- Destinatario: `voz/`, `interfaz/`, `sistema/`
- Ejemplo de salida:
  - Texto de respuesta: "Ahora mismo te lo digo."
  - `EVT_DIALOGUE_RESPONSE`, `EVT_DIALOGUE_CONFUSION`

## Módulos relacionados:
- Entrada desde: `voz/`, `agentes/`, `datos/`, `sistema/`
- Salida hacia: `voz/`, `interfaz/`, `sistema/`
- Comunicación bidireccional con: `agentes/` (modulación emocional y temática)

## Dependencias técnicas:
- Librerías externas: `transformers`, `sentence-transformers`, `nltk`, `spacy`, `json`
- Hardware gestionado: ninguno directamente
- Protocolos: eventos internos, flujo de texto estructurado

## Notas adicionales:
Permite entender el lenguaje natural del usuario, generar respuestas libres o estructuradas, y mantener coherencia temática en la conversación. Se puede integrar con modelos ligeros offline o utilizar servicios externos controlados si se requiere más potencia conversacional.

## Archivos previstos del módulo:
Listado de archivos `.py` que se espera implementar dentro del directorio `dialogo/` para estructurar sus funcionalidades.

- `dialogo_main.py`: Coordinador general del flujo de conversación.
- `nlu.py`: Análisis de intención, entidades y sentimiento en el texto recibido.
- `nlg.py`: Generación de lenguaje natural adaptado al contexto.
- `gestion_contexto.py`: Mantenimiento del estado conversacional y seguimiento de turnos.
- `adaptacion_emocional.py`: Ajuste de respuestas en función del estado emocional detectado.
- `manejo_incertidumbre.py`: Gestión de situaciones de baja comprensión o ambigüedad.
- `perfil_usuario_dialogo.py`: Ajuste de estilo conversacional según perfil de usuario.
- `memoria_conversacional.py`: Persistencia de información relevante durante la sesión.
- `respuestas_predefinidas.py`: Plantillas para respuestas estructuradas y fallback.
- `generacion_respuestas_dinamicas.py`: Producción de respuestas personalizadas basadas en contexto complejo.
- `correccion_asr.py`: Corrección automática de errores comunes de transcripción de voz.
- `prediccion_intencion.py`: Predicción anticipada de intenciones basadas en contexto e historial.
- `ajuste_formalidad.py`: Adaptación del nivel de formalidad en las respuestas según perfil o situación.
- `gestion_subcontextos.py`: Manejo de conversaciones paralelas y subtemas activos.
- `motor_historias.py`: Generación de narrativas dinámicas personalizadas durante la interacción.
- `config_dialogo.py`: Configuración de modelos, parámetros de respuesta, longitud máxima, sensibilidad.
- `utils_dialogo.py`: Funciones auxiliares de procesamiento de texto, normalización y validación.

