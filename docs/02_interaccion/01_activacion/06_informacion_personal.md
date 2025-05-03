# Ejemplo de Uso – Gestión de Información Personal

Este documento proporciona un ejemplo detallado de un flujo completo de interacción entre el usuario y NORA para la creación, consulta y modificación de información personal. Ilustra la coordinación entre módulos y la trazabilidad del proceso.

---

## 1. Escenario: Guardar una nota por voz

**Usuario:** “NORA, apunta que tengo que llamar a Laura”

**Flujo del sistema:**

1. `voz/` detecta la hotword y transcribe la orden.
2. `dialogo/` interpreta intención: `crear_nota(texto)`
3. `agentes/` validan el contexto de la acción.
4. `datos/` registra una nueva entrada en `notas/`
5. `voz/` responde: “He guardado la nota: llamar a Laura”

**Resultado:**

```json
{
  "timestamp": "2025-05-03T18:12:00",
  "contenido": "llamar a Laura"
}
```

---

## 2. Escenario: Consultar eventos del día

**Usuario:** “¿Tengo algo que hacer hoy?”

**Flujo del sistema:**

1. `voz/` transcribe la pregunta.
2. `dialogo/` interpreta: `consultar_agenda(fecha=hoy)`
3. `datos/` busca entradas en `agenda/`
4. Si hay eventos, `voz/` los lee en orden horario.

**Respuesta esperada:**

> “Hoy tienes una reunión con el tutor a las cinco.”

---

## 3. Escenario: Registrar hábito por GUI

**Usuario:** Escribe “He bebido agua” en la interfaz escrita.

**Flujo del sistema:**

1. `interfaz_escrita/` recibe texto.
2. `dialogo/` lo analiza como `actualizar_habito('Beber agua')`
3. `agentes/` validan si es coherente y no repetido.
4. `datos/` añade el día actual al historial del hábito.
5. `interfaz_escrita/` muestra confirmación.

**Resultado en JSON:**

```json
{
  "habito": "Beber agua",
  "historial": ["2025-05-01", "2025-05-02", "2025-05-03"]
}
```

---

## 4. Observaciones

* En todos los casos, las órdenes pueden darse por voz o texto.
* Los módulos `dialogo/` y `agentes/` centralizan la interpretación y control contextual.
* Toda acción que modifica datos puede estar sujeta a confirmación o revisión según el estado del sistema.

Este tipo de flujos representan la base para desarrollar pruebas unitarias, escenarios de validación e interfaces de interacción coherentes con la arquitectura funcional de NORA.
