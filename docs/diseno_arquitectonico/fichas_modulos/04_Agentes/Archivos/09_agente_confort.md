# Ficha Funcional – `agente_confort.py`

## Nombre del archivo:
`agente_confort.py`

## Responsabilidad principal:
Gestionar el confort ambiental dentro del sistema NORA, evaluando eventos relacionados con las condiciones físicas del entorno, como la temperatura, la humedad y la calidad del aire. Este agente ajusta las respuestas del sistema en función del confort del usuario, proporcionando sugerencias o realizando cambios en el sistema para mejorar la experiencia del usuario.

## Entradas esperadas:
- **Tipo de entrada:** Datos ambientales relacionados con el confort del entorno, como temperatura, humedad, calidad del aire.
- **Fuente:** Módulos `sensores/` (DHT22, BME280, MQ-135, CCS811) que proporcionan datos sobre las condiciones ambientales.
- **Formato o protocolo:** Eventos de sensores (`EVT_TEMP_HIGH`, `EVT_HUMIDITY_LOW`), datos en formato JSON provenientes de los sensores.

## Salidas generadas:
- **Tipo de salida:** Sugerencias para ajustar el entorno o las condiciones, alertas relacionadas con el confort.
- **Destinatario:** `interfaz/` (para mostrar notificaciones o sugerencias de confort al usuario), `sistema/` (para ajustar el comportamiento del sistema en función de las condiciones ambientales).
- **Ejemplo de salida:**
  - `AGT_COMFORT_ALERT` (Evento que indica que una condición ambiental ha alcanzado un umbral de confort).
  - `CMD_SUGGEST_ADJUSTMENT` (Instrucción para sugerir ajustes, como encender un ventilador o cambiar la temperatura).
  - `AGT_COMFORT_MODIFICATION` (Instrucción para modificar un parámetro de confort, como la humedad o la temperatura).

## Módulos relacionados:
- **Entrada desde:** `sensores/` (para obtener datos ambientales sobre temperatura, humedad y calidad del aire).
- **Salida hacia:** `interfaz/` (para mostrar alertas o sugerencias de confort), `sistema/` (para aplicar ajustes en el entorno según los datos recibidos).
- **Comunicación bidireccional con:** `agentes/`, `sistema/`, `interfaz/` para coordinar las respuestas y acciones relacionadas con el confort del usuario.

## Dependencias técnicas:
- **Librerías externas:** `paho-mqtt` (para comunicación en tiempo real con sensores o sistemas externos), `json` (para manejar eventos y configuraciones de confort).
- **Hardware gestionado:** Ninguno directamente (se maneja a nivel lógico).
- **Protocolos:** Comunicación basada en eventos internos, integración con sensores de confort y ajustes del sistema en función de las condiciones detectadas.

## Notas adicionales:
Este agente es esencial para asegurar que el entorno de NORA sea confortable para el usuario. Evalúa las condiciones ambientales y realiza ajustes según los umbrales de confort predefinidos o los hábitos del usuario. Además, puede generar sugerencias o alertas para que el usuario tome decisiones sobre cómo mejorar el confort ambiental, como ajustar la temperatura, controlar la humedad o mejorar la calidad del aire.

## Archivos previstos del módulo:
- `agente_confort.py`: Evaluación del confort ambiental y sugerencias de actuación (este archivo).
- Archivos adicionales de agentes como `agente_seguridad.py`, `agente_base.py`.
