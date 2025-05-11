"""
evaluadores.py – Evaluación de condiciones sensor→evento para FSM.
"""

def evaluar_evento_temperatura(temperatura, estado_actual=None):
    """
    Determina el evento FSM futuro basado en la temperatura.

    :param temperatura: valor numérico en grados Celsius
    :param estado_actual: estado FSM actual (opcional para condiciones avanzadas)
    :return: evento FSM como string o None si no aplica
    """
    if temperatura > 30:
        return "EVT_CALOR"
    elif temperatura < 18:
        return "EVT_FRIO"
    return None

def evaluar_evento_presencia(presencia, estado_actual=None):
    """
    Determina el evento FSM futuro basado en detección de presencia.

    :param presencia: booleano, True si hay presencia humana
    :param estado_actual: estado FSM actual (opcional)
    :return: evento FSM como string o None si no aplica
    """
    if presencia:
        return "EVT_PRESENCIA"
    return None  # o "EVT_AUSENCIA" si se quiere detectar también ausencia activa

def evaluar_evento_nfc(uid, estado_actual=None):
    """
    Determina el evento FSM a partir del UID NFC leído.

    :param uid: UID leído (string)
    :param estado_actual: estado FSM actual (opcional)
    :return: evento FSM como string o None
    """
    if uid == "ABC123":  # Lista blanca simple; puedes usar una base de datos real
        return "EVT_NFC_VALIDO"
    else:
        return "EVT_NFC_INVALIDO"

def evaluar_evento_microfono(detectado, estado_actual=None):
    """
    Determina el evento FSM a partir de la detección de voz.

    :param detectado: Booleano, True si se ha detectado voz o hotword
    :param estado_actual: Estado FSM actual
    :return: Evento FSM como string o None
    """
    if detectado:
        return "EVT_COMANDO_VOZ"
    return None  # O EVT_SILENCIO si decides manejarlo

def evaluar_evento_luz(nivel_luz, estado_actual=None):
    """
    Determina el evento FSM según el nivel de luz ambiental.

    :param nivel_luz: Valor numérico de luz (lux o equivalente)
    :param estado_actual: Estado FSM actual (opcional)
    :return: Evento FSM o None
    """
    if nivel_luz < 100:
        return "EVT_LUZ_BAJA"
    elif nivel_luz > 800:
        return "EVT_LUZ_ALTA"
    return None

def evaluar_evento_inclinacion(inclinada, estado_actual=None):
    """
    Determina el evento FSM en base a la inclinación.

    :param inclinada: Booleano que indica si hay inclinación detectada
    :param estado_actual: Estado FSM actual (opcional)
    :return: Evento FSM o None
    """
    if inclinada:
        return "EVT_INCLINACION"
    return None

def evaluar_evento_humedad(humedad, estado_actual=None):
    """
    Determina el evento FSM basado en la humedad ambiental.

    :param humedad: Humedad relativa en porcentaje (float)
    :param estado_actual: Estado FSM actual (opcional)
    :return: Evento FSM o None
    """
    if humedad > 80:
        return "EVT_HUMEDAD_ALTA"
    elif humedad < 30:
        return "EVT_HUMEDAD_BAJA"
    return None
