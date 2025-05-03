# Seguridad de Conexión – Interacción Remota

Este documento detalla las medidas de seguridad que deben aplicarse a toda interacción remota entre el usuario y NORA, garantizando confidencialidad, autenticidad, integridad de los datos y control de acceso.

---

## 1. Objetivo

Proteger las comunicaciones remotas ante riesgos como suplantación de identidad, escucha no autorizada, inyección de comandos maliciosos o acceso indebido a información personal o de configuración.

---

## 2. Canales cifrados

* Todas las comunicaciones HTTP/REST deben realizarse sobre HTTPS (TLS 1.2+)
* Los sockets WebSocket deben usar WSS (WebSocket Secure)
* Para MQTT se recomienda TLS si opera sobre red pública o VPN

---

## 3. Autenticación de usuarios

| Método                  | Descripción                                             |
| ----------------------- | ------------------------------------------------------- |
| Token JWT               | Generado al iniciar sesión remota, firmado localmente   |
| Validación NFC opcional | Posible combinación para autenticación fuerte           |
| Tiempo de expiración    | Tokens con validez limitada, renovables automáticamente |

---

## 4. Control de origen

* Lista blanca de IPs o fingerprint de cliente
* Rechazo automático de peticiones fuera de LAN si así se configura
* Logs de conexión con hora, IP y endpoint accedido

---

## 5. Protección ante abuso

* Límite de peticiones por minuto (rate limiting)
* Bloqueo temporal tras múltiples intentos inválidos
* Desactivación de usuario remoto tras eventos sospechosos

---

## 6. Almacenamiento seguro

* Los tokens se almacenan cifrados en `datos/usuarios/tokenstore.json`
* Los datos de configuración o sesión no se exponen nunca directamente por API

---

## 7. Revisión y auditoría

* El sistema debe permitir revisión de actividad remota en `logs/seguridad.log`
* Se pueden configurar alertas para admins si se detectan eventos críticos

---

Estas medidas aseguran que la interacción remota no comprometa la integridad operativa ni la privacidad de NORA, incluso cuando se accede desde entornos externos o compartidos.
