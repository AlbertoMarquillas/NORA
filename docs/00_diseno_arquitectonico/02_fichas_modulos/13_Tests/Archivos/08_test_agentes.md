# Ficha Funcional – `test_agentes.py`

## Nombre del archivo:
`test_agentes.py`

## Responsabilidad principal:
Contener las pruebas unitarias y de integración destinadas a validar el comportamiento de los agentes perceptivos y expresivos de NORA, incluyendo reacciones a eventos, modulación emocional y adaptación de respuestas.

## Entradas esperadas:
- **Tipo de entrada:** Eventos simulados, entradas sensoriales ficticias, configuraciones de estados emocionales.
- **Fuente:** `agentes/`.
- **Formato o protocolo:** Estructuras de eventos, simulaciones de datos perceptivos.

## Salidas generadas:
- **Tipo de salida:** Reacciones de agentes, logs de comportamiento adaptativo.
- **Destinatario:** `tests_main.py`, desarrolladores.
- **Ejemplo de salida:**
  - Agente perceptivo detecta "proximidad" y cambia a "alerta"
  - Agente expresivo genera animación de "alegría" en respuesta a evento positivo

## Módulos relacionados:
- **Entrada desde:** `agentes/`.
- **Salida hacia:** `tests_main.py`.
- **Comunicación bidireccional con:** `agentes/` para ejecución de pruebas de comportamiento.

## Dependencias técnicas:
- **Librerías externas:** `unittest`, `pytest`, `mock`, `time`.
- **Hardware gestionado:** Opcional (pantallas, LEDs, servos en pruebas de expresividad).
- **Protocolos:** Evaluación de lógica de comportamiento y modulación expresiva.

## Notas adicionales:
`test_agentes.py` debe cubrir tanto la correcta interpretación de eventos como la generación de respuestas apropiadas en distintos contextos. Debe simular tanto condiciones normales como excepcionales, garantizando la coherencia y riqueza del comportamiento emocional y perceptivo de NORA.

