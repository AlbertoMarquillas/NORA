"""
fsm_routing.py

Routing WebSocket para actualizaciones de la FSM.
"""

from django.urls import re_path

from ..consumers.fsm_consumers import FSMConsumer


websocket_urlpatterns = [

    re_path(
        r"^ws/fsm/$",
        FSMConsumer.as_asgi(),
    ),

]