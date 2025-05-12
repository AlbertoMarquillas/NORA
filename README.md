# NORA – Instrucciones para lanzar el sistema

Este proyecto contiene el frontend (React + Vite) y el backend (Django) del asistente inteligente NORA. A continuación se detallan los pasos para ejecutar ambos entornos, tanto desde **Windows** como desde **Linux (Debian o VM VirtualBox)**.

---

## 📦 Requisitos generales

* Node.js 18+ y npm ([https://nodejs.org](https://nodejs.org))
* Python 3.10+ con `pip` y `venv`
* Git
* VirtualBox (si se usa Linux en VM)
* Clave SSH configurada en GitHub (si se clona por SSH)

---

## 🔯 Estructura esperada del proyecto

```
project-root/
├── backend/
│   └── manage.py
├── frontend/
│   └── package.json
├── run_back_linux.sh
├── run_front_linux.sh
├── run_backend.ps1
├── run_frontend.ps1
```

---

# 🧪 Lanzar el proyecto en entorno de desarrollo

## 🔹 A. Desde **Linux (Debian o VM)**

### ✅ 1. Clonar el repositorio

```bash
git clone git@github.com:AlbertoMarquillas/NORA.git nora-dev
cd nora-dev
```

### ✅ 2. Configurar y lanzar el backend

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cd backend
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
```

### ✅ 3. Lanzar el frontend

```bash
cd frontend
npm install
npm run dev
```

> Asegúrate de que `frontend/.env.local` contenga:
>
> ```env
> VITE_API_URL=http://<ip-de-la-vm>:8000/api
> ```
>
> Puedes obtener la IP con:
>
> ```bash
> ip a
> ```

---

## 🔾 B. Desde **Windows**

### ✅ 1. Backend (PowerShell)

```powershell
cd project-root
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

cd backend
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

> Si usas VM para el backend, asegúrate de incluir la IP de la VM en `ALLOWED_HOSTS` en `settings.py`

---

### ✅ 2. Frontend (PowerShell)

```powershell
cd project-root\frontend
npm install
npm run dev
```

> Crea el archivo `frontend/.env.local` con:
>
> ```env
> VITE_API_URL=http://localhost:8000/api
> ```
>
> o usa la IP de la VM si el backend corre en Linux:
>
> ```env
> VITE_API_URL=http://192.168.1.46:8000/api
> ```

---

## 🌐 Acceso desde navegador

* Frontend: [http://localhost:5173](http://localhost:5173)
* Backend API: [http://localhost:8000/api/](http://localhost:8000/api/)

---

## ✅ Scripts automáticos disponibles

* `run_front_linux.sh` – Inicia el frontend en Linux
* `run_back_linux.sh` – Inicia el backend en Linux
* `run_frontend.ps1` – Inicia el frontend en Windows (PowerShell)
* `run_backend.ps1` – Inicia el backend en Windows (PowerShell)

---

## 🪡 Notas finales

* El backend usa Django con autenticación JWT y FSM
* El frontend debe apuntar al mismo host/IP donde corre el backend
* Usa `.env.local` en React/Vite para conectar correctamente con el backend
* Para evitar errores de red, comprueba que la VM está en modo puente y la IP es accesible desde Windows

```bash
NORA-main/
    NORA-main/
        .gitignore
        docs/
            00_diseno_arquitectonico/
                00_esquema_general/
                    00_bloques_hardware.md
                    01_bloques_software.md
                    02_relaciones_hw_sw.md
                    03_boceto_estructura_general.md
                    04_diagrama.md
                    05_conexiones_funcionales.md
                    06_interaccion_con_usuario.md
                01_datasheets/
                    204-15UTC-S400-X9.PDF
                    2056179.pdf
                    CCS811_Datasheet-DS000459.pdf
                    ESP8266.PDF
                    HC-05.PDF
                    HC-SR04.pdf
                    MG90S_Tower-Pro.pdf
                    NodeMCUV3.pdf
                    PAM8403.pdf
                    PN532_C1.pdf
                    RPiCamMod2.pdf
                    SA400S37_latam.pdf
                    SG90-datasheet.pdf
                    SPKM.36.8.B.pdf
                    SSD1306.pdf
                    ST7735.pdf
                    TLDR5800.pdf
                    WS2812B.pdf
                    barracuda-ds1737-1-1111us.pdf
                    bst-bme280-ds002.pdf
                    ds3231.pdf
                    pcf8574.pdf
                    raspberry-pi-4-datasheet.pdf
                    sp-1305-v1-1-xs-lav-usb-c-en.pdf
                    tsl2561-932888.pdf
                    upload-5mm_RGB_led_common_cathode.pdf
                02_fichas_modulos/
                    indice.md
                    00_Vision/
                        00_vision.md
                        Archivos/
                            00_vision_main.md
                            01_deteccion_rostro.md
                            02_postura.md
                            03_atencion_visual.md
                            04_emociones.md
                            05_gestos.md
                            06_signos.md
                            07_modelo_loader.md
                            08_eventos_vision.md
                            09_utils_vision.md
                            10_config_vision.md
                            11_pipeline.md
                            12_tracking.md
                            13_reconocimiento_usuario.md
                            14_verificacion_calidad.md
                    01_Voz/
                        01_voz.md
                        Archivos/
                            00_voz_main.md
                            01_asr.md
                            02_tts.md
                            03_vad.md
                            04_emocion_audio.md
                            05_hotword.md
                            06_parser_comandos.md
                            07_eventos_voz.md
                            08_utils_voz.md
                            09_config_voz.md
                            10_modelo_asr_loader.md
                            11_pipeline_audio.md
                            12_normalizacion_texto.md
                            13_perfil_voz_usuario.md
                            14_entrenamiento_adaptativo.md
                            15_gestion_salida_tts.md
                            16_variabilidad_prosodica.md
                            17_interrupcion_semantica.md
                            18_expresiones_vocales.md
                            19_motor_personalidad_voz.md
                            20_optimizacion_tts.md
                    02_Sensores/
                        02_sensores.md
                        Archivos/
                            00_sensores_main.md
                            01_sensor_temperatura.md
                            02_sensor_luminosidad.md
                            03_sensor_calidad_aire.md
                            04_sensor_presencia.md
                            05_sensor_pir.md
                            06_sensor_imu.md
                            07_sensor_reloj.md
                            08_sensor_nfc.md
                            09_sensor_ble.md
                            10_sensor_base.md
                            11_eventos_sensores.md
                            12_config_sensores.md
                            13_utils_sensores.md
                    03_Activacion/
                        03_activacion.md
                        Archivos/
                            00_activacion_main.md
                            01_gestion_nfc.md
                            02_gestion_presencia.md
                            03_gestion_atencion.md
                            04_gestion_hotword.md
                            05_gestion_boton.md
                            06_decision_activacion.md
                            07_registro_fallos.md
                            08_control_hysteresis.md
                            09_modo_no_molestar.md
                            10_eventos_activacion.md
                            11_config_activacion.md
                            12_utils_activacion.md
                    04_Agentes/
                        04_agentes.md
                        Archivos/
                            00_agentes_main.md
                            01_agente_base.md
                            02_agente_visual.md
                            03_agente_auditivo.md
                            04_agente_contexto.md
                            05_agente_emocional.md
                            06_agente_priorizacion.md
                            07_agente_habitos.md
                            08_agente_seguridad.md
                            09_agente_confort.md
                            10_agente_mantenimiento.md
                            11_agente_adaptativo.md
                            12_agente_emocion_prioritaria.md
                            13_escenas_expresivas.md
                            14_decision_agentes.md
                            15_config_agentes.md
                            16_utils_agentes.md
                    05_Sistema/
                        05_sistema.md
                        Archivos/
                            00_sistema_main.md
                            01_fsm_control.md
                            02_eventos_sistema.md
                            03_gestion_eventos.md
                            04_control_prioridades.md
                            05_control_emocional.md
                            06_coordinacion_modular.md
                            07_monitor_consistencia.md
                            08_planificador_tareas.md
                            09_gestion_fallos.md
                            10_modulacion_estado.md
                            11_analisis_contextual.md
                            12_perfil_dinamico_usuario.md
                            13_config_sistema.md
                            14_utils_sistema.md
                    06_Interfaz/
                        06_interfaz.md
                        Archivos/
                            00_interfaz_main.md
                            01_pantalla_facial.md
                            02_leds_rgb.md
                            03_control_servos.md
                            04_escenas_expresivas.md
                            05_animaciones_predefinidas.md
                            06_modulacion_expresiva.md
                            07_transiciones_emocionales.md
                            08_animaciones_reactivas.md
                            09_motor_expresiones_parametrizadas.md
                            10_simulador_interfaz.md
                            11_config_interfaz.md
                            12_utils_interfaz.md
                    07_Dialogo/
                        07_dialogo.md
                        Archivos/
                            00_dialogo_main.md
                            01_nlu.md
                            02_nlg.md
                            03_gestion_contexto.md
                            04_adaptacion_emocional.md
                            05_manejo_incertidumbre.md
                            06_perfil_usuario_dialogo.md
                            07_memoria_conversacional.md
                            08_respuestas_predefinidas.md
                            09_generacion_respuestas_dinamicas.md
                            10_correccion_asr.md
                            11_prediccion_intencion.md
                            12_ajuste_formalidad.md
                            13_gestion_subcontextos.md
                            14_motor_historias.md
                            15_config_dialogo.md
                            16_utils_dialogo.md
                    08_Datos/
                        08_datos.md
                        Archivos/
                            00_datos_main.md
                            01_gestion_notas.md
                            02_gestion_rutinas.md
                            03_historial_eventos.md
                            04_gestion_perfiles.md
                            05_seguimiento_habitos.md
                            06_agenda_calendario.md
                            07_listas_dinamicas.md
                            08_anotaciones_emocionales.md
                            09_respaldo_datos.md
                            10_optimizacion_queries.md
                            11_gestion_versiones.md
                            12_analisis_habitos.md
                            13_gestion_privacidad.md
                            14_migracion_datos.md
                            15_busqueda_semantica.md
                            16_registro_sensorial.md
                            17_gestion_historial_usuario.md
                            18_registro_sueno.md
                            19_gestion_habitos_usuario.md
                            20_mejora_habitos_ia.md
                            21_config_datos.md
                            22_utils_datos.md
                    09_Control/
                        09_control.md
                        Archivos/
                            00_control_main.md
                            01_inicializacion_hardware.md
                            02_supervision_estado.md
                            03_gestion_expansor_io.md
                            04_gestion_wifi_externo.md
                            05_gestion_energia.md
                            06_gestion_logs.md
                            07_diagnostico_automatico.md
                            08_control_remoto.md
                            09_proteccion_fallos.md
                            10_sincronizacion_reloj.md
                            11_mantenimiento_predictivo.md
                            12_perfiles_energia_dinamicos.md
                            13_gestion_desconexion_red.md
                            14_balanceo_carga.md
                            15_gestion_alarmas_criticas.md
                            16_config_control.md
                            17_utils_control.md
                    10_GUI/
                        10_gui.md
                        Archivos/
                            00_gui_main.md
                            01_panel_control.md
                            02_monitor_eventos.md
                            03_configuracion_manual.md
                            04_panel_diagnostico.md
                            05_gestion_usuarios_gui.md
                            06_monitor_salud_sistema.md
                            07_panel_intervenciones.md
                            08_simulador_interacciones.md
                            09_servidor_web_gui.md
                            10_alertas_gui.md
                            11_historial_eventos_gui.md
                            12_editor_escenas_gui.md
                            13_simulador_estados_gui.md
                            14_dashboard_rendimiento_gui.md
                            15_utils_gui.md
                    11_Models/
                        11_models.md
                        Archivos/
                            00_models_main.md
                            01_carga_modelos_vision.md
                            02_carga_modelos_voz.md
                            03_carga_modelos_gestos.md
                            04_carga_modelos_emociones.md
                            05_carga_modelos_habitos.md
                            06_gestion_embeddings.md
                            07_gestion_fine_tuning.md
                            08_validacion_modelos.md
                            09_optimizacion_inferencia.md
                            10_seleccion_dinamica_modelos.md
                            11_actualizacion_remota_modelos.md
                            12_gestor_versiones_modelos.md
                            13_autoafinado_modelos.md
                            14_utils_models.md
                    12_Utils/
                        12_utils.md
                        Archivos/
                            00_utils_main.md
                            01_parser_config.md
                            02_parser_config_jerarquico.md
                            03_gestion_eventos.md
                            04_eventos_asincronos.md
                            05_logger_sistema.md
                            06_logger_distribuido.md
                            07_calculos_matematicos.md
                            08_gestion_tiempos.md
                            09_validadores.md
                            10_conversion_formatos.md
                            11_gestion_random.md
                            12_normalizacion_vectores.md
                            13_generador_ids_unicos.md
                            14_gestion_secretos.md
                    13_Tests/
                        13_tests.md
                        Archivos/
                            00_tests_main.md
                            01_test_utils.md
                            02_test_sistema.md
                            03_test_voz.md
                            04_test_vision.md
                            05_test_interfaz.md
                            06_test_datos.md
                            07_test_control.md
                            08_test_agentes.md
                            09_test_models.md
                            10_test_gui.md
                            11_test_sensores.md
                            12_test_eventos.md
                            13_tests_stress_load.md
                            14_tests_coverage_analysis.md
                            15_utils_tests.md
                03_tecnologias/
                    00_tecnologias_utilizadas.md
                    01_entorno_de_desarrollo.md
                diagramas/
                    diagrama_nora_conceptual.pdf
                    diagrama_nora_conceptual.png
                    diagrama_nora_funcional.pdf
                    diagrama_nora_funcional.png
                fotos/
                    Boceto.png
            01_arquitectura_fisica/
                00_pinout_raspberry.md
                01_lista_gpio_componentes.md
                02_cambio_de_pantalla.md
                03_funcionamiento_SSD1306_SPI.md
                04_migracion_a_pbv.md
                esquema_gpio_nora.drawio
                Esquema Eléctrico/
                    Backup Of Nora.pdsbak
                    Last Loaded Nora.pdsbak
                    Nora.PDF
                    Nora.SVG
                    Nora.pdsprj
                    Nora.pdsprj.DESKTOP-JU6ESO9.alberto.workspace
                    Modulos/
                        00_Entrada_potencia.md
                        01_Ultrasonidos.md
                        02_Boton.md
                        03_Luminosidad.md
                        05_Servomotores.md
                        06_Temperatura.md
                        07_Microfono.md
                        08_RTC.md
                        09_Bluetooth.md
                        10_Altavoz.md
                        11_Pantalla.md
                        12_NFC.md
                        13_Camara.md
                        14_Raspberry.md
                        15_almacenamiento.md
                    NORA/
                        NORA.kicad_pcb
                        NORA.kicad_prl
                        NORA.kicad_pro
                        NORA.kicad_sch
                        fp-info-cache
                    Project Backups/
                        Nora [20250503, 21-58-23].pdsprj
                        Nora [Autosaved].pdsprj
                Fotos/
                    MG90.jpg
                    NFC.jpg
                    SSD1306.jpg
                    WS2812 .jpg
                    pinout.jpg
                    raspberri_pi_b_pinout.jpg
                Project Backups/
                    NORA_schematic [20250430, 17-53-07].pdsprj
                    NORA_schematic [Autosaved].pdsprj
            02_interaccion/
                00_tipos.md
                01_flujo_global_interaccion.md
                02_validacion_flujos.md
                01_activacion/
                    00_descripcion.md
                    01_ejemplos_visuales.md
                    02_flujos.md
                    03_sensores_y_eventos.md
                    04_privacidad.md
                    05_estructura_datos.md
                    06_informacion_personal.md
                    07_flujo_activacion_nfc.md
                02_verbal/
                    00_descripcion.md
                    01_comandos_soportados.md
                    02_flujo_dialogo.md
                    03_integracion_voz.md
                    04_flujo_interaccion_voz.md
                03_visual/
                    00_descripcion.md
                    01_procesamiento_visual.md
                    02_orientacion_fisica.md
                    03_pruebas_camara.md
                    04_flujo_deteccion_visual.md
                04_contexto/
                    00_descripcion.md
                    01_sensores_ambientales.md
                    02_condiciones_disparo.md
                    03_respuestas_contextuales.md
                05_info_personal/
                    00_descripcion.md
                    01_interfaz_gestion.md
                    02_configuracion_usuario.md
                    03_estructura_datos.md
                    04_privacidad.md
                    05_flujo_registro_nota.md
                06_autonomas/
                    00_descripcion.md
                    01_temporizadores.md
                    02_estado_sistema.md
                    03_gestion_fallos.md
                    04_flujo_ausencia_usuario.md
                    05_flujo_error_sistema.md
                07_escrita_gui/
                    00_descripcion.md
                    01_diseño_interfaz.md
                    02_gestion_usuarios.md
                    03_flujo_texto_comando.md
                    04_equivalencias_voz.md
                08_tactil/
                    00_descripcion.md
                    01_hardware_tacto.md
                    02_patrones_interaccion.md
                    03_ideas_expresion.md
                09_remota/
                    00_descripcion.md
                    01_protocolos.md
                    02_control_remoto.md
                    03_seguridad_conexion.md
                10_fisica/
                    00_descripcion.md
                    01_sensores_imu.md
                    02_respuestas_fisicas.md
                    03_pruebas_contacto.md
            03_arquitectura_logica/
                00_plantilla_estado_fsm.md
                01_fsm_transiciones.md
                02_fsm_prioridades.md
                03_estados/
                    Activado/
                        00_descripcion.md
                        01_condiciones_entrada.md
                        02_acciones.md
                        03_condiciones_salida.md
                        04_transiciones.md
                    Atencion/
                        00_descripcion.md
                        01_condiciones_entrada.md
                        02_acciones.md
                        03_condiciones_salida.md
                        04_transiciones.md
                    Error/
                        00_descripcion.md
                        01_condiciones_entrada.md
                        02_acciones.md
                        03_condiciones_salida.md
                        04_transiciones.md
                    Escucha/
                        00_descripcion.md
                        01_condiciones_entrada.md
                        02_acciones.md
                        03_condiciones_salida.md
                        04_transiciones.md
                    Procesando/
                        00_descripcion.md
                        01_condiciones_entrada.md
                        02_acciones.md
                        03_condiciones_salida.md
                        04_transiciones.md
                    Reposo/
                        00_descripcion.md
                        01_condiciones_entrada.md
                        02_acciones.md
                        03_condiciones_salida.md
                        04_transiciones.md
                04_protocolos/
                    00_activacion_nfc/
                        00_especificacion_general.md
                        01_activacion_reposo.md
                        02_desactivacion_activado.md
                        03_validacion_uid.md
                        04_salida_multimodal_activacion.md
                        05_salida_multimodal_desactivacion.md
                        06_prevencion_errores.md
                05_datos/
                    almacenamiento_local/
                        00_estructura_general.md
                        01_plantilla_documentacion_tabla.md
                        02_tabla_notas.md
                        03_tabla_recordatorios.md
                        04_tabla_eventos.md
                        05_tabla_uids.md
                        06_tabla_configuracion.md
                        07_relaciones_integridad.md
                        08_interacciones.md
                        09_respuestas_generadas.md
                        10_usuarios.md
                        11_sensores_log.md
                        12_alarmas.md
                        13_privacidad.md
                        14_estado_sistema.md

```