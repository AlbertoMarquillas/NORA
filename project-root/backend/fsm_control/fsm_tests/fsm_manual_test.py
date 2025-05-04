"""
fsm_manual_test.py

Script de prueba manual para verificar el comportamiento básico de la FSM de NORA.
Simula una secuencia de eventos para observar las transiciones y la lógica de control.
"""

import time
from fsm_control.fsm_controller import FSMController
from fsm_control.definitions.fsm_definitions import FSMEvent
from fsm_control.definitions.fsm_conditions import FSMContext
from fsm_control.fsm_tests.fsm_test_profiles import contexto_normal, contexto_sin_usuario, contexto_audio_caido, contexto_idle_total, contexto_visual_atencion



# Instanciar controlador
fsm = FSMController()

# Actualizar contexto simulado
fsm.actualizar_contexto(contexto_normal)

# Secuencia de prueba: simulamos varios eventos en orden
secuencia_eventos = [
    FSMEvent.EVT_PRESENCE_CONFIRMED,
    FSMEvent.EVT_ATTENTION_CONFIRMED,
    FSMEvent.EVT_SPEECH_START,
    FSMEvent.EVT_SPEECH_RECOGNIZED,
    FSMEvent.EVT_PROCESS_COMPLETED,
    FSMEvent.EVT_IDLE_TIMEOUT,
]

# Enviar eventos a la FSM
for evento in secuencia_eventos:
    print(f"\n[TEST] Enviando evento: {evento.name}")
    fsm.recibir_evento(evento)
    fsm.procesar_siguiente_evento()
    time.sleep(0.5)  # Pausa opcional para legibilidad
