# backend/voz/emisor_eventos.py
import requests

def enviar_evento_fsm(evento, descripcion=""):
    """
    Envía un evento FSM al backend Django mediante una petición POST.
    """
    url = "http://localhost:8000/api/evento/"
    payload = {
        "type": "fsm_event",
        "evento": evento,
        "descripcion": descripcion,
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print(f"[FSM] Evento enviado correctamente: {evento}")
        else:
            print(f"[FSM] Error al enviar evento: {response.status_code} → {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"[FSM] Error de conexión: {e}")
