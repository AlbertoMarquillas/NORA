# Ficha Funcional – `sincronizacion_reloj.py`

## Nombre del archivo:
`sincronizacion_reloj.py`

## Responsabilidad principal:
Gestionar la sincronización horaria del sistema NORA utilizando un RTC externo (DS3231) o, en su defecto, servicios NTP. Garantiza la consistencia temporal de los registros, eventos y operaciones cronometradas del sistema, tanto en modo online como offline.

## Entradas esperadas:
- **Tipo de entrada:** Solicitudes de actualización horaria, verificación de coherencia temporal, eventos de arranque.
- **Fuente:** `control_main.py`, `sistema/`, eventos de inicio del sistema.
- **Formato o protocolo:** Llamadas de función, comunicación I2C, sincronización NTP (protocolo de red).

## Salidas generadas:
- **Tipo de salida:** Actualización de la hora del sistema, logs de sincronización, alarmas de error de reloj.
- **Destinatario:** `control_main.py`, `sistema/`, `gui/`.
- **Ejemplo de salida:**
  - `EVT_CLOCK_SYNC_SUCCESS`
  - `EVT_CLOCK_SYNC_FAILURE`

## Módulos relacionados:
- **Entrada desde:** `control_main.py`, `sistema/`.
- **Salida hacia:** `control_main.py`, `sistema/`, `gui/`.
- **Comunicación bidireccional con:** RTC DS3231 (vía I2C), servicio NTP.

## Dependencias técnicas:
- **Librerías externas:** `smbus2`, `ntplib`, `datetime`, `os`, `logging`.
- **Hardware gestionado:** Reloj de Tiempo Real (RTC) DS3231.
- **Protocolos:** I2C, NTP (red).

## Notas adicionales:
`sincronizacion_reloj.py` debe priorizar el uso del RTC externo para garantizar la independencia del sistema respecto a la conectividad de red. Solo en ausencia de un RTC operativo deberá intentar sincronizar vía NTP. Toda actualización de hora debe ser registrada adecuadamente para auditoría de eventos y consistencia de logs.

