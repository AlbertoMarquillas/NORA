# Protocolos de Comunicación – Interacción Remota

Este documento detalla los protocolos y métodos de comunicación considerados para habilitar la interacción remota con NORA. Se incluyen canales REST, WebSocket, MQTT y HTTP, con sus ventajas, limitaciones y mecanismos de autenticación.

---

## 1. Objetivo

Establecer una base técnica robusta para las comunicaciones entre NORA y clientes remotos, permitiendo enviar comandos, recibir eventos y consultar información en tiempo real o bajo demanda.

---

## 2. Protocolos contemplados

| Protocolo | Uso previsto                         | Tipo de comunicación    | Persistencia | Comentarios                      |
| --------- | ------------------------------------ | ----------------------- | ------------ | -------------------------------- |
| HTTP REST | Consultas y comandos bajo demanda    | Unidireccional          | No           | Sencillo, ampliamente compatible |
| WebSocket | Diálogo en tiempo real               | Bidireccional           | Sí           | Ideal para sincronización GUI    |
| MQTT      | Automatización y eventos del sistema | Publicación/suscripción | Opcional     | Eficiente en IoT y entornos LAN  |

---

## 3. Seguridad

* Autenticación con tokens por usuario (JWT o similar)
* Validación de origen (whitelisting IP o fingerprint del cliente)
* Canales cifrados (HTTPS o WSS)
* Límite de frecuencia y control de sesión activa

---

## 4. Estructura de peticiones (REST)

### Ejemplo: Enviar nota

```http
POST /api/nota HTTP/1.1
Authorization: Bearer <token>
Content-Type: application/json

{
  "texto": "Comprar pan",
  "categoria": "personal",
  "usuario_id": "laura"
}
```

### Ejemplo: Consultar estado

```http
GET /api/estado?usuario_id=laura
Authorization: Bearer <token>
```

---

## 5. Tópicos MQTT propuestos

| Tópico                | Dirección | Contenido ejemplo                |
| --------------------- | --------- | -------------------------------- |
| `nora/cmd/usuario_id` | Entrada   | `enciende luz`                   |
| `nora/data/estado`    | Salida    | `STATE_DIALOGUE`                 |
| `nora/alerta/error`   | Salida    | `Error en sensor de temperatura` |

---

Estos protocolos permiten una integración flexible y escalable con múltiples clientes y plataformas, garantizando que la interacción remota sea tan potente como la local, pero segura y trazable.
