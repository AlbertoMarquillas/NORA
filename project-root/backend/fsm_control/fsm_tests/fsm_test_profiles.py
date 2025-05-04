"""
fsm_test_profiles.py

Este módulo define distintos contextos de prueba para simular condiciones
operativas específicas del sistema NORA. Cada perfil representa una configuración
de `FSMContext` con parámetros relevantes, como presencia de usuario, estado
de sensores, estado emocional o fallos técnicos simulados.
"""

from fsm_control.definitions.fsm_conditions import FSMContext

# Perfil base: todos los sistemas funcionando, usuario presente
contexto_normal = FSMContext(
    usuario_presente=True,
    modulo_audio_operativo=True,
    sensor_data={
        "camara": "ok",
        "nfc": "listo",
    }
)

# Usuario ausente, pero todo lo demás en funcionamiento
contexto_sin_usuario = FSMContext(
    usuario_presente=False,
    modulo_audio_operativo=True
)

# Audio no disponible, impide pasar a ESCUCHA
contexto_audio_caido = FSMContext(
    usuario_presente=True,
    modulo_audio_operativo=False
)

# Simulación de entorno silencioso sin interacción humana
contexto_idle_total = FSMContext(
    usuario_presente=False,
    modulo_audio_operativo=False
)

# Contexto personalizado con sensores específicos
contexto_visual_atencion = FSMContext(
    usuario_presente=True,
    modulo_audio_operativo=True,
    sensor_data={
        "camara": "atencion_visual_detectada",
        "nfc": "sin_dato"
    }
)
