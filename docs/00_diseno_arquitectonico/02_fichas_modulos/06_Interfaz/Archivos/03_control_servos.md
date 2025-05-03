# Ficha Funcional – `control_servos.py`

## Nombre del archivo:
`control_servos.py`

## Responsabilidad principal:
Gestionar los movimientos físicos de NORA a través de servomotores, permitiendo gesticulaciones como mover la cabeza, inclinarla o realizar otros movimientos físicos asociados con las expresiones visuales y emocionales del sistema. Este archivo traduce las decisiones del sistema en movimientos físicos concretos.

## Entradas esperadas:
- **Tipo de entrada:** Comandos de movimiento, eventos emocionales, instrucciones de atención física.
- **Fuente:** `sistema/`, `agentes/`, `interfaz/`, `voz/` (para recibir eventos relacionados con movimientos físicos y modulación emocional).
- **Formato o protocolo:** Eventos internos (`CMD_MOVE_HEAD`, `CMD_ADJUST_POSE`), parámetros PWM para controlar el movimiento de los servos.

## Salidas generadas:
- **Tipo de salida:** Activación de servomotores, movimientos físicos específicos (por ejemplo, mover la cabeza hacia el usuario, inclinación).
- **Destinatario:** Hardware físico (servomotores SG90/MG90).
- **Ejemplo de salida:**
  - `CMD_MOVE_HEAD` (Instrucción para mover los servomotores y orientar la cabeza de NORA hacia el usuario).
  - `CMD_TILT_HEAD` (Instrucción para inclinar la cabeza en función del contexto o de la emoción detectada).
  - `AGT_HEAD_MOVEMENT_COMPLETED` (Evento que confirma que el movimiento físico se ha completado correctamente).

## Módulos relacionados:
- **Entrada desde:** `sistema/`, `agentes/`, `interfaz/`, `voz/` (para recibir instrucciones sobre los movimientos físicos según el estado emocional y las interacciones del usuario).
- **Salida hacia:** Hardware físico (servomotores SG90/MG90).
- **Comunicación bidireccional con:** `interfaz/` (para coordinar los movimientos físicos con las expresiones visuales y emocionales).

## Dependencias técnicas:
- **Librerías externas:** `RPi.GPIO`, `pigpio`, `gpiozero` (para controlar los servomotores mediante los pines GPIO de la Raspberry Pi).
- **Hardware gestionado:** Servomotores SG90/MG90 para los movimientos físicos.
- **Protocolos:** PWM, eventos internos para controlar los servos y garantizar movimientos precisos.

## Notas adicionales:
Este archivo es fundamental para dar vida a NORA a través de movimientos físicos, haciendo que el sistema no solo sea visualmente expresivo, sino también capaz de realizar gestos físicos que refuercen su comunicación con el usuario. Los servomotores permiten que NORA pueda interactuar de una manera más natural, reaccionando a las emociones y eventos con movimientos que complementan las expresiones faciales y las respuestas vocales.

## Archivos previstos del módulo:
- `control_servos.py`: Movimiento de servomotores para gesticulaciones físicas (este archivo).
- Archivos adicionales como `interfaz_main.py`, `pantalla_facial.py`, `leds_rgb.py`.
