# Ficha Funcional – `tests_main.py`

## Nombre del archivo:
`tests_main.py`

## Responsabilidad principal:
Coordinar la ejecución centralizada de todas las pruebas unitarias, de integración, de carga y de cobertura del sistema NORA. Facilita la automatización y supervisión completa del proceso de validación.

## Entradas esperadas:
- **Tipo de entrada:** Comandos de ejecución de pruebas, configuraciones de selección de tests.
- **Fuente:** `gui/`, terminal, futuros sistemas CI/CD.
- **Formato o protocolo:** Argumentos de línea de comandos, configuraciones JSON/YAML.

## Salidas generadas:
- **Tipo de salida:** Resultados agregados de pruebas, informes de cobertura, logs de ejecución.
- **Destinatario:** Desarrolladores, `gui/`, sistemas de integración continua.
- **Ejemplo de salida:**
  - Informe de 100% de cobertura en `utils/`
  - Detalle de fallo en `test_sistema.py`

## Módulos relacionados:
- **Entrada desde:** `gui/`, terminal, CI/CD.
- **Salida hacia:** Todos los subtests.
- **Comunicación bidireccional con:** Submódulos de `tests/` para ejecución y recolección de resultados.

## Dependencias técnicas:
- **Librerías externas:** `unittest`, `pytest`, `coverage`, `timeit`, `logging`.
- **Hardware gestionado:** Acceso indirecto durante pruebas de integración.
- **Protocolos:** Lanzamiento y supervisión de tests automatizados.

## Notas adicionales:
`tests_main.py` debe permitir la ejecución selectiva o completa de pruebas, la generación de reportes automáticos en distintos formatos (HTML, XML, JSON) y la integración sencilla con sistemas de CI/CD futuros. Su diseño modular debe facilitar la extensión de nuevas suites de prueba a medida que el sistema crezca.