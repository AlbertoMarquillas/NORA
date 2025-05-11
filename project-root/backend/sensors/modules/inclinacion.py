"""
inclinacion.py – Módulo de adquisición de inclinación (simulada o física).
"""

def detectar_inclinacion(valor_simulado=None):
    """
    Retorna True si se detecta inclinación anormal.

    :param valor_simulado: Valor booleano simulado (True/False)
    :return: Booleano que indica si NORA está inclinada
    """
    if valor_simulado is not None:
        return bool(valor_simulado)

    # Placeholder para lectura real de acelerómetro (por I2C)
    raise NotImplementedError("Lectura de inclinación no implementada")
