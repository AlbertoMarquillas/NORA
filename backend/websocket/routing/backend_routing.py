"""
backend_routing.py

Router principal de WebSockets para el backend de NORA.

Este archivo define todos los endpoints WebSocket del sistema y
conecta cada ruta con su consumer correspondiente.
"""

from django.urls import re_path

from ..consumers.events_consumers import EventConsumer
from ..consumers.fsm_consumers import FSMConsumer


websocket_urlpatterns = [

    # --------------------------------------------------
    # Eventos externos del sistema
    # --------------------------------------------------

    re_path(
        r"^ws/events/$",
        EventConsumer.as_asgi(),
    ),

    # --------------------------------------------------
    # Actualizaciones internas de la FSM
    # --------------------------------------------------

    re_path(
        r"^ws/fsm/$",
        FSMConsumer.as_asgi(),
    ),
]