# Ficha Funcional – `test_sensores.py`

## Nombre del archivo:
`test_sensores.py`

## Responsabilidad principal:
Contener las pruebas unitarias y de integración destinadas a validar la lectura, interpretación y generación de eventos a partir de los sensores físicos conectados al sistema NORA.

## Entradas esperadas:
- **Tipo de entrada:** Lecturas simuladas o reales de sensores, configuraciones de sensores, eventos de activación.
- **Fuente:** `sensores/`.
- **Formato o protocolo:** Lecturas numéricas, estados digitales, configuraciones estructuradas.

## Salidas generadas:
- **Tipo de salida:** Validación de datos sensoriales, generación de eventos, logs de lectura.
- **Destinatario:** `tests_main.py`, desarrolladores.
- **Ejemplo de salida:**
  - Detección correcta de proximidad
  - Activación de evento `EVT_SENSOR_TRIGGERED`

## Módulos relacionados:
- **Entrada desde:** `sensores/`.
- **Salida hacia:** `tests_main.py`.
- **Comunicación bidireccional con:** `sensores/` para simulación y verificación de lecturas.

## Dependencias técnicas:
- **Librerías externas:** `unittest`, `pytest`, `mock`, `smbus2`, `RPi.GPIO`, `numpy`.
- **Hardware gestionado:** Sensores digitales y analógicos conectados al sistema.
- **Protocolos:** Lectura y procesamiento de datos de sensores.

## Notas adicionales:
`test_sensores.py` debe evaluar tanto la correcta captura de datos sensoriales como la generación precisa de eventos internos a partir de ellos. Además, debe validar el comportamiento del sistema frente a lecturas anómalas, desconexiones o fallos simulados para asegurar la robustez del subsistema de percepción.