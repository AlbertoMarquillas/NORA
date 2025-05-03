# Flujos – Interacción: Activación del Sistema

Este apartado describe los flujos lógicos que conectan los estímulos externos con la transición interna de estado en el sistema NORA. Cada flujo representa una cadena de eventos desde la percepción hasta la activación efectiva del sistema.

## 1. Diagrama general del flujo de activación

```plaintext
[Sensor o entrada activa] → [Módulo perceptivo (voz/visión/sensores)]
                        → [Evaluación por agentes]
                        → [Generación de EVT_ACTIVATION_XXX]
                        → [sistema/] → Cambio a STATE_ACTIVE_WAIT
```

## 2. Flujos específicos por tipo de entrada

### a. Hotword detectada

```plaintext
[Micrófono] → [voz/] detecta “oye NORA” → [agentes/] validan contexto →
EVT_ACTIVATION_VOICE_CONFIRMED → [sistema/] entra en modo atención
```

### b. Rostro detectado visualmente

```plaintext
[Cámara] → [vision/] detecta rostro + atención → [agentes/] validan mantenimiento →
EVT_ACTIVATION_VISUAL_CONFIRMED → [sistema/] transiciona de IDLE a ACTIVE_WAIT
```

### c. Sensor ultrasónico (presencia física)

```plaintext
[HC-SR04] → [sensores/] mide distancia < umbral → [activacion/] temporiza permanencia →
EVT_ACTIVATION_PRESENCE_CONFIRMED → [sistema/] inicia recepción de entrada
```

### d. Tarjeta NFC

```plaintext
[NFC PN532] → [sensores/] detecta UID válido → [activacion/] valida identidad →
EVT_ACTIVATION_NFC_CONFIRMED → [sistema/] inicia atención personalizada (si aplica)
```

### e. Botón físico

```plaintext
[GPIO] → [activacion/] detecta presión mantenida →
EVT_ACTIVATION_BUTTON_CONFIRMED → [sistema/] activa LED + saludo
```

## 3. Consideraciones sobre FSM (máquina de estados)

* Solo se admiten eventos de activación cuando el sistema está en `STATE_IDLE`.
* La transición tras evento confirmado lleva a `STATE_ACTIVE_WAIT`, en espera de entrada verbal o escrita.
* Si no se recibe entrada posterior en un tiempo límite, se retorna a `STATE_IDLE`.
* Eventos repetidos dentro del mismo ciclo son ignorados salvo que provengan de una fuente distinta.
