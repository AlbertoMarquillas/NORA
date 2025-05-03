# Especificación Técnica General del Protocolo NFC para NORA

## 1. Introducción

Este documento especifica el protocolo general de control mediante NFC para la activación y desactivación consciente del asistente físico inteligente NORA. Describe claramente los procedimientos y requisitos desde la detección de una etiqueta NFC válida hasta la transición del estado completo del sistema.

## 2. Componentes Hardware

### 2.1. Módulo NFC PN532

* Comunicación soportada: I²C/UART/SPI
* Referencia técnica: Datasheet PN532

### 2.2. Raspberry Pi 4 Model B

* Plataforma base, gestión del protocolo mediante GPIO y librerías Python.

## 3. Estados Principales

* **Reposo:** Sistema en bajo consumo y en espera.
* **Activado:** Sistema completamente operativo y listo para interacción.

## 4. Flujo del Protocolo NFC

### 4.1. Flujo de Activación con UID válido

* **Estado inicial:** Reposo
* **Evento:** Detección NFC
* **Condición:** UID registrado y válido
* **Acciones:**

  1. Validación del UID mediante `sensores/`.
  2. Evento interno `EVT_NFC_UID_VALID`.
  3. Cambio de estado (`activacion/` → `sistema/`).
  4. Activación progresiva de módulos periféricos:

     * Ambientales (`sensores/`)
     * Visual (`vision/`)
     * Auditivo (`voz/`)
     * Expresividad (`interfaz/`)
  5. Respuesta multimodal:

     * LED verde (activado)
     * Audio: "Sistema activado"

### 4.2. Flujo de Desactivación con UID previo (Toggle)

* **Estado inicial:** Activado/Escucha
* **Evento:** Nueva detección NFC del mismo UID
* **Condición:** UID previamente activado
* **Acciones:**

  1. Validación del UID activo mediante `sensores/`.
  2. Evento interno `EVT_NFC_UID_TOGGLE`.
  3. Inicio apagado progresivo (`activacion/` → `sistema/`).
  4. Desactivación secuencial de módulos:

     * Auditivo (`voz/`)
     * Visual (`vision/`)
     * Ambientales (`sensores/`)
     * Expresividad (`interfaz/`)
  5. Respuesta multimodal:

     * LED rojo (desactivado)
     * Audio: "Sistema desactivado"

## 5. Condiciones de Seguridad

* **Validación estricta de UID:** Sólo aceptan UIDs previamente registrados en base de datos (`datos/`).
* **Tarjetas no registradas:** Ignoradas con alerta visual (LED amarillo intermitente) y mensaje auditivo ("UID no reconocido").
* **Bloqueo temporal:** Evita múltiples activaciones simultáneas mediante bloqueo mínimo de 2 segundos tras cada lectura NFC.

## 6. Diagramas

Referencia al archivo adjunto: `protocolo_nfc.drawio`

* **Tipo:** Diagrama de flujo
* **Detalle:** Pasos específicos de activación y desactivación
* **Leyenda:** Incluye símbolos para eventos, decisiones y acciones claramente definidos.
