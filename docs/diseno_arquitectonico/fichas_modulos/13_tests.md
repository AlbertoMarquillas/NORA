# Ficha Funcional – Módulo de Pruebas

## Nombre del módulo:
`tests/`

## Responsabilidad principal:
Contener todos los scripts, rutinas y casos de prueba destinados a validar el correcto funcionamiento de los módulos de software del sistema NORA, tanto de forma aislada (unit testing) como integrada (integration testing) y bajo condiciones simuladas o de estrés.

## Entradas esperadas:
- Tipo de entrada: comandos de ejecución de pruebas, parámetros de prueba, configuraciones de entorno
- Fuente: `gui/`, desarrolladores vía terminal, CI/CD (opcional en el futuro)
- Formato o protocolo: scripts de prueba, configuraciones JSON/YAML, eventos simulados

## Salidas generadas:
- Tipo de salida: resultados de tests, informes de cobertura, logs de validación
- Destinatario: desarrolladores, `gui/`, sistema de monitorización
- Ejemplo de salida:
  - Informe de éxito/fallo de test unitario
  - Resumen de cobertura de código
  - Logs de fallos detectados durante integración

## Módulos relacionados:
- Entrada desde: `gui/`, terminal, sistemas de CI/CD
- Salida hacia: todos los módulos que sean sometidos a prueba
- Comunicación bidireccional con: todos los módulos operativos

## Dependencias técnicas:
- Librerías externas: `unittest`, `pytest`, `doctest`, `coverage`, `faker`, `mock`, `timeit`
- Hardware gestionado: acceso indirecto a sensores y actuadores durante pruebas de integración
- Protocolos: ejecución controlada de funciones, simulación de eventos

## Notas adicionales:
El módulo `tests/` permite validar individualmente funciones, integrar módulos, simular eventos reales o fallos, analizar rendimiento bajo carga y garantizar la robustez general del sistema antes de despliegues o actualizaciones.

## Archivos previstos del módulo:
Listado de archivos `.py` que se espera implementar dentro del directorio `tests/` para estructurar sus funcionalidades.

- `tests_main.py`: Coordinador principal de ejecución de pruebas.
- `test_utils.py`: Pruebas unitarias del módulo `utils/`.
- `test_sistema.py`: Pruebas unitarias e integración del núcleo `sistema/`.
- `test_voz.py`: Pruebas de ASR, TTS, y procesamiento de voz.
- `test_vision.py`: Pruebas de procesamiento visual, detección facial, gestos y emociones.
- `test_interfaz.py`: Pruebas de salida gráfica, LEDs, servos.
- `test_datos.py`: Validación de almacenamiento, recuperación, consistencia de datos.
- `test_control.py`: Pruebas de inicialización de hardware, supervisión, gestión energética.
- `test_agentes.py`: Evaluación del comportamiento de los agentes perceptivos y expresivos.
- `test_models.py`: Validación de carga, inferencia y rendimiento de modelos de IA.
- `test_gui.py`: Pruebas de interacción gráfica, simulaciones y control de módulos desde GUI.
- `test_sensores.py`: Validación de lectura, interpretación y eventos generados por sensores.
- `test_eventos.py`: Pruebas de generación, propagación y captura de eventos internos.
- `tests_stress_load.py`: Simulación de carga elevada para medir tiempos de respuesta y estabilidad.
- `tests_coverage_analysis.py`: Análisis de cobertura de código de todos los módulos.
- `utils_tests.py`: Funciones de soporte para generación de datos simulados, mocks y fixtures.

