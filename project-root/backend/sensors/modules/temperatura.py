"""
temperatura.py – Módulo de adquisición de temperatura (simulada o física).
"""
from hardware.sensores.mcp9902 import leer_temperatura_mcp9902

def leer_temperatura(valor_simulado=None):
    """
    Retorna la temperatura leída.
    Si se pasa un valor simulado, lo retorna directamente.
    En el futuro, aquí se integrará la lectura desde hardware físico.
    """


    if valor_simulado is not None:
        return valor_simulado
    return leer_temperatura_mcp9902()

