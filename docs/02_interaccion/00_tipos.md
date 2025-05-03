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

## Tipos de Interacción Futura entre el Usuario y NORA

Este apéndice documenta interacciones previstas para futuras versiones del sistema NORA, ampliando las capacidades existentes e integrando nuevos canales sensoriales y de control.


---

### 7. Interacción escrita por interfaz gráfica

**Descripción:**
Forma de interacción basada en la introducción escrita de comandos, preguntas o contenido por parte del usuario, a través de una interfaz gráfica desarrollada en Python (web o escritorio). Permite replicar las funcionalidades disponibles por voz de forma accesible y precisa.

**Ejemplos previstos:**

* Escribir "Recuérdame la cita con el médico" en un campo de texto
* Añadir una nota mediante formulario
* Consultar el historial de rutinas o emociones

**Entradas involucradas:** Campo de texto en GUI, interfaz web o escritorio
**Salidas asociadas:** Respuestas textuales o visuales, actualizaciones en la base de datos, ejecución de comandos equivalentes a los verbales

---

Estas interacciones —algunas ya implementadas, otras previstas— complementan el marco actual de operación, permitiendo una experiencia más rica, flexible y adaptada a diferentes contextos de uso.

### 8. Interacción táctil directa *(implementación futura)*

**Descripción:**
Interacciones basadas en el contacto físico o manipulaciones directas sobre superficies sensibles al tacto, como una pantalla capacitiva o sensores capacitivos integrados en la carcasa.

**Ejemplos previstos:**

* Pulsación en una pantalla táctil para confirmar o cancelar
* Deslizamiento sobre una superficie capacitiva para navegar
* Toque prolongado como señal de pausa o emergencia

**Entradas involucradas:** Pantalla táctil, sensores capacitivos GPIO/I²C
**Salidas asociadas:** Retroalimentación visual o sonora, cambios de estado, comandos internos

---

### 9. Interacción remota por aplicación o interfaz externa *(implementación futura)*

**Descripción:**
Comunicaciones iniciadas desde una aplicación móvil, interfaz web o sistema conectado en red, permitiendo al usuario interactuar con NORA sin presencia física directa.

**Ejemplos previstos:**

* Envío de una nota desde el móvil
* Consulta remota de la agenda
* Activación de un modo específico desde una app

**Entradas involucradas:** Interfaz web, sockets TCP/IP, mensajes MQTT o HTTP
**Salidas asociadas:** Comandos en el sistema, respuestas vía app, sincronización de estados

---

### 10. Interacción física avanzada *(implementación futura)*

**Descripción:**
Formas de interacción basadas en la detección de movimientos, inclinaciones o contacto físico estructural, mediante sensores inerciales o de presión.

**Ejemplos previstos:**

* NORA detecta que ha sido levantada o inclinada
* Reacción ante un golpe o vibración
* Activación al tocar su superficie con cierto patrón

**Entradas involucradas:** IMU (acelerómetro/giroscopio), sensores táctiles o de presión
**Salidas asociadas:** Expresión facial de sorpresa, voz, registro de evento físico

---

## Tipos de Interacción Futura entre el Usuario y NORA

### Tabla Resumen de Interacciones

| Nº | Tipo de Interacción                          | Estado de implementación |
| -- | -------------------------------------------- | ------------------------ |
| 1  | Activación del sistema                       | Implementada             |
| 2  | Interacción verbal                           | Implementada             |
| 3  | Interacción visual directa                   | Implementada             |
| 4  | Interacción contextual o ambiental           | Implementada             |
| 5  | Gestión de información personal              | Implementada             |
| 6  | Reacciones autónomas del sistema             | Implementada             |
| 7  | Interacción escrita por interfaz gráfica     | Implementada             |
| 8  | Interacción táctil directa                   | Futura                   |
| 9  | Interacción remota por aplicación o interfaz | Futura                   |
| 10 | Interacción física avanzada                  | Futura                   |

Este apéndice documenta interacciones previstas para futuras versiones del sistema NORA, ampliando las capacidades existentes e integrando nuevos canales sensoriales y de control.

Estas interacciones —algunas ya implementadas, otras previstas— complementan el marco actual de operación, permitiendo una experiencia más rica, flexible y adaptada a diferentes contextos de uso.

```bash
docs_interacciones/
├── 01_activacion/
│   ├── descripcion.md
│   ├── flujos.md
│   ├── sensores_y_eventos.md
│   └── ejemplos_visuales.md
│
├── 02_verbal/
│   ├── descripcion.md
│   ├── flujo_dialogo.md
│   ├── comandos_soportados.md
│   └── integracion_voz.md
│
├── 03_visual/
│   ├── descripcion.md
│   ├── procesamiento_visual.md
│   ├── orientacion_fisica.md
│   └── pruebas_camara.md
│
├── 04_contexto/
│   ├── descripcion.md
│   ├── sensores_ambientales.md
│   ├── condiciones_disparo.md
│   └── respuestas_contextuales.md
│
├── 05_info_personal/
│   ├── descripcion.md
│   ├── estructura_datos.md
│   ├── ejemplo_uso.md
│   └── privacidad.md
│
├── 06_autonomas/
│   ├── descripcion.md
│   ├── temporizadores.md
│   ├── estado_sistema.md
│   └── gestion_fallos.md
│
├── 07_escrita_gui/
│   ├── descripcion.md
│   ├── diseño_interfaz.md
│   ├── flujo_texto_comando.md
│   └── equivalencias_voz.md
│
├── 08_tactil/
│   ├── descripcion.md
│   ├── hardware_tacto.md
│   ├── patrones_interaccion.md
│   └── ideas_expresion.md
│
├── 09_remota/
│   ├── descripcion.md
│   ├── protocolos.md
│   ├── control_remoto.md
│   └── seguridad_conexion.md
│
└── 10_fisica/
    ├── descripcion.md
    ├── sensores_imu.md
    ├── respuestas_fisicas.md
    └── pruebas_contacto.md
```

de operación, permitiendo una experiencia más rica, flexible y adaptada a diferentes contextos de uso.
