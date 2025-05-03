# Ficha Funcional – `gestion_perfiles.py`

## Nombre del archivo:
`gestion_perfiles.py`

## Responsabilidad principal:
Gestionar los perfiles de usuario dentro de NORA, incluyendo la creación, modificación y recuperación de configuraciones personalizadas como preferencias lingüísticas, nivel de formalidad, tono de voz, y otros ajustes personalizados que afectan la interacción. Este archivo permite a NORA adaptarse a diferentes usuarios y proporcionar una experiencia personalizada basada en sus preferencias y características.

## Entradas esperadas:
- **Tipo de entrada:** Datos de perfil de usuario, configuraciones de preferencias, solicitudes de actualización de perfil.
- **Fuente:** `dialogo/` (para recibir datos sobre el perfil del usuario y sus preferencias), `sistema/` (para gestionar el perfil de configuración global).
- **Formato o protocolo:** Datos del perfil en formato JSON, eventos internos de actualización de perfil.

## Salidas generadas:
- **Tipo de salida:** Confirmación de perfil actualizado, datos de perfil recuperados, eventos de personalización de interacción.
- **Destinatario:** `dialogo/`, `voz/`, `sistema/` (para aplicar los ajustes del perfil en la interacción y el flujo del sistema).
- **Ejemplo de salida:**
  - `EVT_PROFILE_UPDATED` (Evento que indica que el perfil del usuario ha sido actualizado correctamente).
  - `CMD_APPLY_PROFILE_SETTINGS` (Instrucción para aplicar los ajustes del perfil de usuario en el sistema).
  - `AGT_PROFILE_RETRIEVED` (Confirmación de que los datos del perfil han sido recuperados correctamente).

## Módulos relacionados:
- **Entrada desde:** `dialogo/` (para recibir las preferencias y ajustes del perfil del usuario), `sistema/` (para obtener configuraciones globales y aplicarlas al perfil del usuario).
- **Salida hacia:** `dialogo/`, `voz/`, `sistema/` (para aplicar los ajustes del perfil en el diálogo y las interacciones del sistema).
- **Comunicación bidireccional con:** `agentes/`, `sistema/` para asegurar que el perfil de usuario esté alineado con el contexto y las interacciones del sistema.

## Dependencias técnicas:
- **Librerías externas:** `json` (para el almacenamiento y recuperación del perfil de usuario), `sqlite3`, `SQLAlchemy` (para persistencia de datos en bases de datos locales).
- **Hardware gestionado:** Almacenamiento local (SSD/HDD) para persistencia de perfiles y configuraciones.
- **Protocolos:** SQL, JSON para almacenar y recuperar datos del perfil del usuario.

## Notas adicionales:
Este archivo es esencial para permitir que NORA interactúe de manera personalizada con cada usuario. La capacidad de almacenar y ajustar las configuraciones del perfil asegura que NORA pueda adaptarse a los gustos y necesidades del usuario, ya sea ajustando el tono de voz, la formalidad o la forma de interactuar. Gracias a **`gestion_perfiles.py`**, NORA puede ofrecer una experiencia más humana y personalizada, adaptándose a lo largo del tiempo según las preferencias del usuario.

## Archivos previstos del módulo:
- `gestion_perfiles.py`: Gestión de perfiles de usuario y configuraciones personalizadas (este archivo).
- Archivos adicionales como `datos_main.py`, `dialogo_main.py`, `config_dialogo.py`.
