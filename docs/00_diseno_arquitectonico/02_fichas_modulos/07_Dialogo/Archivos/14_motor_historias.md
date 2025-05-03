# Ficha Funcional – `motor_historias.py`

## Nombre del archivo:
`motor_historias.py`

## Responsabilidad principal:
Generar narrativas dinámicas personalizadas durante la interacción de NORA con el usuario. Este archivo se encarga de crear historias o narrativas a partir de eventos y contexto de la conversación, permitiendo que NORA cuente historias personalizadas, adaptadas al usuario, al contexto emocional y a los intereses mostrados durante la interacción.

## Entradas esperadas:
- **Tipo de entrada:** Datos de contexto, eventos emocionales, intenciones del usuario.
- **Fuente:** `dialogo_main.py` (para recibir el contexto y el flujo de la conversación), `sistema/` (para recibir eventos de estado emocional y eventos del sistema).
- **Formato o protocolo:** Texto plano, eventos de contexto y emociones, datos estructurados (historias previas, datos de usuario).

## Salidas generadas:
- **Tipo de salida:** Narrativas generadas dinámicamente, historias personalizadas, eventos de narración.
- **Destinatario:** `voz/` (para convertir las historias en respuestas habladas), `sistema/` (para integrar las narrativas dentro de la interacción general del sistema).
- **Ejemplo de salida:**
  - `"Hace mucho tiempo, en un reino lejano..."` (Inicio de una historia personalizada).
  - `EVT_STORY_STARTED` (Evento que indica que una historia ha comenzado).
  - `CMD_PLAY_STORY` (Instrucción para comenzar la narración de una historia personalizada).

## Módulos relacionados:
- **Entrada desde:** `dialogo_main.py` (para recibir el contexto de la conversación y los temas de interés del usuario), `sistema/` (para adaptar las historias al estado emocional del usuario).
- **Salida hacia:** `voz/` (para convertir la narración en voz sintetizada), `sistema/` (para mantener el control del flujo de la interacción mientras se cuenta la historia).
- **Comunicación bidireccional con:** `sistema/`, `agentes/` para coordinar las narrativas con el contexto emocional y temático de la conversación.

## Dependencias técnicas:
- **Librerías externas:** `transformers` (para generación de texto dinámico), `nltk`, `spacy` (para el procesamiento de texto y generación de narrativas), `openai` (si se utiliza GPT u otros modelos para la creación de historias).
- **Hardware gestionado:** Ninguno directamente (se maneja la creación y reproducción de historias a nivel lógico).
- **Protocolos:** Comunicación basada en eventos internos, generación dinámica de texto adaptado al contexto de la conversación.

## Notas adicionales:
Este archivo es fundamental para que NORA pueda interactuar de una manera más creativa, contando historias que se adapten al contexto y a las emociones del usuario. **`motor_historias.py`** no solo genera historias estáticas, sino que también puede construir narrativas dinámicas y adaptadas, haciendo que la experiencia de conversación sea mucho más rica y envolvente. Este enfoque puede ser especialmente útil en interacciones de entretenimiento o cuando el usuario busca una experiencia más inmersiva.

## Archivos previstos del módulo:
- `motor_historias.py`: Generación de narrativas dinámicas personalizadas durante la interacción (este archivo).
- Archivos adicionales como `dialogo_main.py`, `generacion_respuestas_dinamicas.py`, `adaptacion_emocional.py`.
