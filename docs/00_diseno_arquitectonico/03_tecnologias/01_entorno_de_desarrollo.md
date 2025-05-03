## Entorno de Desarrollo para NORA

### 1. Requisitos de software base

**Lenguaje principal:**

- Python 3.9 o superior (recomendado Python 3.11 si el hardware lo permite para mejoras de rendimiento y eficiencia).

**Sistema operativo:**

- Raspberry Pi OS 64-bit (Lite o Desktop), basado en Debian 11 o superior.

**Herramientas básicas necesarias:**

- `git`: Control de versiones distribuido.
- `pip`: Instalación y gestión de paquetes Python.
- `venv`: Creación de entornos virtuales.
- `tmux` o `screen`: Para mantener procesos persistentes.
- `systemd`: Gestión de servicios al arranque.

**Notas específicas:**

- Se recomienda tener configurado `sudo` para ejecución segura de scripts administrativos.
- La Raspberry Pi debe contar con conectividad SSH habilitada para administración remota segura.

---

### 2. Requisitos de hardware

**Plataforma recomendada:**

- Raspberry Pi 4 Model B (2GB/4GB/8GB) o Raspberry Pi 5.

**Almacenamiento:**

- Mínimo 32GB microSD clase A1 o superior.
- Recomendado: SSD USB 3.0 para mayor rendimiento y durabilidad.

**Periféricos y accesorios:**

- Pantalla OLED/TFT conectada por SPI o I2C.
- Tira de LEDs WS2812 (Neopixels) o similar.
- Servomotores SG90 o MG90S (mínimo 2 unidades).
- Sensor de presencia (HC-SR04 o PIR).
- Sensor de temperatura y humedad (DHT22 o BME280).
- Sensor de luminosidad (TSL2561 o equivalente).
- Sensor de calidad de aire (MQ-135 o CCS811).
- Módulo NFC (PN532) para identificación.
- RTC DS3231 para gestión horaria estable.

**Requisitos de energía:**

- Fuente de alimentación oficial para Raspberry Pi (3A para RPi 4, 5A para RPi 5).
- Opcional: UPS o batería para contingencias de corte de energía.

**Notas específicas:**

- Todos los sensores deben ser compatibles con tensiones de 3.3V o 5V según el modelo de la Raspberry Pi utilizada.
- Se recomienda una ventilación pasiva adecuada (heatsinks, carcasas de aluminio) para evitar sobrecalentamiento en usos prolongados sin refrigeración activa.


## 3. Preparación inicial del sistema operativo

### 3.1. Instalación del sistema operativo

- Descargar Raspberry Pi OS 64-bit desde la web oficial de Raspberry Pi.
- Recomendado: versión Lite (sin entorno gráfico) para dispositivos destinados exclusivamente a NORA.
- Grabar la imagen en una microSD utilizando herramientas como **Raspberry Pi Imager** o **balenaEtcher**.

### 3.2. Primer arranque y configuración básica

- Insertar la microSD en la Raspberry Pi y arrancar el dispositivo.
- Configurar región, idioma y teclado mediante `raspi-config` si se utiliza Raspberry Pi OS Lite.
- Activar las siguientes interfaces desde `raspi-config`:
  - SSH (para administración remota)
  - I2C (para sensores y periféricos)
  - SPI (para pantalla facial)
  - Serial UART (si se usa comunicación UART con sensores NFC o módulos WiFi)

### 3.3. Actualización del sistema

```bash
sudo apt update
sudo apt full-upgrade -y
sudo reboot
```

### 3.4. Instalación de herramientas necesarias

```bash
sudo apt install -y git python3-pip python3-venv tmux screen
```

Opcional (si se requiere gestión avanzada de servicios):
```bash
sudo apt install -y systemd-timesyncd
```

### 3.5. Configuración de red

- Establecer una conexión WiFi o cableada estable.
- Opcionalmente, configurar IP fija para administración remota constante.

### 3.6. Configuración SSH y seguridad

- Cambiar la contraseña predeterminada:

```bash
passwd
```

- Opcional: configurar autenticación SSH mediante claves públicas para mayor seguridad.

### 3.7. Preparación de almacenamiento adicional (opcional)

- Si se utiliza un SSD o disco duro USB:
  - Formatearlo en formato ext4.
  - Montarlo automáticamente en `/etc/fstab`.

### 3.8. Consideraciones de optimización

- Deshabilitar servicios innecesarios en entornos headless (sin pantalla) para ahorrar recursos:

```bash
sudo systemctl disable lightdm
sudo systemctl disable triggerhappy
```

- Reducir el uso de swap si se utiliza almacenamiento SSD para alargar la vida útil:

```bash
sudo dphys-swapfile swapoff
sudo systemctl disable dphys-swapfile
```

### 3.9. Reinicio final

- Reiniciar para aplicar todas las configuraciones:

```bash
sudo reboot
```

## 4. Instalación y configuración del entorno de desarrollo en la Raspberry Pi

### 4.1. Creación de entorno virtual Python

- Crear y activar un entorno virtual específico para NORA:

```bash
python3 -m venv ~/nora_env
source ~/nora_env/bin/activate
```

- Actualizar `pip` a la última versión dentro del entorno virtual:

```bash
pip install --upgrade pip
```

### 4.2. Estructura de carpetas recomendada

```bash
~/nora/
├── nora_env/          # Entorno virtual Python
├── src/               # Código fuente del sistema
├── models/            # Modelos de IA
├── data/              # Bases de datos y archivos persistentes
├── logs/              # Registros de eventos y logs del sistema
├── scripts/           # Scripts de utilidad
├── config/            # Configuraciones de módulos y sistema
```

### 4.3. Descarga del repositorio de NORA

- Clonar el repositorio del proyecto en `src/`:

```bash
cd ~/nora/
git clone https://github.com/tu_usuario/nora.git src/
```

### 4.4. Instalación de dependencias globales

- Desde el entorno virtual, instalar todas las dependencias necesarias:

```bash
cd ~/nora/src/
pip install -r requirements.txt
```

- Verificar que todas las dependencias se instalan sin errores. Si alguna dependencia requiere librerías del sistema (por ejemplo, `opencv-python`), instalarlas manualmente:

```bash
sudo apt install -y libatlas-base-dev libjpeg-dev libtiff5-dev libjasper-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libgtk-3-dev libhdf5-dev libhdf5-serial-dev
```

### 4.5. Consideraciones específicas de compatibilidad ARM

- Siempre preferir versiones de librerías que tengan soporte para arquitectura ARM64.
- Evitar paquetes de IA extremadamente pesados que no estén optimizados para Raspberry Pi (usar versiones ligeras o adaptadas si es necesario).

### 4.6. Configuración de arranque automático (opcional)

- Crear un servicio `systemd` para lanzar NORA automáticamente al encender la Raspberry Pi. Se documentará en un apartado específico más adelante.

## 5. Instalación de herramientas complementarias recomendadas

### 5.1. Herramientas para la gestión de sesiones y persistencia

#### tmux

`tmux` permite crear sesiones de terminal persistentes, esenciales para mantener el sistema NORA activo aunque la sesión SSH se corte o la terminal local se cierre.

- Instalación:

```bash
sudo apt install -y tmux
```

- Comandos básicos:
  - Crear una nueva sesión:

    ```bash
    tmux new -s nora_session
    ```

  - Desconectarse de la sesión sin cerrarla:

    ```bash
    Ctrl + b, luego d
    ```

  - Reconectar a una sesión existente:

    ```bash
    tmux attach -t nora_session
    ```

#### screen (alternativa)

`screen` también permite gestionar sesiones persistentes, aunque `tmux` se recomienda por su mayor flexibilidad.

- Instalación:

```bash
sudo apt install -y screen
```

- Creación de sesión:

```bash
screen -S nora_screen
```

### 5.2. Herramientas para gestión automática de servicios

#### systemd

Se utilizará `systemd` para lanzar NORA automáticamente en el arranque de la Raspberry Pi.

- Crear un nuevo servicio en `/etc/systemd/system/nora.service`:

Ejemplo de contenido básico:

```bash
[Unit]
Description=NORA Main Service
After=network.target

[Service]
User=pi
WorkingDirectory=/home/pi/nora/src/
ExecStart=/home/pi/nora_env/bin/python main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

- Comandos principales:

```bash
sudo systemctl daemon-reload
sudo systemctl enable nora.service
sudo systemctl start nora.service
```

- Verificar estado:

```bash
sudo systemctl status nora.service
```

### 5.3. Herramientas de control remoto y diagnóstico (opcional)

#### ssh

Acceso remoto seguro a la Raspberry Pi.

- Instalación del servidor SSH (si no está instalado):

```bash
sudo apt install -y openssh-server
```

- Conexión desde otro equipo:

```bash
ssh pi@direccion_ip_local
```

#### htop

Monitor de procesos para diagnóstico de carga de CPU y RAM.

- Instalación:

```bash
sudo apt install -y htop
```

- Uso:

```bash
htop
```

#### vnstat

Monitor de tráfico de red para análisis de actividad de la interfaz de red.

- Instalación:

```bash
sudo apt install -y vnstat
```

- Inicializar vnstat para la interfaz correcta (por ejemplo, eth0 o wlan0):

```bash
sudo vnstat -u -i wlan0
```

- Ver tráfico:

```bash
vnstat
```
## 6. Compatibilidad General

### 6.1. Funcionamiento Offline

Todo el sistema NORA debe estar diseñado para funcionar completamente **sin necesidad de conexión a Internet**. Esto implica:

- Los modelos de inteligencia artificial cargados localmente (en `models/`).
- La base de datos de usuario (`datos/`) persistente en almacenamiento local.
- Todas las inferencias de visión, voz y diálogo funcionando de manera autónoma.
- La sincronización horaria opcional (RTC) sin depender de servidores NTP si no hay red.

En caso de pérdida de red:

- El sistema debe seguir operativo en modo local.
- Los módulos de supervisión y control (`control/`) registrarán el estado de desconexión.
- Las reconexiones deben ser detectadas automáticamente.

### 6.2. Compatibilidad con Arquitectura ARM64

Todos los módulos y librerías utilizadas en NORA deben ser **compatibles con Raspberry Pi OS de 64 bits** (modelo Pi 4 o Pi 5), asegurando:

- Ejecución de TensorFlow Lite o PyTorch para ARM64.
- Instalación de paquetes como `numpy`, `opencv-python`, `mediapipe`, `whisper`, `transformers`, `paho-mqtt`, etc., en versiones aptas para ARM.
- Uso exclusivo de bibliotecas que ofrezcan soporte en arquitecturas ARM64 o compilación manual si es necesario.

En caso de dependencias críticas:

- Se debe proporcionar un procedimiento de instalación alternativo (compilación manual, paquetes .deb personalizados o uso de versiones compatibles).

### 6.3. Optimización de Consumo de Recursos

El sistema debe estar optimizado para un **consumo de CPU y RAM moderado**, permitiendo:

- Ejecución continua durante largos periodos **sin necesidad de refrigeración activa** (ideal para uso fanless).
- Monitoreo continuo mediante herramientas como `htop` y `vnstat`.
- Priorización de procesos ligeros (cuando sea posible).
- Gestión de energía a través del módulo `control/gestion_energia.py`, con modos de bajo consumo durante periodos de inactividad.

Objetivos de referencia:

- Uso promedio de CPU: **< 30%** en reposo, **< 65%** durante inferencia activa.
- Uso de RAM: **< 1.5 GB** en condiciones normales de operación.
- Temperatura de CPU: mantener **< 70°C** en operación continua.

### 6.4. Tolerancia a Fallos y Recuperación Autónoma

NORA debe ser capaz de:

- Detectar fallos parciales en módulos individuales (ej. pérdida de sensores, interrupción de red).
- Registrar los fallos en `datos/` (submódulo `gestion_logs.py` y `gestion_fallos.py`).
- Intentar **recuperaciones automáticas** mediante `systemd` (reinicio de servicios) o lógica interna.
- Mantener una operación estable incluso bajo degradaciones parciales del sistema.

## 7. Buenas Prácticas de Entorno y Mantenimiento

### 7.1. Estructura de Proyecto Ordenada

El repositorio del proyecto NORA debe mantener una estructura de carpetas clara, siguiendo la organización modular definida:

- `vision/`, `voz/`, `sensores/`, `activacion/`, `agentes/`, `sistema/`, `interfaz/`, `dialogo/`, `control/`, `gui/`, `models/`, `datos/`, `utils/`, `tests/`

Cada carpeta contiene submódulos y archivos específicos claramente definidos.

Se debe evitar:

- Archivos sueltos en la raíz que no correspondan a configuraciones o entrada principal.
- Ficheros temporales o de prueba persistentes en el repositorio.

Archivos especiales:

- `README.md`: documentación principal.
- `requirements.txt`: dependencias mínimas requeridas.
- `setup_inicial.py` (opcional): script automatizado de configuración inicial.


### 7.2. Nombres de Archivos y Comandos Coherentes

Normas a seguir:

- Todo archivo `.py` debe tener nombre en minúsculas, separado por guiones bajos (`_`).
- Nombres descriptivos y breves.
- Comandos y funciones internas también deben usar snake_case.
- Clases definidas con PascalCase.

Ejemplos válidos:

- `gestion_eventos.py`
- `perfil_usuario_dialogo.py`
- `ControlEventosInternos` (nombre de clase)


### 7.3. Control de Versiones y Commits Limpios

Uso de `git` siguiendo estas prácticas:

- Commits frecuentes, pequeños y atómicos.
- Mensajes de commit claros y descriptivos.
- Estructura de mensaje:
  - Tipo: `feat:`, `fix:`, `docs:`, `style:`, `refactor:`, `test:`, `chore:`
  - Breve descripción.
  - Ejemplo: `feat: Añadir gestión de emociones en agente_visual`
- Branch principal protegida (`main` o `master`).
- Uso opcional de ramas de características (`feature/`), correcciones (`bugfix/`) y mejoras (`enhancement/`).


### 7.4. Documentación Local Automática (opcional)

Para proyectos más grandes o en expansiones futuras:

- Uso de `docstrings` en todas las funciones y clases principales.
- Herramientas recomendadas para generación de documentación:
  - `pdoc`
  - `sphinx`
  - `mkdocs`

Opcionalmente, integración de documentación en CI/CD o despliegues automáticos.

## 8. Buenas Prácticas de Entorno

### 8.1. Estructura de Carpetas Clara

Mantener una estructura de directorios clara y organizada basada en el modelo definido:

- `sistema/` → Orquestación FSM y gestión de eventos
- `voz/` → Reconocimiento, síntesis y modulación de voz
- `vision/` → Procesamiento visual y perceptivo
- `interfaz/` → Control de pantallas, LEDs, servos
- `control/` → Inicialización de hardware y supervisión
- `agentes/` → Coordinación inteligente y modulación de respuestas
- `models/` → Modelos de IA locales
- `datos/` → Persistencia de información estructurada
- `utils/` → Utilidades y funciones auxiliares
- `tests/` → Pruebas unitarias e integradas

Evitar archivos sueltos fuera de su módulo correspondiente.

### 8.2. Versionado y Control de Cambios

Utilizar `git` con las siguientes buenas prácticas:

- Commits pequeños y descriptivos.
- Branches específicos para nuevas funcionalidades o fixes.
- Integración vía Pull Requests (PR) cuando se trabaje en equipo.
- Mensajes de commit estructurados:
  - `feat: nueva funcionalidad`
  - `fix: corrección de bug`
  - `docs: actualización de documentación`
  - `refactor: mejora de código`
  - `test: añadido/actualizado test`
  - `chore: tareas menores, dependencias`

### 8.3. Documentación y Comentarios

- Documentar exhaustivamente:
  - Fichas funcionales de módulos (como las ya desarrolladas).
  - Configuraciones de entorno.
  - Procedimientos de despliegue y recuperación.
- Mantener comentarios claros en el código, siguiendo el estilo doctrinal de NORA:
  - **Antes** de funciones complejas
  - **Durante** lógicas críticas
  - **Al finalizar** procedimientos sensibles

### 8.4. Aislamiento de Entorno

- Mantener la ejecución siempre dentro de un `venv` dedicado.
- Evitar dependencias globales instaladas en el sistema.
- Asegurar la reproducción del entorno mediante:
  - `requirements.txt` actualizado.
  - Documentación de pasos post-instalación si hay configuraciones específicas.

### 8.5. Estilo de Código

- Seguir estándares PEP8.
- Aplicar `black` o `autopep8` para formato automático.
- Usar `isort` para ordenar automáticamente los imports.
- Nombres de variables y funciones descriptivos en inglés.
- Evitar "hardcoded paths" (usar `pathlib`).
- Manejar excepciones de manera explícita y documentada.

### 8.6. Logs y Diagnósticos

- Implementar logs estructurados a través de `utils/logger_sistema.py`.
- Nivel de log configurado por entorno (`DEBUG`, `INFO`, `WARNING`, `ERROR`).
- Mantener logs rotativos para evitar saturación del almacenamiento.

## 9. Procedimiento de Instalación Rápida

### 9.1. Requisitos Previos

Antes de comenzar la instalación, asegúrate de disponer de:

- Raspberry Pi 4 o 5 con Raspberry Pi OS 64 bits (Lite o Desktop).
- Acceso a terminal con permisos de administrador (usuario `pi` o equivalente).
- Conexión a red local (opcional, pero recomendable para actualizaciones iniciales).
- Sistema actualizado (`sudo apt update && sudo apt upgrade`).

### 9.2. Instalación de Dependencias del Sistema

```bash
sudo apt install -y python3 python3-pip python3-venv git tmux screen htop vnstat i2c-tools libatlas-base-dev libopenblas-dev libhdf5-dev libffi-dev libssl-dev
```

Si se utilizará comunicación con sensores I2C:
```bash
sudo raspi-config
# Interfaces -> Habilitar I2C
```

### 9.3. Creación y Activación del Entorno Virtual

```bash
python3 -m venv ~/nora_env
source ~/nora_env/bin/activate
```


### 9.4. Clonación del Repositorio de NORA

```bash
cd ~
git clone <URL_DEL_REPOSITORIO>
cd nora
```


### 9.5. Instalación de Dependencias del Proyecto

Dentro del entorno virtual:

```bash
pip install -r requirements.txt
```


### 9.6. Configuración de la Ejecución Automática

Opcional pero recomendado para arranque automático al iniciar la Raspberry Pi:

```bash
sudo nano /etc/systemd/system/nora.service
```

Contenido sugerido:

```ini
[Unit]
Description=NORA Startup Service
After=network.target

[Service]
User=pi
WorkingDirectory=/home/pi/nora
ExecStart=/home/pi/nora_env/bin/python3 /home/pi/nora/sistema/sistema_main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Activar el servicio:

```bash
sudo systemctl daemon-reload
sudo systemctl enable nora.service
sudo systemctl start nora.service
```


### 9.7. Comprobación de Instalación

- Verificar que NORA está corriendo:

```bash
sudo systemctl status nora.service
```

- Para ver logs de la ejecución:

```bash
journalctl -u nora.service -f
```


### 9.8. Notas Finales

- El entorno puede ser actualizado reactivando el `venv` y actualizando `requirements.txt`.
- Recomendado hacer copias periódicas de seguridad del directorio `datos/`.
- Para detención manual del sistema:

```bash
sudo systemctl stop nora.service
```

- Para reiniciar manualmente:

```bash
sudo systemctl restart nora.service
```

## 10. Procedimiento de Mantenimiento y Actualización

### 10.1. Actualización de Código Fuente

Para actualizar NORA desde el repositorio principal:

```bash
cd ~/nora
source ~/nora_env/bin/activate
git pull origin main
pip install -r requirements.txt  # Solo si hay nuevos requisitos
```

### 10.2. Actualización de Dependencias

En caso de que se modifiquen librerías:

```bash
source ~/nora_env/bin/activate
pip install --upgrade -r requirements.txt
```

Se recomienda hacer una copia de seguridad del entorno virtual antes de actualizar.

### 10.3. Backup de Datos Importantes

Respaldar periódicamente:

```bash
cd ~/nora
mkdir -p backups
cp -r datos/ backups/datos_backup_$(date +%F)
```

Opcionalmente, configurar un cronjob para automatizar backups:

```bash
crontab -e
```

Agregar línea:

```bash
0 2 * * * /bin/bash -c 'cd /home/pi/nora && cp -r datos/ backups/datos_backup_$(date +\%F)'
```
(Este ejemplo hace un backup diario a las 2:00 AM).

### 10.4. Mantenimiento del Sistema Operativo

Actualizar el sistema operativo regularmente:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt autoremove -y
```

Verificar estado de disco:

```bash
df -h
```

Verificar uso de RAM y CPU:

```bash
htop
```

### 10.5. Pruebas de Salud del Sistema

Ejecutar pruebas periódicas:

```bash
source ~/nora_env/bin/activate
python3 tests/tests_main.py
```

Supervisar:
- Integridad de sensores
- Rendimiento de modelos de inferencia
- Estado del hardware (temperatura, voltaje)

### 10.6. Procedimiento de Recuperación ante Fallos

Si un módulo falla:

1. Verificar el estado con:
```bash
sudo systemctl status nora.service
```
2. Consultar logs:
```bash
journalctl -u nora.service -f
```
3. Reiniciar servicio:
```bash
sudo systemctl restart nora.service
```
4. Si el error persiste, revisar el último `git pull` o volver a una versión anterior del repositorio si fuera necesario.

### 10.7. Checklist de Mantenimiento Mensual

- [ ] Actualizar sistema operativo.
- [ ] Verificar actualizaciones de código.
- [ ] Actualizar dependencias.
- [ ] Revisar salud del hardware (temperatura, RAM, almacenamiento).
- [ ] Realizar backup completo de `datos/`.
- [ ] Ejecutar tests de salud.
- [ ] Validar correcto funcionamiento de todos los sensores.


### 10.8. Notas de Seguridad

- Configurar `ufw` (firewall) si la Raspberry Pi está expuesta a red:

```bash
sudo apt install ufw
sudo ufw allow ssh
sudo ufw enable
```

- Cambiar contraseña por defecto del usuario `pi`.
- Deshabilitar servicios innecesarios.
- Actualizar claves SSH regularmente si hay acceso remoto.

## 11. Estrategias de Optimización de Recursos

### 11.1. Optimización de Uso de CPU

- **Asignación de afinidad de procesos**: limitar NORA a núcleos específicos para liberar otros recursos del sistema.
- **Control de frecuencia dinámica (DVFS)**: utilizar `cpufrequtils` para ajustar políticas de ahorro energético.
- **Reducción de prioridad de procesos secundarios**: usar `nice` o `ionice` para tareas no críticas.

### 11.2. Gestión Eficiente de Memoria

- **Liberación explícita de recursos**: cierre adecuado de procesos, cierre de archivos abiertos, limpieza de objetos en Python.
- **Carga perezosa de modelos**: cargar modelos de IA solo cuando sean requeridos, descargarlos de memoria tras uso si es posible.
- **Uso de estructuras de datos ligeras**: preferencia por `numpy` arrays frente a listas grandes, estructuras optimizadas.

### 11.3. Minimización de Acceso a Disco

- **Escritura diferida de datos**: agrupar operaciones de escritura en disco en lotes.
- **Uso de almacenamiento en RAM cuando sea posible**: tmpfs para logs temporales o bases de datos efímeras.
- **Compresión ligera**: aplicar compresión automática para históricos y respaldos (`gzip`, `lz4`).

### 11.4. Optimización de Red

- **Evitar dependencias de conexión externa**: garantizar operación 100% offline.
- **Compresión de tráfico interno si se usa**: en comunicaciones MQTT o web sockets.

### 11.5. Buenas Prácticas de Código

- **Programación asíncrona donde sea viable**: especialmente en `sistema/`, `voz/` y `interfaz/`.
- **Control de excepciones robusto**: evitar caídas innecesarias por errores no manejados.
- **Modularidad extrema**: cargar solo los módulos necesarios según modo de operación.

### 11.6. Consideraciones Hardware

- **Disipadores pasivos**: recomendados aunque el sistema esté optimizado para no generar sobrecalentamiento.
- **Medición periódica de temperatura y carga**: activar alarmas preventivas si CPU > 75ºC o RAM > 85%.

### 11.7. Monitorización Continua

- **Uso de herramientas como `htop`, `vnstat`, `iotop`**: monitoreo en tiempo real.
- **Logs de recursos**: registro histórico para análisis y ajustes.

Estas estrategias aseguran que NORA pueda operar de forma fluida, estable y eficiente en hardware como Raspberry Pi sin necesidad de refrigeración activa, maximizando la vida útil de la plataforma y garantizando una experiencia de usuario óptima.

## 12. Buenas Prácticas de Codificación y Estructura de Proyecto

### 12.1. Estilo de Código

- **Convenciones PEP8**: todo el código Python debe seguir la guía de estilo PEP8.
- **Nombres descriptivos**: variables, funciones y clases deben usar nombres que indiquen claramente su propósito.
- **Uso de type hints**: especificar tipos de entrada y salida en funciones para mejorar la legibilidad y facilitar herramientas de análisis estático.
- **Documentación completa**: todas las funciones, clases y módulos deben incluir docstrings claros siguiendo el estándar Google o NumPy.
- **Longitud de línea**: preferencia por líneas de máximo 100 caracteres para mejorar la lectura en terminales.

### 12.2. Estructura de Proyecto

- **Separación clara de módulos**: cada directorio funcional (`vision/`, `voz/`, `sistema/`, etc.) contiene solo el código relacionado a su responsabilidad.
- **Archivo `__init__.py`**: presente en todos los submódulos para garantizar importaciones limpias.
- **Carpetas específicas para datos y modelos**: `models/` y `datos/` organizados por dominio y tipo de dato.
- **Directorio `utils/` unificado**: todas las funciones auxiliares comunes centralizadas para evitar duplicación de código.
- **Directorio `tests/` paralelo al código**: misma estructura que el proyecto principal para pruebas unitarias y de integración.

### 12.3. Documentación y Manuales

- **README detallado**: en cada directorio funcional, indicando su propósito y dependencias específicas.
- **Manual de despliegue**: instrucciones paso a paso para instalar, configurar y lanzar NORA.
- **Documentación de APIs internas**: para eventos, comandos y configuraciones JSON.

### 12.4. Control de Versiones

- **Commits pequeños y descriptivos**: cada commit debe representar un cambio funcional específico.
- **Branching claro**:
  - `main`: solo versiones estables.
  - `develop`: integración de cambios en curso.
  - `feature/*`, `fix/*`, `test/*`: ramas específicas para funcionalidades nuevas, correcciones y pruebas.
- **Uso de etiquetas (`tags`)**: marcar versiones relevantes del proyecto (`v1.0`, `v1.1-beta`, etc.).

### 12.5. Manejo de Configuraciones

- **Archivos de configuración separados**: `config_*.py` por módulo, o `*.json` en `configs/`.
- **Variables sensibles excluidas**: credenciales y secretos gestionados en archivos seguros, nunca en el repositorio.
- **Carga dinámica de configuraciones**: permitir actualización de parámetros en tiempo de ejecución sin reiniciar NORA.

### 12.6. Seguridad y Robustez

- **Control exhaustivo de errores**: manejo de excepciones en puntos críticos.
- **Validación estricta de entradas**: todo dato de entrada debe ser validado y sanitizado.
- **Logs estructurados**: eventos críticos, advertencias y errores deben registrarse claramente.

Estas buenas prácticas aseguran que el código de NORA sea mantenible, escalable, robusto y fácilmente comprensible por cualquier nuevo desarrollador o colaborador que se incorpore al proyecto.

## 13. Política de Librerías Externas Permitidas

### 13.1. Criterios Generales de Aceptación

Para mantener la estabilidad, seguridad y rendimiento del sistema NORA, solo se permitirán librerías externas que cumplan todos los siguientes criterios:

- **Compatibilidad ARM64**: Deben funcionar de forma estable en arquitecturas ARM64, como las de Raspberry Pi 4 y 5.
- **Licencia abierta compatible**: Deben tener licencias como MIT, BSD, Apache 2.0 o equivalentes. No se aceptarán librerías con licencias restrictivas o ambigua.
- **Operación Offline**: No deben requerir conexión permanente a Internet para funcionar.
- **Bajo consumo de recursos**: Preferencia por librerías ligeras, optimizadas para dispositivos de bajo consumo.
- **Mantenimiento activo**: Deben estar mantenidas o al menos estables, con última actualización no superior a 3 años.
- **Documentación adecuada**: Se requiere documentación oficial o referencias completas para su uso correcto.

### 13.2. Librerías Específicamente Aprobadas

- **Procesamiento general**:
  - `numpy`
  - `scipy`
  - `pandas`

- **Visión artificial**:
  - `opencv-python`
  - `mediapipe`

- **Procesamiento de audio**:
  - `pyaudio`
  - `webrtcvad`
  - `pyttsx3`

- **Machine Learning y Deep Learning**:
  - `tensorflow` (versión Lite o optimizada ARM si es posible)
  - `torch` (solo versiones ARM64)
  - `scikit-learn`

- **Interfaz gráfica y visualización**:
  - `tkinter`
  - `Pillow`
  - `PyQt5` (opcional, preferiblemente en modos de GUI local)

- **Sistema y hardware**:
  - `RPi.GPIO`
  - `gpiozero`
  - `smbus2`
  - `psutil`

- **Eventos y comunicación interna**:
  - `pyee`
  - `eventlet` (solo en contextos aislados)

- **Administración remota o web opcional**:
  - `flask`
  - `dash` (solo para interfaz remota avanzada)

- **Persistencia y bases de datos**:
  - `sqlite3` (módulo estándar)
  - `dataset`
  - `SQLAlchemy`

- **Otros auxiliares**:
  - `json`
  - `yaml`
  - `logging`
  - `datetime`

### 13.3. Librerías Restringidas o Excluidas

- **Librerías excesivamente pesadas**: como `opencv-contrib-python`, `tensorflow full` (salvo versión Lite adaptada).
- **Librerías con dependencias externas obligatorias**: que requieran conexión a API externas para funciones críticas.
- **Paquetes en estado experimental o no mantenidos**: versiones beta o sin mantenimiento documentado.
- **Librerías de pago o con licencias cerradas**: todo software que imponga restricciones legales o técnicas al despliegue.

### 13.4. Procedimiento para Aprobar Nuevas Librerías

1. **Solicitud documentada**: incluir nombre, versión propuesta, justificación de necesidad.
2. **Evaluación técnica**: análisis de compatibilidad ARM64, rendimiento, peso y dependencia de terceros.
3. **Test de integración**: prueba de funcionamiento en entorno de pruebas de Raspberry Pi.
4. **Aprobación formal**: inclusión explícita en el documento de dependencias permitidas.

### 13.5. Consideraciones Especiales

- **Librerías para GUI** deben poder funcionar opcionalmente desactivadas si el sistema opera en modo "sin interfaz gráfica".
- **Librerías de IA** deben ser cargadas de manera perezosa (`lazy loading`) para ahorrar RAM.
- **Actualizaciones controladas**: actualización de librerías solo previa validación de compatibilidad.

Esta política asegura que el ecosistema de NORA siga siendo **ligero, modular, mantenible y 100% operativo en modo offline** sobre plataformas ARM64 de bajo consumo.

## 14. Gestión de Entornos Virtuales y Recomendaciones Avanzadas

### 14.1. Creación y Uso del Entorno Virtual

- **Creación del entorno**:
  ```bash
  python3 -m venv nora_env
  ```

- **Activación**:
  ```bash
  source nora_env/bin/activate
  ```

- **Desactivación**:
  ```bash
  deactivate
  ```

- **Importancia**:
  - Aislar las dependencias de NORA del sistema operativo base.
  - Facilitar actualizaciones y mantenimientos controlados.
  - Permitir múltiples versiones de librerías sin conflictos.

### 14.2. Instalación de Dependencias

- **Instalación directa**:
  ```bash
  pip install -r requirements.txt
  ```

- **Actualización segura de paquetes**:
  ```bash
  pip list --outdated
  pip install --upgrade nombre_paquete
  ```

- **Congelación del entorno actualizado**:
  ```bash
  pip freeze > requirements.txt
  ```

### 14.3. Organización de Requerimientos

- **División opcional de archivos**:
  - `requirements_core.txt`: dependencias esenciales de producción.
  - `requirements_dev.txt`: dependencias solo para desarrollo y testing.
  - `requirements_optional.txt`: librerías adicionales o experimentales.

- **Instalación selectiva**:
  ```bash
  pip install -r requirements_core.txt
  pip install -r requirements_dev.txt
  ```

### 14.4. Buenas Prácticas

- **Entorno virtual dedicado por rama principal**:
  - Evitar contaminación de dependencias entre ramas o versiones mayores del proyecto.

- **No activar el entorno virtual en `~/.bashrc`**:
  - Mejor activar manualmente o mediante scripts de arranque específicos para evitar problemas con otros proyectos.

- **Verificación de compatibilidad antes de actualizar**:
  - Probar nuevas versiones de librerías en entornos virtuales de prueba antes de aplicar a producción.

- **Uso de alias o scripts de automatización**:
  - Por ejemplo, alias `startnora` que active entorno y arranque la aplicación:
    ```bash
    alias startnora='cd /ruta/nora && source nora_env/bin/activate && python sistema_main.py'
    ```

## 15. Automatización con Scripts y Entornos CI/CD (Opcional)

### 15.1. Scripts de Automatización Local

- **Script de inicialización**: script bash (`setup_nora.sh`) para configurar el entorno en una Raspberry Pi desde una instalación limpia.
  - Actualización de sistema operativo.
  - Instalación de dependencias base (Python, pip, git, tmux, systemd utilities).
  - Clonación del repositorio.
  - Creación y activación de entorno virtual.
  - Instalación de requirements.

- **Script de despliegue**: actualización del repositorio y reinicio seguro de servicios relacionados con NORA.

### 15.2. Integración Continua (CI)

- **Repositorio Git**: estructura de ramas estándar (`main`, `develop`, `feature/*`).
- **Validaciones automáticas**:
  - Tests unitarios automáticos (`pytest`) en cada push.
  - Análisis de calidad de código (opcional) con `flake8`, `pylint`.
  - Verificación de dependencias.

- **Plataformas compatibles** (opcional):
  - GitHub Actions.
  - GitLab CI.
  - Jenkins (para entornos autogestionados).

### 15.3. Despliegue Continuo (CD) Opcional

- **Actualización automática controlada** en Raspberry Pi bajo condiciones seguras:
  - Pull automático de rama estable.
  - Reinicio controlado de servicios.
  - Rollback automático en caso de error.

- **Consideraciones**:
  - El sistema debe seguir funcionando offline, incluso durante despliegues parciales.
  - Ningún despliegue debe interrumpir funciones críticas (activación, alarmas, seguridad).

### 15.4. Recomendaciones Generales para CI/CD en NORA

- Preferencia por **testing local exhaustivo** antes de integrar cambios.
- Separar **testing unitario**, **testing de integración** y **testing de hardware**.
- Documentar en README los comandos de build, test y deploy.
- Uso de etiquetas (`tags`) y versionado semántico (`v1.0.0`, `v1.1.0`, etc.) para las releases.

Estas estrategias permitirán en el futuro facilitar el mantenimiento, escalar el proyecto y aumentar la fiabilidad del despliegue de actualizaciones en sistemas productivos.

## 16. Consideraciones de Seguridad Básicas

### 16.1. Seguridad del Entorno

- **Actualización continua** del sistema operativo Raspberry Pi (parches de seguridad).
- **Actualización de paquetes Python**: revisión periódica de `pip list --outdated` y actualización controlada.
- **Uso de entornos virtuales** (`venv`) para aislar dependencias y evitar conflictos o instalaciones accidentales globales.
- **Protección del acceso físico**: asegurar que la Raspberry Pi esté ubicada en entornos confiables o protegidos.

### 16.2. Seguridad en la Red

- **Configuración segura de SSH**:
  - Deshabilitar acceso SSH por contraseña (`PasswordAuthentication no`) y usar autenticación por clave pública.
  - Cambiar el puerto SSH por defecto.
- **Firewall básico** con `ufw` o `iptables`, limitando los puertos expuestos (idealmente solo SSH si es necesario).
- **VPN opcional**: en entornos remotos, conectar la Raspberry Pi a través de una VPN segura.

### 16.3. Gestión de Usuarios y Permisos

- **Principio de mínimo privilegio**:
  - El sistema de NORA debe ejecutarse con un usuario restringido, no con `root`.
  - Configurar permisos mínimos necesarios para cada servicio o script.
- **Bloqueo de superusuario**: evitar el acceso directo como `root` en producciones de uso estándar.

### 16.4. Seguridad en la Gestión de Datos

- **Encriptación opcional** de la base de datos local (`datos/`) o uso de almacenamiento seguro.
- **Política de backups cifrados** periódicos en dispositivos externos o servicios en la red interna segura.
- **Retención limitada de datos sensibles**: establecer políticas de expiración de datos emocionales, historiales de conversaciones o rutinas personales.

### 16.5. Seguridad en los Modelos de IA

- **Validación de fuentes** de los modelos descargados para evitar cargas de modelos manipulados maliciosamente.
- **Verificación de integridad** (checksums) antes de instalar modelos o actualizaciones.

### 16.6. Logs y Auditoría

- **Control de logs**:
  - Evitar guardar en logs información sensible del usuario.
  - Rotación de logs automática (`logrotate`) para evitar saturación del almacenamiento.
- **Auditoría periódica** del historial de eventos y actividades registradas para detectar anomalías.

## 17. Documentación y Mantenimiento

### 17.1. Generación Automática de Documentación

- Utilización de herramientas como:
  - **Sphinx**: generación de documentación HTML/PDF a partir de docstrings estructurados.
  - **pdoc** o **mkdocs**: alternativas ligeras para documentación API navegable.
- Documentación obligatoria para:
  - Definición de eventos estándar (`CMD_`, `EVT_`, `AGT_`).
  - Flujo de activación, conversación y expresión emocional.
  - Arquitectura modular y relaciones entre subsistemas.
- Actualización automática con cada commit relevante cuando sea posible.

### 17.2. Actualización Continua de la Documentación

- Registro de cambios en la documentación junto con los cambios de código.
- Versionado documental asociado a las versiones del sistema.
- Validación obligatoria de documentación antes de cerrar una versión estable.

### 17.3. Estándar de Documentación Interna

- Uso de **docstrings** obligatorios en todas las funciones, clases y módulos:
  - Estilo preferido: **Google docstring** o **reStructuredText**.
- Comentarios explicativos en zonas críticas del código.
- Plantillas de estructura para nuevos módulos o funciones extensas.

### 17.4. Notas de Versión (Release Notes)

- Estructura estandarizada en cada entrega:
  - `Added`, `Changed`, `Fixed`, `Removed`.
- Inclusión de sección de **Breaking Changes** si corresponde.
- Guía de migración documentada para cambios incompatibles.

### 17.5. Guías de Despliegue y Actualización

- **Scripts de soporte**:
  - `setup.sh`: creación de entorno virtual, instalación de dependencias.
  - `upgrade.sh`: actualización incremental de paquetes y configuraciones.
- Procedimientos documentados para:
  - Instalación limpia en Raspberry Pi.
  - Actualización segura entre versiones.
  - Restauración del sistema tras fallo crítico.

## 18. Buenas Prácticas de Logs y Diagnóstico

### 18.1. Principios Generales

- **Coherencia estructural**: todos los logs deben tener una estructura estandarizada: timestamp, módulo, nivel de severidad, mensaje.
- **Separación de logs**: logs críticos, de sistema, de usuario y de auditoría deben almacenarse en ficheros diferenciados.
- **Formato legible y machine-readable**: se recomienda el uso de formatos como JSONL o texto estructurado simple para logs críticos.
- **Persistencia rotativa**: los ficheros de logs deben rotarse periódicamente para evitar saturación del almacenamiento (úso de herramientas como `logrotate`).

### 18.2. Niveles de Severidad Estándar

- **DEBUG**: Información detallada para depuración.
- **INFO**: Eventos normales, confirmaciones de funcionamiento esperado.
- **WARNING**: Comportamientos no críticos pero anómalos.
- **ERROR**: Fallos que impiden el correcto funcionamiento de una parte del sistema.
- **CRITICAL**: Fallos graves que pueden afectar a la estabilidad general.

### 18.3. Recomendaciones para el Loggeo Modular

- **Cada módulo debe inicializar su propio logger** con nombre derivado del nombre del módulo (ej. `voz.asr`, `vision.pipeline`).
- **Logs de agente** deben incluir el ID del agente y el contexto de evaluación.
- **Logs de eventos** deben capturar tipo de evento, origen, y destino.
- **Logs de errores** deben registrar stacktrace resumido cuando sea posible.

### 18.4. Buenas Prácticas de Diagnóstico

- **Sistema de "autodiagnóstico"**: al arranque, lanzar tests automáticos ligeros sobre estado de sensores, conexión a periféricos, espacio libre en disco, temperatura de CPU.
- **Checkpoints de diagnóstico**: cada 24 horas (o ajustable), realizar una validación rápida del estado de funcionamiento básico.
- **Alertas anticipadas**:
  - Detección de temperaturas excesivas.
  - Pérdida de conexión a sensores o periféricos.
  - Saturación de almacenamiento > 80%.
- **Registro de análisis de fallo**: ante un error crítico, crear automáticamente un paquete de diagnóstico que contenga:
  - Últimos logs relevantes.
  - Estado de la FSM en el momento del fallo.
  - Stacktrace resumido.

### 18.5. Políticas de Retención de Logs

- **Logs críticos**: conservar un histórico de al menos 7 días.
- **Logs de DEBUG**: conservación temporal (24-48 horas), eliminación automática.
- **Logs de auditoría de eventos**: conservación ampliada (hasta 90 días) si no contienen información sensible.

### 18.6. Herramientas de Soporte Recomendadas

- **logging** (Python estándar): configurado para rotación automática.
- **logrotate**: manejo externo de rotación y purgado de ficheros.
- **psutil**: supervisión de recursos para activación de alertas preventivas.
- **tmux/screen**: supervisión de logs en vivo durante fases de pruebas intensivas.

### 18.7. Integración en el Sistema

- **Logs separados por módulo**: cada módulo (`voz/`, `vision/`, `agentes/`, etc.) debe generar sus propios archivos de logs.
- **Dashboard opcional**: posibilidad de integrar en `gui/` una vista básica de eventos y alertas recientes.
- **Eventos de log importantes** deben generar notificaciones internas para agentes de seguridad o mantenimiento.

## 19. Plan de Mantenimiento del Entorno

### 19.1. Objetivo del Mantenimiento
Garantizar la estabilidad, eficiencia, seguridad y adaptabilidad del entorno de ejecución de NORA a lo largo del tiempo, minimizando riesgos de fallo, vulnerabilidades o degradación de rendimiento.

### 19.2. Tareas de Mantenimiento Periódico

- **Actualización del Sistema Operativo**:
  - Comando periódico recomendado:
    ```bash
    sudo apt update && sudo apt full-upgrade
    ```
  - Revisar cambios de versión críticos manualmente para evitar incompatibilidades.

- **Actualización del Entorno Python**:
  - Activar el entorno virtual:
    ```bash
    source nora_env/bin/activate
    ```
  - Actualizar paquetes importantes:
    ```bash
    pip list --outdated
    pip install --upgrade paquete
    ```

- **Renovación de Modelos de IA** (cuando aplique):
  - Verificar disponibilidad de nuevas versiones de modelos en `models/`.
  - Validar integridad de nuevos modelos antes de instalarlos.

- **Backup de Datos y Configuraciones**:
  - Backup de `datos/`, `config/`, y `models/` de forma mensual.
  - Recomendado uso de scripts automáticos de backup a dispositivos externos o nube privada.

- **Inspección de Hardware**:
  - Verificación de temperatura de CPU:
    ```bash
    vcgencmd measure_temp
    ```
  - Comprobación del estado del almacenamiento (microSD o SSD).

- **Revisiones de Seguridad**:
  - Verificar puertos abiertos:
    ```bash
    sudo netstat -tulnp
    ```
  - Validar integridad de paquetes instalados:
    ```bash
    debsums -s
    ```

- **Limpieza de Archivos Temporales**:
  - Liberar espacio de almacenamiento:
    ```bash
    sudo apt autoremove
    sudo apt clean
    ```

### 19.3. Frecuencias Sugeridas
| Tarea                           | Frecuencia Recomendada |
|----------------------------------|-------------------------|
| Actualización del sistema       | Mensual                 |
| Actualización del entorno Python | Cada 2-3 meses          |
| Backup completo                 | Mensual                 |
| Inspección de hardware          | Trimestral              |
| Revisión de seguridad           | Mensual                 |
| Limpieza de temporales          | Mensual                 |

### 19.4. Herramientas Auxiliares Recomendadas
- `cron` para programar tareas automáticas de mantenimiento.
- `rpi-clone` para backups rápidos de tarjetas SD/SSD.
- `glances` para monitoreo en tiempo real del sistema.
- `rsync` para sincronización segura de datos.

### 19.5. Notas Adicionales
- Documentar cada operación de mantenimiento importante en un archivo de log de mantenimiento.
- No realizar actualizaciones automáticas críticas sin validación manual previa.
- Ante cambios mayores, probar primero en entornos de prueba si es posible.

### 19.6. Mantenimiento Preventivo

**Frecuencia semanal:**
- Ejecutar `sudo apt update && sudo apt upgrade` en la Raspberry Pi.
- Actualizar las dependencias de Python con `pip list --outdated` y, si procede, `pip install --upgrade <paquete>`.
- Verificar el estado de los servicios críticos con `systemctl status <servicio>`.
- Comprobar el estado de red y conectividad externa.
- Supervisar espacio de almacenamiento con `df -h`.
- Revisar la carga del sistema con `htop` o `top`.

**Frecuencia mensual:**
- Aplicar parches de seguridad mayores al sistema operativo (Kernel y paquetes críticos).
- Actualizar controladores y firmware de hardware (si disponible).
- Validar versiones de modelos de IA instalados.
- Realizar un backup completo del entorno virtual (`nora_env`) y de la base de datos `datos/`.

**Frecuencia trimestral:**
- Rotación de logs históricos mediante `logrotate` o eliminación manual de archivos obsoletos.
- Validación de integridad de bases de datos (`PRAGMA integrity_check;` en SQLite).
- Auditoría de configuraciones: `config_sistema.py`, `config_voz.py`, `config_sensores.py`, etc.
- Comprobación de versiones de herramientas críticas: `python3 --version`, `git --version`, etc.

### 19.7. Mantenimiento Correctivo

- Diagnóstico y resolución de errores detectados mediante los logs del sistema o de aplicación.
- Actualización de dependencias específicas en caso de fallo de compatibilidad.
- Reinicio o reinstalación controlada de módulos defectuosos.
- Reconstrucción del entorno virtual si se detectan corrupciones (`python3 -m venv --clear nora_env`).
- Aplicación de procedimientos de restauración desde backups en caso de fallo catastrófico.

### 19.8. Recomendaciones Adicionales

- Mantener siempre un backup externo reciente de toda la carpeta de proyecto.
- Documentar todos los cambios relevantes aplicados en cada sesión de mantenimiento.
- Automatizar en lo posible tareas repetitivas mediante scripts seguros.
- Minimizar el tiempo de inactividad programando mantenimientos en horas valle.

### 19.9. Herramientas Sugeridas para el Mantenimiento

- `cron` para programación de tareas automáticas.
- `rsync` para backups incrementales eficientes.
- `ufw` o `iptables` para ajuste dinámico de reglas de firewall.
- `tmux` o `screen` para ejecución persistente de tareas de diagnóstico.
- `fail2ban` para protección ante accesos maliciosos a SSH.

## 20. Anexo: Comandos Rápidos Útiles para el Entorno

Este anexo recopila comandos esenciales para la gestión diaria y el mantenimiento del entorno de desarrollo y ejecución de NORA en Raspberry Pi. Se organiza por categoría funcional para fácil referencia.

### 20.1. Gestión de Entorno Virtual

- Crear entorno virtual:
  ```bash
  python3 -m venv nora_env
  ```

- Activar entorno virtual:
  ```bash
  source nora_env/bin/activate
  ```

- Instalar dependencias:
  ```bash
  pip install -r requirements.txt
  ```

- Salir del entorno virtual:
  ```bash
  deactivate
  ```

### 20.2. Gestión de Paquetes

- Actualizar `pip`:
  ```bash
  python3 -m pip install --upgrade pip
  ```

- Listar paquetes desactualizados:
  ```bash
  pip list --outdated
  ```

- Actualizar un paquete específico:
  ```bash
  pip install --upgrade nombre_paquete
  ```

### 20.3. Control de Versiones (Git)

- Clonar repositorio:
  ```bash
  git clone https://github.com/AlbertoMarquillas/NORA.git
  ```

- Crear nueva rama:
  ```bash
  git checkout -b nombre_rama
  ```

- Confirmar cambios:
  ```bash
  git add .
  git commit -m "Mensaje descriptivo"
  git push origin nombre_rama
  ```

- Actualizar rama local:
  ```bash
  git pull origin nombre_rama
  ```

### 20.4. Gestión de Sesiones Persistentes

- Iniciar sesión nueva con `tmux`:
  ```bash
  tmux new -s nombre_sesion
  ```

- Reanudar sesión:
  ```bash
  tmux attach-session -t nombre_sesion
  ```

- Listar sesiones activas:
  ```bash
  tmux ls
  ```

### 20.5. Control de Servicios con `systemd`

- Crear un servicio:
  ```bash
  sudo nano /etc/systemd/system/nora.service
  ```

- Recargar configuración de servicios:
  ```bash
  sudo systemctl daemon-reload
  ```

- Iniciar servicio:
  ```bash
  sudo systemctl start nora.service
  ```

- Habilitar servicio al arranque:
  ```bash
  sudo systemctl enable nora.service
  ```

- Ver estado del servicio:
  ```bash
  sudo systemctl status nora.service
  ```

### 20.6. Gestión de Logs

- Visualizar logs de sistema:
  ```bash
  journalctl -u nora.service
  ```

- Limpiar logs antiguos:
  ```bash
  sudo journalctl --vacuum-time=7d
  ```

### 20.7. Otros Comandos últiles

- Monitorizar consumo de CPU/RAM:
  ```bash
  htop
  ```

- Comprobar temperatura CPU Raspberry Pi:
  ```bash
  vcgencmd measure_temp
  ```

- Sincronizar hora con servidores NTP:
  ```bash
  sudo timedatectl set-ntp true
  ```

- Verificar conexión a red:
  ```bash
  ping 8.8.8.8
  ```

- Apagar Raspberry Pi de forma segura:
  ```bash
  sudo shutdown now
  ```

- Reiniciar Raspberry Pi:
  ```bash
  sudo reboot
  ```

---

Este anexo debe ser mantenido actualizado si se añaden nuevas herramientas o flujos de trabajo en el entorno de desarrollo de NORA.

## 21. Anexo: Comandos Rápidos ÚTiles para el Entorno

### 21.1. Inicialización Rápida del Entorno

- Crear entorno virtual:
  ```bash
  python3 -m venv nora_env
  ```

- Activar entorno virtual:
  ```bash
  source nora_env/bin/activate
  ```

- Instalar dependencias:
  ```bash
  pip install -r requirements.txt
  ```

### 21.2. Actualización del Entorno

- Actualizar paquetes instalados:
  ```bash
  pip list --outdated
  pip install --upgrade <paquete>
  ```

- Actualizar sistema operativo (Raspberry Pi OS):
  ```bash
  sudo apt update && sudo apt full-upgrade -y
  sudo reboot
  ```

### 21.3. Gestores de Procesos y Automatización

- Crear nueva sesión tmux:
  ```bash
  tmux new -s nora
  ```

- Desconectarse de tmux:
  ```bash
  Ctrl+b, luego d
  ```

- Listar sesiones activas:
  ```bash
  tmux ls
  ```

- Reconectar a una sesión tmux existente:
  ```bash
  tmux attach-session -t nora
  ```

- Recargar servicios gestionados por systemd:
  ```bash
  sudo systemctl daemon-reload
  sudo systemctl restart nora.service
  ```

### 21.4. Logs y Diagnóstico

- Visualizar logs en tiempo real:
  ```bash
  sudo journalctl -u nora.service -f
  ```

- Revisar logs antiguos:
  ```bash
  sudo journalctl -u nora.service --since "2 hours ago"
  ```

### 21.5. Backup y Restauración

- Realizar backup de la carpeta de entorno:
  ```bash
  tar -czvf nora_backup_$(date +%F).tar.gz /ruta/al/proyecto
  ```

- Restaurar backup:
  ```bash
  tar -xzvf nora_backup_<fecha>.tar.gz
  ```

### 21.6. Otros Comandos ÚTiles

- Chequear espacio disponible:
  ```bash
  df -h
  ```

- Monitorear temperatura CPU:
  ```bash
  vcgencmd measure_temp
  ```

- Ver uso de memoria RAM:
  ```bash
  free -h
  ```

- Ver procesos activos:
  ```bash
  htop
  ```

- Forzar apagado seguro:
  ```bash
  sudo shutdown now
  ```

- Reiniciar sistema:
  ```bash
  sudo reboot
  ```

