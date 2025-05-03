# Estructura de Datos – Configuración del Usuario

Este documento detalla la organización interna de los datos relacionados con la configuración del usuario en NORA. La estructura se diseña para ser fácilmente accesible, editable y extensible, manteniendo coherencia con el resto del subsistema `datos/usuario/`.

---

## 1. Archivo principal

* **Ruta:** `datos/usuario/configuracion.json`
* **Formato:** JSON plano, con claves de primer nivel por parámetro
* **Carga:** automática en la inicialización del sistema
* **Modificación:** vía comandos o GUI

---

## 2. Ejemplo de contenido

```json
{
  "nombre_usuario": "Laura",
  "idioma_respuestas": "es",
  "modo_privacidad": false,
  "formato_fecha": "DD/MM/YYYY",
  "hora_notificaciones": "20:00",
  "confirmacion_al_guardar": true
}
```

---

## 3. Validación

* Al leer el archivo, cada campo es validado por tipo y formato
* Si hay un error, se aplica un valor por defecto registrado en `config/valores_defecto.json`
* Los cambios se escriben de forma atómica para evitar corrupción

---

## 4. Acceso desde el sistema

* Módulo principal: `datos/configuracion.py`
* Funciones típicas:

  * `get_parametro(clave)`
  * `set_parametro(clave, valor)`
  * `guardar_configuracion()`

---

## 5. Relación con otros archivos

| Archivo                            | Función relacionada                                |
| ---------------------------------- | -------------------------------------------------- |
| `datos/usuario/habitos.json`       | Puede depender del idioma o frecuencia configurada |
| `datos/usuario/agenda.db`          | El formato de fecha se aplica en consultas         |
| `interfaz_escrita/config_gui.json` | Se adapta a preferencias de visualización          |

---

Esta estructura asegura un control claro sobre los parámetros que afectan el comportamiento general del asistente, permitiendo su persistencia sin complejidad añadida ni riesgo de incompatibilidad entre versiones.
