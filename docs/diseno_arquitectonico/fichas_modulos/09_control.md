# Ficha Funcional – Módulo de Control

## Nombre del módulo:
`control/`

## Responsabilidad principal:
Supervisa y coordina el funcionamiento físico y operativo del sistema NORA. Se encarga de la inicialización del hardware, la monitorización del estado del sistema, el soporte a dispositivos auxiliares como expansores de I/O, y tareas administrativas como apagado controlado, reinicio, gestión energética y diagnóstico de fallos.

## Entradas esperadas:
- Tipo de entrada: comandos administrativos, estados de hardware, eventos de monitoreo
- Fuente: `gui/`, `sistema/`, sensores internos, eventos del sistema operativo
- Formato o protocolo: señales GPIO, datos de sensores, comandos de sistema, eventos estructurados

## Salidas generadas:
- Tipo de salida: señales de control de hardware, actualizaciones de estado, logs de operación
- Destinatario: `sistema/`, `gui/`, periféricos físicos (expansores, WiFi, RTC)
- Ejemplo de salida:
  - Activación/desactivación de expansores
  - Logs de diagnóstico
  - Alarmas de sobretemperatura

## Módulos relacionados:
- Entrada desde: `gui/`, `sistema/`
- Salida hacia: `sistema/`, `gui/`
- Comunicación bidireccional con: hardware físico, expansores de I/O, reloj RTC, WiFi externo

## Dependencias técnicas:
- Librerías externas: `RPi.GPIO`, `gpiozero`, `smbus2`, `psutil`, `os`, `subprocess`, `logging`
- Hardware gestionado: expansor I/O PCF8574, módulos WiFi, RTC DS3231
- Protocolos: GPIO, I2C, UART, llamadas a sistema operativo

## Notas adicionales:
El módulo `control/` centraliza todas las tareas de bajo nivel necesarias para mantener el sistema operativo estable, incluyendo la recuperación ante fallos, la supervisión de consumo de recursos, el diagnóstico preventivo y la gestión energética avanzada. Permite también el control remoto seguro mediante herramientas de administración en red.

## Archivos previstos del módulo:
Listado de archivos `.py` que se espera implementar dentro del directorio `control/` para estructurar sus funcionalidades.

- `control_main.py`: Coordinador general de supervisión y administración del sistema.
- `inicializacion_hardware.py`: Configuración de GPIOs, buses, sensores y periféricos al arranque.
- `supervision_estado.py`: Monitorización del estado físico: temperatura CPU, carga de RAM, conexión de red.
- `gestion_expansor_io.py`: Control del expansor de entradas/salidas PCF8574.
- `gestion_wifi_externo.py`: Configuración y control de módulo WiFi adicional (ESP8266 o similar).
- `gestion_energia.py`: Control de energía, perfiles de bajo consumo, apagados programados.
- `gestion_logs.py`: Registro estructurado y almacenamiento de logs de operación y eventos.
- `diagnostico_automatico.py`: Autotest de dispositivos físicos al arranque o bajo demanda.
- `control_remoto.py`: Soporte para administración remota (reinicios, apagados, diagnósticos vía web).
- `proteccion_fallos.py`: Gestión de watchdog interno y recuperación ante errores críticos.
- `sincronizacion_reloj.py`: Sincronización horaria mediante RTC DS3231 o NTP.
- `mantenimiento_predictivo.py`: Predicción temprana de fallos basada en patrones operativos.
- `perfiles_energia_dinamicos.py`: Gestión automática de modos de energía según condiciones del sistema.
- `gestion_desconexion_red.py`: Acciones de contingencia ante desconexión de red prolongada.
- `balanceo_carga.py`: Redistribución dinámica de tareas para optimizar uso de CPU y memoria.
- `gestion_alarmas_criticas.py`: Priorización y gestión avanzada de alarmas críticas del sistema.
- `config_control.py`: Configuración de parámetros de hardware, niveles de alerta y perfiles de energía.
- `utils_control.py`: Funciones auxiliares para acceso a hardware, control de GPIOs, lecturas de sensores de sistema.

