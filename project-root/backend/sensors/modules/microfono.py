"""
microfono.py – Módulo de detección de entrada vocal (simulada o física).
"""

def detectar_voz(valor_simulado=None):
    """
    Retorna True si se detecta actividad vocal (hotword o comando).

    :param valor_simulado: Valor booleano simulado (True/False)
    :return: Booleano indicando si se detectó voz
    """
    if valor_simulado is not None:
        return bool(valor_simulado)

    # Aquí se integrará con un sistema de hotword (por ejemplo por socket o evento externo)
    raise NotImplementedError("Detección vocal no implementada")
