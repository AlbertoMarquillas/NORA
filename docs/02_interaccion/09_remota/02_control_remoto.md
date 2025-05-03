# Control Remoto – Interacción desde Aplicaciones Externas

Este documento describe los mecanismos de control remoto sobre el sistema NORA, tanto para ejecutar comandos como para gestionar estados, eventos y configuraciones desde interfaces conectadas por red.

---

## 1. Objetivo

Permitir al usuario controlar funciones clave del asistente a distancia, con la misma capacidad que si interactuara presencialmente por voz o GUI local, manteniendo integridad de estado y trazabilidad.

---

## 2. Funcionalidades expuestas remotamente

| Función                    | Medio     | Endpoint/API                            |
| -------------------------- | --------- | --------------------------------------- |
| Crear nota                 | REST/MQTT | `POST /api/nota`                        |
| Consultar agenda           | REST      | `GET /api/agenda?fecha=...`             |
| Cambiar modo               | MQTT/REST | `nora/cmd/usuario_id` → `modo:descanso` |
| Activar comando específico | REST      | `POST /api/comando`                     |
| Enviar alerta              | MQTT      | `nora/alerta/manual`                    |

---

## 3. Relación con FSM

* Los comandos remotos pueden generar eventos internos (`EVT_REMOTE_*`) evaluados por la FSM
* El cambio de estado solo se permite si es coherente con el flujo actual
* Las sesiones remotas pueden tener prioridad o no según configuración del perfil

---

## 4. Visualización remota (GUI espejo)

* WebSocket permite sincronización con el estado interno de NORA
* Las variables clave (estado, últimas notas, hora, alertas) pueden ser reflejadas en tiempo real

---

## 5. Control administrativo

* Los usuarios tipo admin pueden:

  * Consultar logs
  * Cambiar configuraciones globales
  * Reiniciar el sistema o componentes específicos

---

El control remoto convierte a NORA en un sistema extendido, accesible y gestionable desde múltiples ubicaciones, abriendo la puerta a usos domóticos, organizativos y supervisión remota sin comprometer su lógica interna.
