# Tipos de Interacción entre el Usuario y NORA

Este documento define las categorías funcionales de interacción entre el usuario y el sistema NORA. Cada tipo describe un patrón general de entrada, procesamiento y respuesta, sirviendo como base para la documentación de flujos específicos.

---

## 1. Activación del sistema

**Descripción:**
Conjunto de eventos que permiten transitar a NORA desde un estado pasivo (`STATE_IDLE`) a un estado operativo (`STATE_ACTIVE_WAIT` o superior).

**Ejemplos típicos:**

* Detección de tarjeta NFC válida
* Detección de presencia visual prolongada
* Activación por hotword (“oye NORA”)
* Pulsación de botón físico

**Entradas involucradas:** NFC, visión (presencia/rostro), voz (hotword), GPIO

**Salidas asociadas:** Encendido de LEDs, pantalla atenta, saludo por voz

---

## 2. Interacción verbal

**Descripción:**
Flujos en los que el usuario emite un comando o una pregunta por voz, y NORA responde con una acción y/o una respuesta hablada y expresiva.

**Ejemplos típicos:**

* “¿Qué hora es?”
* “Recuérdame beber agua”
* “Enciende la luz”

**Entradas involucradas:** Voz (ASR + parsing de comandos)

**Salidas asociadas:** Voz sintetizada (TTS), expresión facial, cambio de estado, ejecución de acción

---

## 3. Interacción visual directa

**Descripción:**
Comportamientos que se ajustan en tiempo real según la percepción visual del usuario: su posición, mirada, gestos o emociones.

**Ejemplos típicos:**

* El usuario se coloca delante → NORA gira o “mira”
* Contacto visual mantenido → entra en modo atención
* Usuario saluda con la mano → respuesta física

**Entradas involucradas:** Visión (rostro, atención, gestos, emociones)

**Salidas asociadas:** Movimiento físico, LEDs, pantalla, comandos al núcleo

---

## 4. Interacción contextual o ambiental

**Descripción:**
Respuestas ante condiciones del entorno físico (luz, temperatura, presencia, ruido) o estado interno del sistema.

**Ejemplos típicos:**

* Ambiente oscuro → expresión facial cambia
* Temperatura alta → mensaje de advertencia
* Error del sistema → expresión de fallo

**Entradas involucradas:** Sensores ambientales, monitoreo del sistema

**Salidas asociadas:** Luz de alerta, voz, expresión en pantalla, logs

---

## 5. Gestión de información personal

**Descripción:**
Interacciones que implican la creación, consulta o modificación de contenido asociado al usuario (notas, rutinas, agenda, hábitos).

**Ejemplos típicos:**

* “Guarda una nota”
* “¿Tengo algo que hacer hoy?”
* “Apunta que bebí agua”

**Entradas involucradas:** Voz (ASR), diálogo, activadores temporales o eventos

**Salidas asociadas:** Confirmación por voz, almacenamiento en base de datos, actualización de estado

---

## 6. Reacciones autónomas del sistema

**Descripción:**
Acciones iniciadas por NORA sin intervención directa del usuario, en base a condiciones internas, temporales o de contexto acumulado.

**Ejemplos típicos:**

* Ausencia prolongada → entrar en reposo
* Falta de respuesta → repetir pregunta
* Error crítico → reinicio parcial

**Entradas involucradas:** Temporizadores internos, estado del sistema, supervisión de agentes

**Salidas asociadas:** Transición de estado, mensajes automáticos, acciones de mantenimiento

---

Este marco permite clasificar de forma precisa cualquier flujo futuro y asegurar consistencia documental y arquitectónica.
