# Prevención de Errores y Condiciones de Seguridad en el Protocolo NFC de NORA

## 1. Objetivo

Establecer las medidas técnicas y operativas necesarias para prevenir errores, garantizar la seguridad del flujo de activación/desactivación y evitar estados indeterminados en el sistema.

## 2. Tipos de Errores Previstos

* Lectura incorrecta de UID
* Reintentos consecutivos no deseados (rebote)
* UID no registrado
* Lectura simultánea por múltiples módulos
* Error en acceso a base de datos
* Fallo en respuesta multimodal

## 3. Mecanismos de Prevención

### 3.1. Validación Estructurada del UID

* Uso de patrón hexadecimal estricto (ej. `0xXXXXXXXX`)
* Longitud controlada por firmware
* Validación contra base de datos interna (`datos/`)

### 3.2. Ignorar UID no registrados

* Emisión de `EVT_NFC_UID_INVALID`
* Respuesta visual: LED amarillo intermitente
* Respuesta auditiva: "UID no reconocido"

### 3.3. Protección contra activaciones simultáneas

* Mutex o semáforo software dentro de `activacion/`
* Ventana de bloqueo temporal (ej. 2 segundos) tras cada lectura
* Estado `STATE_LOCKED` opcional si se requiere bloquear el protocolo

### 3.4. Tolerancia a Fallos en la Base de Datos

* Fallback automático: UID inválido en caso de fallo
* Logging de error en `datos/`
* No bloquear FSM global en caso de error local

### 3.5. Gestión de Fallos Multimodales

* Si `voz/` falla → mantener salida visual
* Si `interfaz/` falla → salida auditiva + log
* Emisión de evento `EVT_OUTPUT_ERROR` para diagnóstico

## 4. Recomendaciones de Implementación

* No usar lectura NFC como única fuente de activación crítica
* Implementar modo de depuración supervisado desde `gui/`
* Pruebas periódicas de validación de UID y respuestas (desde `tests/`)

## 5. Eventos de Control

* `EVT_NFC_UID_INVALID`
* `EVT_OUTPUT_ERROR`
* `EVT_ACCESS_DENIED`
* `EVT_TIMEOUT_NFC`

## 6. Diagramas Relacionados

* Secciones "Errores previstos" y "Fallbacks" en `protocolo_nfc.drawio`
