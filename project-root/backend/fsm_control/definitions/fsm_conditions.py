"""
fsm_conditions.py

Este módulo define condiciones adicionales (guard clauses) que restringen
o permiten ciertas transiciones de la FSM del sistema NORA. Cada condición
es una función booleana que evalúa el contexto en tiempo de decisión.

Las condiciones deben ser evaluadas por el FSMController antes de aplicar
una transición, cuando dicha transición tenga una condición explícita asociada.
"""

# Ejemplo de tipo Context: estructura con información relevante del sistema
# que puede ser evaluada por las condiciones.
class FSMContext:
    def __init__(self, sensor_data=None, usuario_presente=False, modulo_audio_operativo=True):
        self.sensor_data = sensor_data or {}
        self.usuario_presente = usuario_presente
        self.modulo_audio_operativo = modulo_audio_operativo

def condicion_usuario_presente(context: FSMContext) -> bool:
    """Permite la transición sólo si hay un usuario presente en el entorno."""
    return context.usuario_presente

def condicion_audio_operativo(context: FSMContext) -> bool:
    """Permite la transición sólo si el canal de audio funciona correctamente."""
    return context.modulo_audio_operativo

def condicion_siempre(context: FSMContext) -> bool:
    """Condición siempre verdadera (transición incondicional)."""
    return True
