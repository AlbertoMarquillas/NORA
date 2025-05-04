# 01.esquema\_frontend.md

## Objetivo del documento

Este archivo describe el diseño funcional y estructural de la interfaz frontend de NORA, desarrollada en React. Se detallan las páginas principales, la navegación general, los tipos de usuario, y las funcionalidades accesibles según los permisos. Esta interfaz servirá como punto de interacción gráfica para usuarios generales y administradores del sistema NORA.

---

## 1. Estructura general

La interfaz estará compuesta por varias rutas principales, accesibles mediante React Router. En todas ellas se usará una barra superior común que incluirá:

* Nombre/logo del sistema (NORA)
* Navegación por rutas principales
* Estado de sesión (Iniciar sesión / Registrarse / Usuario activo)

---

## 2. Rutas principales

### `/` - Home

Página pública introductoria sobre el sistema NORA.
Contenidos:

* Qué es NORA y su objetivo
* Características principales
* Imagen representativa o mockup
* Botones para registrarse o iniciar sesión

### `/login` - Inicio de sesión

Formulario de login para usuarios ya registrados.

### `/register` - Registro de usuario

Formulario para crear una nueva cuenta de usuario.

### `/perfil` - Zona de usuario

Disponible solo para usuarios autenticados. Contiene:

* Información del perfil
* Acceso a acciones:

  * Añadir/modificar hábitos
  * Modificar la agenda
  * Gestionar listas To-Do
  * **(Solo admins)** Acceder al panel de debug integrado:

    * Visualización del estado actual de la FSM
    * Envío manual de eventos a la FSM mediante botones (ej. `EVT_WAKEWORD`, `EVT_SPEECH_START`, `EVT_PROCESS_COMPLETED`, etc.)
    * Visualización del log estructurado del sistema
    * Monitorización del contexto actual (presencia, audio, emociones)

---

## 3. Tipos de usuario

### Usuario general

* Acceso a `/`, `/login`, `/register`, `/perfil`
* Puede consultar y modificar su información personal y configuraciones

### Administrador

* Acceso total a todas las funciones disponibles en `/perfil`
* Dentro del perfil, puede inspeccionar y testear el sistema mediante la sección de debug

---

## 4. Consideraciones técnicas

* El estado de sesión se almacenará mediante JWT.
* Se utilizará `react-router-dom` para la navegación entre páginas.
* El componente de barra superior se renderizará en todas las vistas.
* La verificación de privilegios se hará tanto en el frontend como en el backend (doble validación).

---

## 5. Extensiones futuras

* Integración con FSM visual
* Sección de estadísticas personales de interacción
* Notificaciones en tiempo real (WebSocket)
* Panel para entrenar a NORA en comportamientos específicos (solo admin)

---

Este esquema servirá de base para el desarrollo estructurado del frontend del sistema NORA.
