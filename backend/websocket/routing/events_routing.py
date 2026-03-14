"""
events_routing.py

Routing WebSocket para eventos externos del sistema.
"""

from django.urls import re_path

from ..consumers.events_consumers import EventConsumer


websocket_urlpatterns = [

    re_path(
        r"^ws/events/$",
        EventConsumer.as_asgi(),
    ),

]