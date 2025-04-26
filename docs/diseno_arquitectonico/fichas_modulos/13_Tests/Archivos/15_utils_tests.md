# Ficha Funcional – `utils_tests.py`

## Nombre del archivo:
`utils_tests.py`

## Responsabilidad principal:
Proporcionar funciones auxiliares para la generación de datos simulados, creación de mocks, fixtures reutilizables y soporte a la automatización de las pruebas del sistema NORA.

## Entradas esperadas:
- **Tipo de entrada:** Solicitudes de generación de datos de prueba, creación de entornos simulados.
- **Fuente:** `tests/`.
- **Formato o protocolo:** Parámetros de generación de datos, configuraciones de mocks.

## Salidas generadas:
- **Tipo de salida:** Datos ficticios, instancias de objetos simulados, configuraciones de fixtures.
- **Destinatario:** Ficheros de prueba del módulo `tests/`.
- **Ejemplo de salida:**
  - Generación de un evento ficticio para pruebas
  - Creación de un mock de conexión de sensor

## Módulos relacionados:
- **Entrada desde:** `tests_main.py`, pruebas de `utils/`, `sistema/`, `voz/`, `vision/`, `interfaz/`, `datos/`, `control/`, `agentes/`, `models/`, `gui/`.
- **Salida hacia:** Ficheros de pruebas que requieran soporte simulado.
- **Comunicación bidireccional con:** No aplica (funciones de soporte).

## Dependencias técnicas:
- **Librerías externas:** `unittest.mock`, `faker`, `random`, `time`, `uuid`.
- **Hardware gestionado:** Ninguno.
- **Protocolos:** Generación automática de datos y simulación de comportamientos.

## Notas adicionales:
`utils_tests.py` debe facilitar la creación rápida y flexible de datos de prueba coherentes, mocks de objetos o funciones, y entornos controlados para realizar pruebas robustas, aisladas y reproducibles dentro del sistema de validación de NORA.

