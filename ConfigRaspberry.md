# Guía inicial para empezar con Raspberry Pi

Esta guía está diseñada para proporcionarte todo lo que necesitas saber antes de comenzar a trabajar con una Raspberry Pi en el contexto del proyecto NORA.

---

## 1. Modelos y elección

* **Recomendado**: Raspberry Pi 4 Model B (4GB o 8GB RAM).
* **Motivos**: rendimiento, puertos USB 3.0, soporte para periféricos, conexión Ethernet y Wi-Fi.

---

## 2. Sistema operativo

* **Raspberry Pi OS** (basado en Debian): estable, bien soportado.
* Otras opciones: Ubuntu Server, DietPi.
* Instalación mediante: [Raspberry Pi Imager](https://www.raspberrypi.com/software/) o `balenaEtcher`.

---

## 3. Almacenamiento y alimentación

* **microSD** de 16GB mínimo, clase A1 o A2 (mejor rendimiento en I/O).
* Alternativa: SSD externo por USB 3.0.
* **Fuente de alimentación** de 5V/3A con USB-C (oficial o equivalente).

---

## 4. Primer acceso

* Con teclado, ratón y pantalla (HDMI), o acceso remoto por SSH:

  * Crear archivo `ssh` vacío en la partición boot.
  * Crear `wpa_supplicant.conf` para WiFi con credenciales.

---

## 5. GPIO e interfaces

* Pines a 3.3V lógicos (no toleran 5V).
* Interfaz SPI, I2C, UART, PWM, entradas y salidas digitales.
* Librerías útiles: `RPi.GPIO`, `gpiozero`, `pigpio`, `spidev`, `smbus`.

---

## 6. Conexión de sensores

* Usa resistencias de pull-up/down si el sensor lo requiere.
* Para señales analógicas: necesitas un ADC (ej: MCP3008, MCP3203).
* En el proyecto NORA, se ha diseñado un sistema con micrófono analógico y amplificador (MAX9814) seguido de un ADC externo.

---

## 7. Voz y audio

* Raspberry Pi no tiene entrada de audio analógico integrada.
* Alternativas:

  * Micrófono USB.
  * Módulo con ADC (como en tu esquema con MCP3203).
* Pulseaudio y ALSA suelen venir instalados, aunque puede requerirse configuración adicional.

---

## 8. Desarrollo de software

* Usar `python3`, `pip`, `virtualenv` para entornos virtuales.
* Proyectos en Django, Flask, FastAPI, etc.
* Ejecución de scripts con `tmux`, `systemd` o `supervisor`.

---

## 9. Interfaz remota y debugging

* Acceso vía SSH, VNC, o entorno remoto como Visual Studio Code (via SSH).
* Logs: `journalctl`, archivos propios, `print`, `logging`.
* Monitorización de recursos con `htop`, `iotop`, `vcgencmd`.

---

## 10. Seguridad y actualizaciones

* Cambiar credenciales por defecto.
* Activar cortafuegos: `ufw`.
* Actualizar: `sudo apt update && sudo apt upgrade`.
* Hacer copias de seguridad de la tarjeta SD regularmente.

---

## 11. Comunicación entre procesos

* Usar `socket`, `MQTT`, `REST API` para comunicación local.
* En NORA, backend en Django + control por eventos (FSM).

---

## 12. Preparación de hardware

* Leer esquemas de conexión y adaptar niveles de voltaje.
* Comprobar disponibilidad de pines antes de conectar.
* Probar el sistema por partes: primero audio, luego sensores, finalmente integración FSM.

---

Si quieres, puedo preparar también una tabla de materiales recomendados para comprar y una hoja de ruta para pasar tu sistema de VirtualBox a Raspberry Pi real.
