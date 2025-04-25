# Ficha Funcional – `servidor_web_gui.py`

## Nombre del archivo:
`servidor_web_gui.py`

## Responsabilidad principal:
Exponer la interfaz gráfica de usuario de NORA a través de un servidor web local o remoto, permitiendo el control y monitoreo del sistema desde navegadores compatibles. Facilita la administración remota y la supervisión distribuida.

## Entradas esperadas:
- **Tipo de entrada:** Solicitudes HTTP/S de navegadores, comandos enviados vía API.
- **Fuente:** Navegador web del usuario.
- **Formato o protocolo:** HTTP, WebSocket opcional.

## Salidas generadas:
- **Tipo de salida:** Páginas web generadas dinámicamente, respuestas a solicitudes, actualizaciones de estado.
- **Destinatario:** Cliente web (navegador).
- **Ejemplo de salida:**
  - Panel de control accesible vía IP local
  - Respuesta JSON con estado de sensores

## Módulos relacionados:
- **Entrada desde:** Navegador web.
- **Salida hacia:** Cliente web, `gui_main.py`.
- **Comunicación bidireccional con:** `gui_main.py` y subpaneles para reflejar cambios.

## Dependencias técnicas:
- **Librerías externas:** `flask`, `dash`, `streamlit`, `socket`, `json`, `threading`.
- **Hardware gestionado:** Ninguno directamente.
- **Protocolos:** HTTP, WebSocket.

## Notas adicionales:
`servidor_web_gui.py` debe asegurar una implementación ligera, segura y eficiente para exponer la GUI. Se recomienda implementar autenticación básica, cifrado opcional (TLS/SSL) y control de acceso para evitar intrusiones. Debe ser capaz de sincronizarse en tiempo real con el estado interno del sistema y ofrecer una experiencia de usuario fluida desde navegadores modernos.

