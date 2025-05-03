# Índice General – Arquitectura de Módulos NORA

## 1. Entrada Sensorial
- `vision/` – Procesamiento de entrada visual, detección facial, gestual y emocional.
- `voz/` – Reconocimiento automático del habla (ASR) y generación de voz (TTS).
- `sensores/` – Adquisición de datos ambientales, de presencia, NFC y Bluetooth.
- `activacion/` – Gestión de activación multisensorial (hotword, NFC, presencia, botón).

## 2. Coordinación Inteligente
- `agentes/` – Evaluación contextual, modulación emocional, coordinación perceptiva y expresiva.

## 3. Núcleo Lógico del Sistema
- `sistema/` – Máquina de estados (FSM), gestión de eventos, control del comportamiento global.

## 4. Expresión y Salida Multimodal
- `interfaz/` – Control de expresión física: pantalla facial, LEDs RGB, servos.
- `voz/` – (también listado en entrada) Síntesis y expresión emocional mediante audio.
- `dialogo/` – Procesamiento de lenguaje natural (NLU/NLG) y generación de respuestas contextuales.

## 5. Persistencia de Datos
- `datos/` – Almacenamiento estructurado de notas, rutinas, emociones, hábitos, historial de usuario.

## 6. Control del Sistema Embebido
- `control/` – Supervisión de hardware, energía, conectividad, protección contra fallos, diagnóstico.

## 7. Interfaz de Usuario
- `gui/` – Panel de control visual, monitorización, configuración dinámica y simulación de interacciones.

## 8. Modelos de Inteligencia Artificial
- `models/` – Gestión de modelos de visión, voz, emociones, hábitos, incluyendo autoactualización y fine-tuning.

## 9. Utilidades Compartidas
- `utils/` – Funciones auxiliares comunes: parsers, logging, eventos, cálculos, validadores, gestión segura.

## 10. Validación y Testing
- `tests/` – Pruebas unitarias, de integración, de estrés, cobertura de código, simulaciones controladas.


# Estructura de Carpetas y Archivos (Árbol)

```
NORA/
│
├── vision/
│   ├── vision_main.py
│   ├── deteccion_rostro.py
│   ├── postura.py
│   ├── atencion_visual.py
│   ├── emociones.py
│   ├── gestos.py
│   ├── signos.py
│   ├── modelo_loader.py
│   ├── eventos_vision.py
│   ├── utils_vision.py
│   ├── config_vision.py
│   ├── pipeline.py
│   ├── tracking.py
│   ├── reconocimiento_usuario.py
│   ├── verificacion_calidad.py
│
├── voz/
│   ├── voz_main.py
│   ├── asr.py
│   ├── tts.py
│   ├── vad.py
│   ├── emocion_audio.py
│   ├── hotword.py
│   ├── parser_comandos.py
│   ├── normalizacion_texto.py
│   ├── perfil_voz_usuario.py
│   ├── entrenamiento_adaptativo.py
│   ├── eventos_voz.py
│   ├── pipeline_audio.py
│   ├── gestion_salida_tts.py
│   ├── variabilidad_prosodica.py
│   ├── interrupcion_semantica.py
│   ├── expresiones_vocales.py
│   ├── motor_personalidad_voz.py
│   ├── optimizacion_tts.py
│   ├── config_voz.py
│   ├── utils_voz.py
│
├── sensores/
│   ├── sensores_main.py
│   ├── sensor_temperatura.py
│   ├── sensor_luminosidad.py
│   ├── sensor_calidad_aire.py
│   ├── sensor_presencia.py
│   ├── sensor_pir.py
│   ├── sensor_imu.py
│   ├── sensor_reloj.py
│   ├── sensor_nfc.py
│   ├── sensor_ble.py
│   ├── sensor_base.py
│   ├── eventos_sensores.py
│   ├── config_sensores.py
│   ├── utils_sensores.py
│
├── activacion/
│   ├── activacion_main.py
│   ├── gestion_nfc.py
│   ├── gestion_presencia.py
│   ├── gestion_atencion.py
│   ├── gestion_hotword.py
│   ├── gestion_boton.py
│   ├── decision_activacion.py
│   ├── registro_fallos.py
│   ├── control_hysteresis.py
│   ├── modo_no_molestar.py
│   ├── eventos_activacion.py
│   ├── config_activacion.py
│   ├── utils_activacion.py
│
├── agentes/
│   ├── agentes_main.py
│   ├── agente_base.py
│   ├── agente_visual.py
│   ├── agente_auditivo.py
│   ├── agente_contexto.py
│   ├── agente_emocional.py
│   ├── agente_priorizacion.py
│   ├── agente_habitos.py
│   ├── agente_seguridad.py
│   ├── agente_confort.py
│   ├── agente_mantenimiento.py
│   ├── agente_adaptativo.py
│   ├── agente_emocion_prioritaria.py
│   ├── escenas_expresivas.py
│   ├── decision_agentes.py
│   ├── config_agentes.py
│   ├── utils_agentes.py
│
├── sistema/
│   ├── sistema_main.py
│   ├── fsm_control.py
│   ├── eventos_sistema.py
│   ├── gestion_eventos.py
│   ├── control_prioridades.py
│   ├── control_emocional.py
│   ├── coordinacion_modular.py
│   ├── monitor_consistencia.py
│   ├── planificador_tareas.py
│   ├── gestion_fallos.py
│   ├── modulacion_estado.py
│   ├── analisis_contextual.py
│   ├── perfil_dinamico_usuario.py
│   ├── config_sistema.py
│   ├── utils_sistema.py
│
├── interfaz/
│   ├── interfaz_main.py
│   ├── pantalla_facial.py
│   ├── leds_rgb.py
│   ├── control_servos.py
│   ├── escenas_expresivas.py
│   ├── animaciones_predefinidas.py
│   ├── modulacion_expresiva.py
│   ├── transiciones_emocionales.py
│   ├── animaciones_reactivas.py
│   ├── motor_expresiones_parametrizadas.py
│   ├── simulador_interfaz.py
│   ├── config_interfaz.py
│   ├── utils_interfaz.py
│
├── dialogo/
│   ├── dialogo_main.py
│   ├── nlu.py
│   ├── nlg.py
│   ├── gestion_contexto.py
│   ├── adaptacion_emocional.py
│   ├── manejo_incertidumbre.py
│   ├── perfil_usuario_dialogo.py
│   ├── memoria_conversacional.py
│   ├── respuestas_predefinidas.py
│   ├── generacion_respuestas_dinamicas.py
│   ├── correccion_asr.py
│   ├── prediccion_intencion.py
│   ├── ajuste_formalidad.py
│   ├── gestion_subcontextos.py
│   ├── motor_historias.py
│   ├── config_dialogo.py
│   ├── utils_dialogo.py
│
├── datos/
│   ├── datos_main.py
│   ├── gestion_notas.py
│   ├── gestion_rutinas.py
│   ├── historial_eventos.py
│   ├── gestion_perfiles.py
│   ├── seguimiento_habitos.py
│   ├── agenda_calendario.py
│   ├── listas_dinamicas.py
│   ├── anotaciones_emocionales.py
│   ├── respaldo_datos.py
│   ├── optimizacion_queries.py
│   ├── gestion_versiones.py
│   ├── analisis_habitos.py
│   ├── gestion_privacidad.py
│   ├── migracion_datos.py
│   ├── busqueda_semantica.py
│   ├── registro_sensorial.py
│   ├── gestion_historial_usuario.py
│   ├── registro_sueno.py
│   ├── gestion_habitos_usuario.py
│   ├── mejora_habitos_ia.py
│   ├── config_datos.py
│   ├── utils_datos.py
│
├── control/
│   ├── control_main.py
│   ├── inicializacion_hardware.py
│   ├── supervision_estado.py
│   ├── gestion_expansor_io.py
│   ├── gestion_wifi_externo.py
│   ├── gestion_energia.py
│   ├── gestion_logs.py
│   ├── diagnostico_automatico.py
│   ├── control_remoto.py
│   ├── proteccion_fallos.py
│   ├── sincronizacion_reloj.py
│   ├── mantenimiento_predictivo.py
│   ├── perfiles_energia_dinamicos.py
│   ├── gestion_desconexion_red.py
│   ├── balanceo_carga.py
│   ├── gestion_alarmas_criticas.py
│   ├── config_control.py
│   ├── utils_control.py
│
├── gui/
│   ├── gui_main.py
│   ├── panel_control.py
│   ├── monitor_eventos.py
│   ├── configuracion_manual.py
│   ├── panel_diagnostico.py
│   ├── gestion_usuarios_gui.py
│   ├── monitor_salud_sistema.py
│   ├── panel_intervenciones.py
│   ├── simulador_interacciones.py
│   ├── servidor_web_gui.py
│   ├── alertas_gui.py
│   ├── historial_eventos_gui.py
│   ├── editor_escenas_gui.py
│   ├── simulador_estados_gui.py
│   ├── dashboard_rendimiento_gui.py
│   ├── utils_gui.py
│
├── models/
│   ├── models_main.py
│   ├── carga_modelos_vision.py
│   ├── carga_modelos_voz.py
│   ├── carga_modelos_gestos.py
│   ├── carga_modelos_emociones.py
│   ├── carga_modelos_habitos.py
│   ├── gestion_embeddings.py
│   ├── gestion_fine_tuning.py
│   ├── validacion_modelos.py
│   ├── optimizacion_inferencia.py
│   ├── seleccion_dinamica_modelos.py
│   ├── actualizacion_remota_modelos.py
│   ├── gestor_versiones_modelos.py
│   ├── autoafinado_modelos.py
│   ├── utils_models.py
│
├── utils/
│   ├── utils_main.py
│   ├── parser_config.py
│   ├── parser_config_jerarquico.py
│   ├── gestion_eventos.py
│   ├── eventos_asincronos.py
│   ├── logger_sistema.py
│   ├── logger_distribuido.py
│   ├── cálculos_matemáticos.py
│   ├── gestion_tiempos.py
│   ├── validadores.py
│   ├── conversion_formatos.py
│   ├── gestion_random.py
│   ├── normalizacion_vectores.py
│   ├── generador_ids_unicos.py
│   ├── gestion_secretos.py
│
├── tests/
│   ├── tests_main.py
│   ├── test_utils.py
│   ├── test_sistema.py
│   ├── test_voz.py
│   ├── test_vision.py
│   ├── test_interfaz.py
│   ├── test_datos.py
│   ├── test_control.py
│   ├── test_agentes.py
│   ├── test_models.py
│   ├── test_gui.py
│   ├── test_sensores.py
│   ├── test_eventos.py
│   ├── tests_stress_load.py
│   ├── tests_coverage_analysis.py
│   ├── utils_tests.py
```

