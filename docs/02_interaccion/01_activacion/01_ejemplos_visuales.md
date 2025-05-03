# Descripción – Interacción: Activación del Sistema

La interacción de activación define el conjunto de eventos que permiten a NORA transitar desde un estado pasivo (`STATE_IDLE`) hacia un estado activo o receptivo (`STATE_ACTIVE_WAIT` o superior). Este proceso representa el primer nivel de contacto entre el usuario y el sistema, y puede realizarse mediante estímulos físicos o perceptuales.

Se considera parte del mecanismo de activación toda señal que implique una intención clara del usuario de iniciar la interacción, sin necesidad de una orden explícita. Estos eventos desencadenan la puesta en marcha de módulos visuales, auditivos y lógicos que permiten a NORA prepararse para recibir comandos o establecer un vínculo de atención con el usuario.

## Tipos de activación implementados

* **Presencia física detectada** mediante sensores ultrasónicos (HC-SR04).
* **Reconocimiento de rostro o atención visual** mediante la cámara.
* **Lectura de tarjeta o identificador NFC** (PN532).
* **Hotword detectada por el módulo de voz** (“oye NORA”).
* **Interacción manual** mediante pulsador físico conectado a GPIO.

## Objetivos de la fase de activación

* Garantizar que la interacción posterior ocurre en un estado receptivo.
* Permitir modos de activación accesibles tanto para humanos como para interfaces externas (ej. vía Bluetooth).
* Registrar el evento de activación con su fuente y contexto.

## Módulos implicados

* `activacion/`
* `sensores/` (lectura de eventos físicos)
* `voz/` (detección de hotword)
* `vision/` (detección de rostro)
* `agentes/` (validación y modulación de respuesta)
* `sistema/` (transición de estado FSM)

---

# Ejemplos Visuales – Interacción: Activación del Sistema

Este documento recoge representaciones gráficas y esquemas que ilustran los diferentes métodos de activación del sistema NORA. Estos ejemplos ayudan a comprender el flujo físico y perceptivo que inicia la transición desde un estado inactivo a un estado operativo.

---

## 1. Activación por Presencia Física (HC-SR04)

**Esquema de detección:**

* Sensor ultrasónico detecta un objeto a menos de 100 cm.
* Si se mantiene la presencia durante más de 3 segundos, se genera `EVT_ACTIVATION_PRESENCE_CONFIRMED`.

```plaintext
[Usuario delante] → [HC-SR04 detecta distancia < 100 cm] → [Temporizador activo] → [Activación confirmada]
```

**Indicadores físicos:**

* Encendido progresivo de LEDs indicadores.
* Giro de servos hacia el usuario si está disponible.

---

## 2. Activación por Rostro Detectado

**Flujo visual:**

* Cámara detecta una forma facial frontal.
* El agente visual valida si hay contacto visual mantenido.
* Generación de `EVT_ACTIVATION_VISUAL_CONFIRMED`.

**Ejemplo gráfico sugerido:**
(Fotografía o render frontal con superposición del marco de detección de rostro)

---

## 3. Activación por Hotword

**Secuencia lógica:**

* Motor de voz detecta la frase “oye NORA”.
* Si el sistema se encuentra en `STATE_IDLE`, emite `EVT_ACTIVATION_VOICE_CONFIRMED`.

```plaintext
[Entrada de micrófono] → [Reconocimiento de hotword] → [Verificación de estado] → [Cambio de estado a ACTIVE_WAIT]
```

---

## 4. Activación por Tarjeta NFC

**Diagrama de eventos:**

* El módulo PN532 detecta una tarjeta válida.
* Se genera `EVT_ACTIVATION_NFC_CONFIRMED` con `ID_TAG`.

**Representación sugerida:**

* Fotografía del gesto de acercamiento con tarjeta.
* Pantalla con saludo personalizado (si ID está registrado).

---

## 5. Activación por Botón Físico (GPIO)

**Escenario habitual:**

* Usuario presiona el botón durante al menos 1 segundo.
* Evento `EVT_ACTIVATION_BUTTON_CONFIRMED` se lanza.

**Indicadores visuales:**

* Parpadeo corto en LEDs de estado.
* Mensaje breve en pantalla (si habilitada).

---

## Recomendaciones de Implementación Visual

* Incluir estos diagramas en presentaciones, manuales técnicos y sesiones de validación.
* Usar íconos consistentes (presencia, rostro, voz, NFC, botón).
* Mantener consistencia visual con el diseño general de NORA (`interfaz/`).
