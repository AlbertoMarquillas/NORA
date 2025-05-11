"""
presencia.py – Módulo de adquisición de presencia (simulada o física).
"""

def detectar_presencia(valor_simulado=None):
    """
    Retorna True si hay presencia detectada, False en caso contrario.

    :param valor_simulado: Valor simulado recibido desde el frontend (True/False)
    :return: Booleano indicando si se detecta presencia
    """
    if valor_simulado is not None:
        return bool(valor_simulado)

    # Placeholder para lectura desde hardware GPIO
    raise NotImplementedError("Lectura de sensor PIR no implementada")
