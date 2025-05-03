# Flujo de Registro de Nota o Recordatorio mediante Voz o Interfaz

Este documento describe el flujo completo que permite al usuario registrar una nota o recordatorio utilizando comandos verbales o entrada escrita, con almacenamiento en la base de datos local y confirmación clara del proceso.

---

## Nombre del flujo

Registro de nota o recordatorio mediante voz o la interfaz

---

## Estado inicial

**STATE\_ACTIVE\_WAIT**

Sistema activo, con escucha de voz habilitada y módulo de diálogo en espera de comandos.

---

## Evento disparador

* Comando de voz como “anota que tengo examen el lunes”
* Entrada escrita en GUI con intención de guardar una nota

---

## Condición de validación

* Reconocimiento exitoso por `voz/asr.py` o GUI
* Interpretación correcta de intención y contenido por `dialogo/interpretador.py`

---

## Acción del sistema

1. Capturar texto del usuario (voz o GUI)
2. Identificar intención `guardar_nota` y extraer contenido
3. Llamar a `datos/notas.py` para insertar entrada en `base_notas.db`
4. Confirmar almacenamiento exitoso
5. Emitir evento `EVT_NOTA_GUARDADA` a `estado/fsm.py`

---

## Estado final

Retorno a **STATE\_ACTIVE\_WAIT**

---

## Respuesta multimodal

| Canal      | Respuesta prevista                                           |
| ---------- | ------------------------------------------------------------ |
| Voz        | “He anotado tu recordatorio.” / “Nota guardada.”             |
| Pantalla   | Expresión positiva o sonrisa breve (ojos elevados, parpadeo) |
| LEDs       | Pulso blanco o verde suave durante 1 segundo                 |
| Movimiento | Asentimiento leve con servos (si disponibles)                |

---

## Acciones complementarias

* Registro de nota en `logs/notas.log` con timestamp y usuario
* Alerta visual en GUI escrita si se usa interfaz gráfica

---

## Diagrama

El archivo `flujo_registro_nota.drawio` representará el ciclo entrada → análisis → almacenamiento → confirmación.

---

Este flujo asegura una interacción clara, rápida y funcional entre el usuario y NORA para la gestión personal de notas, tanto por voz como por la interfaz escrita.
