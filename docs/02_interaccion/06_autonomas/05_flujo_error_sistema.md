# Flujo de Gestión de Errores en Interacción

Este documento describe el flujo de respuesta de NORA ante errores detectados durante una interacción activa, ya sea en la interpretación del usuario, ejecución de acciones o lectura de sensores. Su objetivo es mantener coherencia expresiva, claridad de diagnóstico y continuidad del diálogo o estado del sistema.

---

## Nombre del flujo

Gestión de errores en interacción

---

## Estado inicial

**STATE\_ACTIVE\_WAIT** o **STATE\_DIALOGUE**

Sistema en escucha o ejecutando comandos, con módulos activos.

---

## Evento disparador

* Error detectado por alguno de los siguientes módulos:

  * `voz/asr.py` (fallo de reconocimiento)
  * `dialogo/core.py` (comando mal interpretado)
  * `accionadores/` o `datos/` (error de ejecución o lectura)
  * `sensores/` (datos inválidos o desconexión)

---

## Condición de validación

* Error confirmado no transitorio (p. ej., 2 intentos fallidos consecutivos)
* Validación por `monitor/supervisor.py` o por módulo específico

---

## Acción del sistema

1. Generar mensaje de error específico o genérico
2. Mostrar expresión facial negativa (confusión o tristeza)
3. Activar LEDs en patrón de alerta (rojo tenue o intermitente)
4. Registrar el error con timestamp en `logs/fallos.log`
5. Emitir evento `EVT_AUTONOMOUS_ERROR_MSG`
6. Si es recuperable, solicitar repetición de entrada

---

## Estado final

* Vuelta a estado anterior (`STATE_ACTIVE_WAIT`), o
* Permanencia en `STATE_DIALOGUE` si se espera nueva entrada

---

## Respuesta multimodal

| Canal      | Respuesta prevista                                             |
| ---------- | -------------------------------------------------------------- |
| Voz        | “Lo siento, no he entendido eso.” / “Algo ha ido mal.”         |
| Pantalla   | Expresión de confusión (cejas caídas, ojos abiertos o dudosos) |
| LEDs       | Parpadeo rojo tenue o pulsante                                 |
| Movimiento | Cabeza inmóvil o leve inclinación hacia abajo                  |

---

## Acciones complementarias

* El error puede ser clasificado como leve, medio o crítico
* Se puede notificar a usuario admin en casos repetidos (futuro)

---

## Diagrama

El archivo `flujo_error_sistema.drawio` representará este flujo como un árbol de decisión desde el error hasta la acción tomada.

---

Este flujo asegura que NORA maneje errores con sensibilidad y coherencia, manteniendo confianza en la interacción sin detener su funcionamiento global.
