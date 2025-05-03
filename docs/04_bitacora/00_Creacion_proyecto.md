# Estructura del Proyecto NORA

## Descripción

Este documento describe la estructura del proyecto **NORA** y cómo está organizado tanto el **Frontend** como el **Backend**.

### Estructura del Proyecto

El proyecto está organizado en los siguientes directorios principales:

```
frontend/
├── public/                # Archivos estáticos, como HTML, imágenes, iconos
│   └── index.html         # Plantilla principal de la app
├── src/                   # Código fuente de la aplicación React
│   ├── components/        # Componentes reutilizables de la interfaz
│   │   ├── Button.js      # Componente de botón
│   │   ├── Header.js      # Componente de cabecera
│   │   └── [otros]        # Otros componentes
│   ├── pages/             # Vistas de la aplicación (Home, Dashboard, Login)
│   │   ├── Home.js        # Página principal
│   │   ├── Login.js       # Página de login
│   │   └── [otros]        # Otras vistas
│   ├── services/          # Servicios para interactuar con el backend
│   │   ├── apiService.js  # Funciones para realizar peticiones HTTP
│   │   └── sensorService.js  # Funciones para interactuar con los sensores
│   ├── state/             # Gestión del estado (Redux, Context API)
│   │   ├── reducer.js     # Reducer para el estado
│   │   └── actions.js     # Acciones para el estado
│   ├── styles/            # Archivos de estilo (CSS/SCSS)
│   │   ├── main.css       # Estilos generales
│   │   └── [otros]        # Otros archivos de estilo
│   ├── utils/             # Utilidades para funciones comunes
│   │   ├── formatDate.js  # Función para formatear fechas
│   │   └── [otros]        # Otras utilidades
│   └── App.js             # Componente principal de la aplicación React
├── .gitignore             # Ignora node_modules y otros archivos
└── package.json           # Dependencias de React y configuración


backend/                 # Carpeta que contiene todo el código del backend.

├── ai_control/          # Lógica de IA y control de decisiones.
│   ├── __init__.py      # Inicializa el módulo de ai_control.
│   ├── models.py        # Modelos de IA (si es necesario).
│   ├── views.py         # Vistas relacionadas con IA.
│   ├── urls.py          # Rutas para la API de IA.
│   └── tests.py         # Pruebas unitarias de IA.
├── api/                 # Rutas y endpoints de la API para el frontend.
│   ├── __init__.py      # Inicializa el módulo de api.
│   ├── views.py         # Vistas de la API.
│   ├── urls.py          # Rutas de la API.
│   └── serializers.py   # Serializadores para convertir datos en JSON.
├── auth/                # Autenticación y gestión de usuarios.
│   ├── __init__.py      # Inicializa el módulo de auth.
│   ├── models.py        # Modelos de usuario y autenticación.
│   ├── views.py         # Vistas para el registro y login de usuarios.
│   ├── urls.py          # Rutas para las operaciones de autenticación.
│   └── serializers.py   # Serializadores de usuario para API.
├── core/                # Funciones y configuraciones comunes.
│   ├── __init__.py      # Inicializa el módulo core.
│   ├── utils.py         # Funciones reutilizables (por ejemplo, validaciones, formateo de datos).
│   └── settings.py      # Configuración global del proyecto.
├── database/            # Modelos y gestión de la base de datos.
│   ├── __init__.py      # Inicializa el módulo de database.
│   ├── models.py        # Modelos de datos (por ejemplo, Sensor, User, etc.).
│   └── migrations/      # Migraciones de la base de datos.
├── env/                 # Variables de entorno y configuración.
│   └── .env             # Archivo con las variables de entorno.
├── fsm_control/         # Lógica de la máquina de estados finitos (FSM).
│   ├── __init__.py      # Inicializa el módulo de fsm_control.
│   ├── fsm.py           # Implementación de la FSM.
│   ├── models.py        # Modelos relacionados con FSM si es necesario.
│   ├── views.py         # Vistas para controlar el flujo de la FSM.
│   └── urls.py          # Rutas de la API de FSM.
├── hardware/            # Gestión de hardware, como sensores y dispositivos.
│   ├── __init__.py      # Inicializa el módulo de hardware.
│   ├── temperature.py   # Lógica para interactuar con el sensor de temperatura.
│   ├── rtc.py           # Lógica para interactuar con el RTC.
│   ├── models.py        # Modelos relacionados con hardware si es necesario.
│   ├── views.py         # Vistas para interactuar con el hardware.
│   └── urls.py          # Rutas para controlar el hardware.
├── log/                 # Archivos de registros y logs del sistema.
│   ├── __init__.py      # Inicializa el módulo de logs.
│   └── logging.py       # Configuración de registros y almacenamiento de logs.
├── notifications/       # Sistema de notificaciones y alertas.
│   ├── __init__.py      # Inicializa el módulo de notificaciones.
│   ├── models.py        # Modelos de notificaciones.
│   ├── views.py         # Vistas para gestionar las notificaciones.
│   └── urls.py          # Rutas de la API para las notificaciones.
├── realtime/            # Comunicación en tiempo real (por ejemplo, WebSockets).
│   ├── __init__.py      # Inicializa el módulo de realtime.
│   ├── views.py         # Vistas para manejar la comunicación en tiempo real.
│   └── urls.py          # Rutas de la API de realtime.
├── sensors/             # Gestión de sensores y dispositivos de medición.
│   ├── __init__.py      # Inicializa el módulo de sensores.
│   ├── models.py        # Modelos de sensores.
│   ├── views.py         # Vistas para interactuar con los sensores.
│   ├── serializers.py   # Serializadores de sensores para la API.
│   └── urls.py          # Rutas para consultar y controlar los sensores.
├── NORA/                # Carpeta principal con la configuración del proyecto Django.
│   ├── __init__.py      # Inicializa el módulo de sensores.
│   ├── settings.py      # Configuración global del proyecto Django.
│   ├── urls.py          # Enrutamiento global del proyecto.
│   ├── wsgi.py          # Configuración de WSGI para producción.
│   └── asgi.py          # Configuración de ASGI para aplicaciones en tiempo real.
├── users/               # Gestión de usuarios y roles.
│   ├── __init__.py      # Inicializa el módulo de users.
│   ├── models.py        # Modelos de usuario (si se extiende el modelo predeterminado).
│   ├── views.py         # Vistas para gestionar usuarios.
│   ├── urls.py          # Rutas de la API de usuarios.
│   └── serializers.py   # Serializadores de usuario para API.
└── manage.py               # Archivo para ejecutar comandos de Django.

data/
├── datasets/              # Datos crudos (CSV, JSON) utilizados para entrenar IA
│   ├── sensorData.json    # Datos de sensores
│   └── [otros]            # Otros datasets
├── processing/            # Scripts de procesamiento de datos (limpieza, normalización)
│   ├── processData.py     # Script de procesamiento
│   └── [otros]            # Otros scripts de procesamiento
├── database/              # Scripts de configuración y gestión de la base de datos
│   ├── migrations/        # Migraciones de base de datos
│   └── setup.py           # Script de inicialización de base de datos
├── models/                # Modelos de IA o Machine Learning
│   ├── neuralNetwork.py   # Modelo de red neuronal
│   └── [otros]            # Otros modelos
├── training/              # Scripts y datos relacionados con el entrenamiento de IA
│   ├── trainModel.py      # Script para entrenar modelos de IA
│   └── [otros]            # Otros scripts de entrenamiento
└── .gitignore             # Ignorar datasets o archivos temporales

config/
├── raspberry/             # Configuración de la Raspberry Pi (GPIO, sensores)
│   ├── gpio.py           # Configuración de pines GPIO para sensores
│   └── wifi.py           # Configuración de conexión Wi-Fi
├── env/                  # Variables de entorno (API keys, configuración general)
│   ├── .env              # Variables sensibles como claves de API
├── settings/             # Configuraciones globales
│   └── serverSettings.py # Configuraciones del servidor (puertos, seguridad)
└── .gitignore            # Ignorar archivos de configuración sensibles

common/
├── utils/                # Funciones auxiliares
│   ├── formatDate.py     # Función para formatear fechas
│   └── [otros]           # Otras utilidades
├── helpers/              # Funciones de asistencia
│   ├── errorHandler.py   # Manejador de errores comunes
│   └── [otros]           # Otras funciones de asistencia
├── constants/            # Constantes usadas en todo el proyecto
│   ├── sensorTypes.py    # Tipos de sensores
│   └── [otros]           # Otras constantes
└── .gitignore            # Ignorar archivos temporales o innecesarios

```

### Detalles del Directorio `frontend/`:

´´´bash
mkdir project-root
cd project-root

npx create-react-app frontend
´´´

* **`node_modules/`**: Contiene todas las dependencias del proyecto instaladas con npm.
* **`public/`**: Archivos estáticos como el `index.html`.
* **`src/`**: Contiene todo el código fuente del frontend, incluidos los componentes React, servicios para interactuar con el backend, gestión del estado y estilos.

  * **`components/`**: Componentes reutilizables (botones, formularios, etc.).
  * **`services/`**: Servicios que gestionan las peticiones HTTP o WebSockets al backend.
  * **`state/`**: Lógica de gestión del estado de la aplicación (por ejemplo, con Redux o Context API).
  * **`styles/`**: Archivos CSS o SCSS para la apariencia de la app.
* **`package.json`**: Contiene las dependencias y configuraciones del proyecto.
* **`.gitignore`**: Archivos y carpetas a ser ignorados por Git.

### Detalles del Directorio `backend/`:
´´´bash
#### Primero navega a tu directorio backend
cd project-root/backend

#### Crea un entorno virtual
python -m venv env

#### Activa el entorno virtual
.\env\Scripts\activate

#### Intalar Django
pip install django

#### Crear proyecto Django
django-admin startproject NORA .

#### Crear App Django
python manage.py startapp sensors #App para gestionar sensores

#### Configruar el Proyecto
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sensors',  # Agregar nuestra app de sensores
]

#### Ejecutar
python manage.py runserver
´´´
* **`node_modules/`**: Contiene las dependencias de Node.js, como Express.
* **`controllers/`**: Controladores para manejar las peticiones de la API.
* **`routes/`**: Definición de las rutas de la API.
* **`services/`**: Lógica de negocios para interactuar con la base de datos y otros módulos.
* **`models/`**: Modelos para definir las estructuras de datos en la base de datos (si usas un ORM como Sequelize).
* **`config/`**: Archivos de configuración como las variables de entorno y la conexión a la base de datos.
* **`app.js`**: Archivo principal que inicializa el servidor y las rutas.
* **`package.json`**: Contiene las dependencias y configuraciones del proyecto backend.

### Próximos Pasos

1. **Configurar el Backend**: Inicializar el servidor y definir las rutas y controladores.
2. **Desarrollar el Frontend**: Empezar con los componentes de React y la conexión con el backend.
3. **Integrar Sensores y APIs**: Añadir la lógica de interacción con
