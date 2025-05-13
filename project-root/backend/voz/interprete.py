"""
interprete.py

Este módulo intenta interpretar frases libres que no coinciden con frases clave.
Puede devolver acciones conocidas o delegar a un modelo LLM (en el futuro).
"""

from voz.definiciones import LLM_ACTIVO, DEBUG_VOZ


def interpretar_texto(texto: str) -> str:
    """
    Interpreta una frase libre del usuario.

    Args:
        texto (str): Texto ya normalizado.

    Returns:
        str: Respuesta a pronunciar por voz o resultado interpretado.
    """
    if DEBUG_VOZ:
        print(f"🔍 Interpretando frase libre: {texto}")

    # Ejemplo simple de interpretación directa
    if "enciende la luz" in texto:
        return "He encendido la luz."
    elif "abre la puerta" in texto:
        return "Abriendo la puerta principal."
    elif "cuántos grados hay" in texto or "temperatura" in texto:
        return "Hace 22 grados ahora mismo."

    # Delegar al modelo LLM si está activado
    if LLM_ACTIVO:
        return enviar_a_llm(texto)

    return "No estoy segura de cómo ayudarte con eso."


def enviar_a_llm(texto: str) -> str:
    """
    Envia la frase a un LLM para obtener una respuesta.

    Args:
        texto (str): Entrada textual libre.

    Returns:
        str: Respuesta generada por el modelo.
    """
    # ⚠️ Esto es un stub: se sustituirá por conexión real (OpenAI, LLaMA, etc.)
    if DEBUG_VOZ:
        print(f"📡 Derivando al modelo LLM: {texto}")

    return "Estoy pensando... aún no tengo conexión con el modelo de lenguaje."
