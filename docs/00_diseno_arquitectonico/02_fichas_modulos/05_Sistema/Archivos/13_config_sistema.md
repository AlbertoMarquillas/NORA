# Ficha Funcional – `config_sistema.py`

## Nombre del archivo:
`config_sistema.py`

## Responsabilidad principal:
Definir los parámetros globales y las configuraciones dinámicas del sistema NORA. Este archivo es responsable de gestionar la configuración del sistema, incluyendo los umbrales, tiempos de espera, y otros parámetros que afectan el comportamiento general del sistema, permitiendo ajustes sin modificar el código base.

## Entradas esperadas:
- **Tipo de entrada:** Archivos de configuración, datos de entrada del usuario o del sistema, cambios en las configuraciones globales.
- **Fuente:** Archivos de configuración (`config.json` o similares), configuraciones de usuario y parámetros definidos en otros módulos del sistema.
- **Formato o protocolo:** Configuraciones en formato JSON, eventos internos que indican cambios en las configuraciones globales (`EVT_CONFIG_UPDATED`).

## Salidas generadas:
- **Tipo de salida:** Actualización de configuraciones del sistema, parámetros globales, ajustes de umbrales y tiempos.
- **Destinatario:** `sistema/`, `agentes/`, `interfaz/` (para aplicar las configuraciones al sistema y a los módulos relevantes).
- **Ejemplo de salida:**
  - `EVT_CONFIG_UPDATED` (Evento que indica que las configuraciones del sistema han sido actualizadas).
  - `CMD_UPDATE_CONFIGURATION` (Instrucción para aplicar nuevas configuraciones al sistema).
  - `AGT_CONFIGURATION_ADJUSTED` (Confirmación de que la configuración del sistema ha sido ajustada correctamente).

## Módulos relacionados:
- **Entrada desde:** Archivos de configuración (`config.json`), módulos que requieren configuraciones globales (`sistema/`, `agentes/`).
- **Salida hacia:** `sistema/`, `agentes/`, `interfaz/` (para aplicar la configuración global a los módulos correspondientes).
- **Comunicación bidireccional con:** `sistema/`, `agentes/`, `interfaz/` para asegurar que las configuraciones sean correctamente distribuidas y aplicadas.

## Dependencias técnicas:
- **Librerías externas:** `json` (para leer y escribir archivos de configuración), `os` (para manejar configuraciones relacionadas con el entorno).
- **Hardware gestionado:** Ninguno directamente (gestiona configuraciones a nivel lógico).
- **Protocolos:** Comunicación basada en eventos internos, carga y aplicación de configuraciones dinámicas.

## Notas adicionales:
Este archivo es crucial para centralizar la configuración del sistema NORA. Permite modificar parámetros del sistema sin necesidad de realizar cambios en el código base. Además, al proporcionar un sistema centralizado de configuración, `config_sistema.py` facilita la personalización del sistema según las necesidades del usuario o los cambios en las condiciones externas, sin comprometer la integridad del sistema.

## Archivos previstos del módulo:
- `config_sistema.py`: Definición de parámetros globales (tiempos, umbrales, configuraciones dinámicas) (este archivo).
- Archivos adicionales como `sistema_main.py`, `analisis_contextual.py`.
