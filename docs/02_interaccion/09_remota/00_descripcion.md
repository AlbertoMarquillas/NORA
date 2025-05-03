# Descripción – Interacción Remota por Aplicación o Interfaz Externa

Este documento define las capacidades y objetivos de la interacción remota entre el usuario y NORA, a través de canales como aplicaciones móviles, interfaces web o sistemas conectados en red. Esta modalidad permite controlar o consultar el sistema sin necesidad de presencia física directa.

---

## 1. Objetivo

Permitir que un usuario autorizado interactúe con NORA a distancia, mediante el envío de comandos, consultas o configuraciones desde una interfaz remota conectada por red local o internet, preservando seguridad y sincronización con el estado actual del sistema.

---

## 2. Casos de uso previstos

* Enviar una nota o recordatorio desde el móvil
* Consultar el estado o agenda del día en tiempo real
* Activar un modo específico (descanso, reunión, noche)
* Recibir alertas o eventos relevantes (temperatura alta, error interno)

---

## 3. Tipos de interfaces remotas

| Tipo de cliente  | Medio               | Requiere autenticación | Capacidad       |
| ---------------- | ------------------- | ---------------------- | --------------- |
| Aplicación móvil | App Android/iOS     | Sí                     | Completa        |
| Web local        | Interfaz web en LAN | Opcional               | Media           |
| Web externa      | Portal online       | Sí                     | Limitada/segura |
| Cliente MQTT     | Sistema embebido    | Sí                     | Automatización  |

---

## 4. Integración con el sistema

* `api/remoto.py`: gestión de peticiones entrantes (REST o WebSocket)
* `dialogo/interpretador.py`: reutilización del motor de intenciones
* `agentes/remoto.py`: validación, control de acceso, seguridad
* `datos/`, `accionadores/`, `monitor/`: módulos ejecutores

---

## 5. Consideraciones generales

* Toda interacción remota debe generar eventos equivalentes a los locales (`EVT_REMOTE_...`)
* El sistema debe mantener coherencia de estado entre sesión local y remota
* Las respuestas deben enviarse en el formato adecuado (JSON, texto plano, notificación push)

---

La interacción remota amplía la utilidad y el alcance de NORA, permitiendo que el usuario mantenga control y acceso contextual incluso cuando se encuentra fuera del entorno físico inmediato del asistente.
