"""
exceptions.py

Excepciones de la capa de aplicación.
"""


class ApplicationLayerError(Exception):
    """
    Excepción base de la capa de aplicación.
    """


class UnsupportedActionIntentError(ApplicationLayerError):
    """
    Se lanza cuando no existe ejecutor para una intención dada.
    """