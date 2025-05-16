"""
procesador.py

Este módulo recibe texto transcrito desde recognizer.py,
lo clasifica y ejecuta la acción correspondiente: emitir eventos FSM,
responder por voz o delegar a un sistema interpretativo (intérprete, LLM, etc.).
"""

import re
from voz.definiciones import (
    FRASES_ACTIVACION,
    FRASES_DESACTIVACION,
    FRASES_REPETICION,
    FRASES_AYUDA,
    EVENTO_ACTIVACION,
    EVENTO_DESACTIVACION,
    EVENTO_REPETICION,
    EVENTO_AYUDA,
    LLM_ACTIVO,
    DEBUG_VOZ
)
from voz.responder import responder_texto, obtener_ultima_respuesta
from voz.emisor_eventos import enviar_evento_fsm
from voz.interprete import interpretar_texto


def normalizar_texto(frase: str) -> str:
    """
    Convierte la frase a minúsculas y elimina signos y dígitos.

    Args:
        frase (str): Texto crudo.

    Returns:
        str: Texto limpio.
    """
    frase = frase.lower()
    frase = re.sub(r'[^a-záéíóúñü\s]', '', frase)
    return frase.strip()


def contiene(frase: str, lista_objetivo: list[str]) -> bool:
    """
    Verifica si la frase contiene alguna frase clave de una lista.

    Args:
        frase (str): Frase normalizada.
        lista_objetivo (list): Lista de frases clave.

    Returns:
        bool: True si hay coincidencia parcial.
    """
    return any(clave in frase for clave in lista_objetivo)


def procesar_frase(frase: str):
    """
    Procesa el texto reconocido y ejecuta la acción correspondiente:
    emitir evento, responder, o enviar al LLM/interprete.

    Args:
        frase (str): Texto transcrito desde voz.
    """
    if not frase:
        return

    frase = normalizar_texto(frase)

    if DEBUG_VOZ:
        print(f"🧠 Procesando frase: {frase}")

    if contiene(frase, FRASES_ACTIVACION):
        enviar_evento_fsm(EVENTO_ACTIVACION, "Activación por frase clave")
        responder_texto("Hola, ¿en qué puedo ayudarte?")

    elif contiene(frase, FRASES_DESACTIVACION):
        enviar_evento_fsm(EVENTO_DESACTIVACION, "Desactivación solicitada")
        responder_texto("Hasta luego.")

    elif contiene(frase, FRASES_REPETICION):
        respuesta = obtener_ultima_respuesta()
        if respuesta:
            responder_texto(respuesta)
        enviar_evento_fsm(EVENTO_REPETICION, "Petición de repetición")

    elif contiene(frase, FRASES_AYUDA):
        responder_texto("¿En qué necesitas ayuda?")
        enviar_evento_fsm(EVENTO_AYUDA, "Petición de asistencia")

    elif LLM_ACTIVO:
        respuesta_llm = interpretar_texto(frase)
        responder_texto(respuesta_llm)

    else:
        responder_texto("Lo siento, no estoy segura de cómo responder eso.")
