"""
nfc.py – Módulo de adquisición de datos NFC (simulada o física).
"""

def leer_nfc(valor_simulado=None):
    """
    Retorna el UID de la tarjeta NFC leída.
    
    :param valor_simulado: UID simulado recibido desde el frontend
    :return: String con el UID NFC
    """
    if valor_simulado is not None:
        return str(valor_simulado)

    # Aquí iría el código real usando py532lib, serial, etc.
    raise NotImplementedError("Lectura física de NFC no implementada")
