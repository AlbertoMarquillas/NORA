# Comandos Soportados – Interacción Verbal

Este documento recoge los comandos de voz que NORA reconoce en la versión inicial del sistema. Cada entrada incluye el patrón general, su intención asociada y el módulo encargado de su ejecución. Se organizan por categorías funcionales.

---

## 1. Consultas informativas

| Ejemplo de entrada         | Intención asociada         | Módulo principal |
| -------------------------- | -------------------------- | ---------------- |
| ¿Qué hora es?              | `consultar_hora()`         | `sistema/`       |
| ¿Qué día es hoy?           | `consultar_fecha()`        | `sistema/`       |
| ¿Tengo algo que hacer hoy? | `consultar_agenda(hoy)`    | `datos/`         |
| ¿Qué tengo mañana?         | `consultar_agenda(mañana)` | `datos/`         |

---

## 2. Comandos de acción

| Ejemplo de entrada           | Intención asociada    | Módulo principal |
| ---------------------------- | --------------------- | ---------------- |
| Enciende la luz              | `encender_luz()`      | `accionadores/`  |
| Apaga el ventilador          | `apagar_ventilador()` | `accionadores/`  |
| Muestra la previsión del día | `mostrar_prevision()` | `interfaz/`      |

---

## 3. Gestión personal

| Ejemplo de entrada                 | Intención asociada                 | Módulo principal |
| ---------------------------------- | ---------------------------------- | ---------------- |
| Recuérdame beber agua              | `crear_recordatorio("beber agua")` | `datos/`         |
| Apunta que he tomado la medicación | `registrar_evento("medicación")`   | `datos/`         |
| ¿Qué notas tengo?                  | `consultar_notas()`                | `datos/`         |
| Borra la nota de comprar pilas     | `eliminar_nota("comprar pilas")`   | `datos/`         |

---

## 4. Diálogo social y expresivo

| Ejemplo de entrada | Intención asociada     | Módulo principal |
| ------------------ | ---------------------- | ---------------- |
| Hola NORA          | `saludo()`             | `expresion/`     |
| Me voy, adiós      | `despedida()`          | `expresion/`     |
| ¿Cómo estás?       | `estado_asistente()`   | `expresion/`     |
| Anímame un poco    | `expresion_positiva()` | `expresion/`     |

---

## 5. Observaciones técnicas

* Todos los comandos se definen mediante expresiones regulares o reglas de coincidencia flexible.
* La intención se normaliza antes de ser enviada al módulo de ejecución.
* Las respuestas están definidas en plantillas, con parámetros variables según el contexto.

Este repertorio inicial podrá ampliarse en fases posteriores con nuevos comandos, sin alterar la estructura del sistema.
