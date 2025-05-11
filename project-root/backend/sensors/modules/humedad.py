"""
humedad.py – Módulo de adquisición de humedad ambiental (simulada o física).
"""

def leer_humedad(valor_simulado=None):
    """
    Retorna el valor de humedad relativa en porcentaje (%).

    :param valor_simulado: Valor numérico simulado (0–100)
    :return: Porcentaje de humedad relativa
    """
    if valor_simulado is not None:
        return float(valor_simulado)

    # Placeholder para sensor real (ej. DHT22)
    raise NotImplementedError("Lectura física de humedad no implementada")
