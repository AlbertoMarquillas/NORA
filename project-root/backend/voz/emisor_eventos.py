"""
emisor_eventos.py

Este módulo permite enviar eventos FSM al backend mediante HTTP POST.
Se utiliza para que el módulo de voz pueda notificar activaciones, desactivaciones,
o cualquier otro evento reconocible.
"""

import requests
import json
from voz.definiciones import DEBUG_VOZ, URL_EVENTO_FSM


def enviar_evento_fsm(evento: str, descripcion: str = "", origen: str = "voz") -> bool:
    """
    Envía un evento FSM al backend.

    Args:
        evento (str): Nombre del evento FSM (por ejemplo: EVT_WAKEWORD).
        descripcion (str): Texto descriptivo del origen del evento.
        origen (str): Módulo que genera el evento (por defecto "voz").

    Returns:
        bool: True si el envío fue exitoso, False en caso de error.
    """
    payload = {
        "type": "fsm_event",
        "evento": evento,
        "descripcion": descripcion,
        "origen": origen,
    }

    try:
        response = requests.post(URL_EVENTO_FSM, json=payload, timeout=3)
        if response.status_code == 200:
            if DEBUG_VOZ:
                print(f"✅ Evento FSM enviado: {evento} - {descripcion}")
            return True
        else:
            if DEBUG_VOZ:
                print(f"⚠️ Error {response.status_code}: {response.text}")
            return False
    except requests.exceptions.RequestException as e:
        if DEBUG_VOZ:
            print(f"❌ Error al conectar con el backend FSM: {e}")
        return False
