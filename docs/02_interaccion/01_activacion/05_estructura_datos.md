# Estructura de Datos – Gestión de Información Personal

Este documento describe el diseño lógico de los datos gestionados por NORA en lo referente a notas, rutinas, agenda y hábitos del usuario. Cada categoría está estructurada para permitir eficiencia de acceso, trazabilidad, control de versiones, y extensibilidad futura.

---

## 1. Categorías de información

### a. Notas rápidas

* Texto libre generado por el usuario.
* Asociadas a una marca de tiempo.
* Opcionalmente categorizadas por tema.

**Ejemplo JSON:**

```json
{
  "timestamp": "2025-05-03T16:25:00",
  "contenido": "Comprar pilas para el mando",
  "categoria": "compras"
}
```

---

### b. Agenda (eventos programados)

* Eventos fechados o recurrentes.
* Incluyen título, descripción y hora.

**Ejemplo JSON:**

```json
{
  "fecha": "2025-05-04",
  "hora": "17:00",
  "evento": "Reunión con tutor",
  "descripcion": "Enviar informe antes"
}
```

---

### c. Rutinas y hábitos

* Actividades repetidas (ej. beber agua, meditar).
* Con estado (pendiente, cumplido).
* Pueden incluir estadísticas: frecuencia, días cumplidos, historial.

**Ejemplo JSON:**

```json
{
  "habito": "Beber agua",
  "frecuencia": "diaria",
  "estado_actual": "cumplido",
  "historial": ["2025-05-01", "2025-05-02", "2025-05-03"]
}
```

---

## 2. Organización en el sistema de archivos

* Carpeta base: `datos/usuario/`

  * `notas/` → archivos individuales o lista consolidada por día.
  * `agenda/` → una entrada por evento o base de datos SQLite.
  * `rutinas/` → un JSON por hábito o archivo general consolidado.

**Ejemplo de estructura:**

```
datos/
└── usuario/
    ├── notas/
    │   └── 2025-05-03_notas.json
    ├── agenda/
    │   └── 2025-05.json
    └── rutinas/
        └── habitos.json
```

---

## 3. Persistencia y actualización

* Las escrituras son atómicas (backup antes de sobrescribir).
* Se guarda el historial completo de hábitos si está habilitado.
* Las notas pueden editarse, duplicarse o eliminarse por comando.
* Toda modificación es trazable y revocable si se activa control de versiones (futuro).

---

## 4. Relación con funcionalidades del sistema

* **Entrada:** por voz, GUI escrita, eventos programados.
* **Procesamiento:** a través de `dialogo/`, `agentes/`, `datos/`.
* **Salida:** voz, pantalla, notificación o consulta por texto.

---

Esta estructura modular permite mantener los datos organizados, consultables y listos para futuras sincronizaciones locales o replicación segura.
