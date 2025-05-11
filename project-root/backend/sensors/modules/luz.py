"""
luz.py – Módulo de adquisición de nivel de luz ambiental (simulada o física).
"""

def leer_luz(valor_simulado=None):
    """
    Retorna el valor de luz ambiental medido.

    :param valor_simulado: Valor numérico simulado (0 a 1000 típicamente)
    :return: Nivel de luz en unidades arbitrarias (lux o similar)
    """
    if valor_simulado is not None:
        return float(valor_simulado)

    # Placeholder para sensor real (e.g., BH1750 o TSL2561 por I2C)
    raise NotImplementedError("Lectura física de luz ambiental no implementada")
