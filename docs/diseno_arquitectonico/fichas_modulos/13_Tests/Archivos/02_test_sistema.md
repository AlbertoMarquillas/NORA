# Ficha Funcional – `test_sistema.py`

## Nombre del archivo:
`test_sistema.py`

## Responsabilidad principal:
Contener pruebas unitarias y de integración destinadas a validar el funcionamiento del núcleo lógico del sistema NORA, incluyendo la gestión de estados, control de eventos y ejecución de comandos internos.

## Entradas esperadas:
- **Tipo de entrada:** Simulaciones de eventos, comandos internos, configuraciones de prueba.
- **Fuente:** `sistema/`.
- **Formato o protocolo:** Eventos simulados, llamadas a funciones de sistema.

## Salidas generadas:
- **Tipo de salida:** Resultados de tests, logs de validación de transición de estados y ejecución de comandos.
- **Destinatario:** `tests_main.py`, desarrolladores.
- **Ejemplo de salida:**
  - Validación de transición de `STATE_IDLE` a `STATE_ACTIVE`
  - Ejecución exitosa de `CMD_SHUTDOWN`

## Módulos relacionados:
- **Entrada desde:** `sistema/`.
- **Salida hacia:** `tests_main.py`.
- **Comunicación bidireccional con:** `sistema/` para pruebas dinámicas.

## Dependencias técnicas:
- **Librerías externas:** `unittest`, `pytest`, `mock`, `timeit`.
- **Hardware gestionado:** Ninguno.
- **Protocolos:** Pruebas de lógica de control de estados y eventos.

## Notas adicionales:
`test_sistema.py` debe cubrir tanto el comportamiento nominal esperado como situaciones límite y condiciones anómalas, garantizando la robustez de la lógica central de NORA. Debe comprobar la correcta propagación de eventos, las respuestas a comandos críticos y la estabilidad de la máquina de estados en diversos escenarios simulados.

