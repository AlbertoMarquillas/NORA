# Ficha Funcional – `generador_ids_unicos.py`

## Nombre del archivo:
`generador_ids_unicos.py`

## Responsabilidad principal:
Generar identificadores únicos de alta entropía para eventos, sesiones, transacciones o recursos internos de NORA. Garantiza unicidad y trazabilidad de operaciones en todo el sistema.

## Entradas esperadas:
- **Tipo de entrada:** Solicitudes de generación de ID, parámetros opcionales de prefijo o formato.
- **Fuente:** `sistema/`, `voz/`, `vision/`, `interfaz/`, `control/`, `datos/`, `agentes/`, `tests/`.
- **Formato o protocolo:** Opcionalmente estructuras de configuración (prefijos, longitud).

## Salidas generadas:
- **Tipo de salida:** Cadenas de texto con IDs únicos.
- **Destinatario:** Módulos funcionales que requieran identificación de instancias.
- **Ejemplo de salida:**
  - ID de evento: `EVT_20240427_ABC123DEF456`
  - ID de sesión: `SESSION_20240427_789XYZ`

## Módulos relacionados:
- **Entrada desde:** `sistema/`, `voz/`, `vision/`, `interfaz/`, `control/`, `datos/`, `agentes/`, `tests/`.
- **Salida hacia:** Módulos funcionales.
- **Comunicación bidireccional con:** No aplica (funciones de soporte).

## Dependencias técnicas:
- **Librerías externas:** `uuid`, `datetime`, `random`, `secrets`.
- **Hardware gestionado:** Ninguno.
- **Protocolos:** Generación de UUIDs, IDs compuestos basados en fecha y aleatoriedad.

## Notas adicionales:
`generador_ids_unicos.py` debe ofrecer distintas estrategias de generación (UUID4, timestamp+aleatorio, IDs seguros criptográficamente) según la criticidad de la operación. Es esencial para mantener consistencia, trazabilidad y seguridad en los procesos internos de NORA.