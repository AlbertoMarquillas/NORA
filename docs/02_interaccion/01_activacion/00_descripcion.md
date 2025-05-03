# Descripción – Interacción: Activación del Sistema

La interacción de activación define el conjunto de eventos que permiten a NORA transitar desde un estado pasivo (`STATE_IDLE`) hacia un estado activo o receptivo (`STATE_ACTIVE_WAIT` o superior). Este proceso representa el primer nivel de contacto entre el usuario y el sistema, y puede realizarse mediante estímulos físicos o perceptuales.

Se considera parte del mecanismo de activación toda señal que implique una intención clara del usuario de iniciar la interacción, sin necesidad de una orden explícita. Estos eventos desencadenan la puesta en marcha de módulos visuales, auditivos y lógicos que permiten a NORA prepararse para recibir comandos o establecer un vínculo de atención con el usuario.

## Tipos de activación implementados

- **Presencia física detectada** mediante sensores ultrasónicos (HC-SR04).
- **Reconocimiento de rostro o atención visual** mediante la cámara.
- **Lectura de tarjeta o identificador NFC** (PN532).
- **Hotword detectada por el módulo de voz** (“oye NORA”).
- **Interacción manual** mediante pulsador físico conectado a GPIO.

## Objetivos de la fase de activación

- Garantizar que la interacción posterior ocurre en un estado receptivo.
- Permitir modos de activación accesibles tanto para humanos como para interfaces externas (ej. vía Bluetooth).
- Registrar el evento de activación con su fuente y contexto.

## Módulos implicados

- `activacion/`  
- `sensores/` (lectura de eventos físicos)
- `voz/` (detección de hotword)
- `vision/` (detección de rostro)
- `agentes/` (validación y modulación de respuesta)
- `sistema/` (transición de estado FSM)

---