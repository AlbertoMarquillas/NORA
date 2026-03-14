"""
asgi.py

Punto de entrada ASGI del backend de NORA.

Este módulo configura el enrutado de protocolos para servir tanto
peticiones HTTP tradicionales de Django como conexiones WebSocket
gestionadas mediante Django Channels.
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from backend.websocket.routing.backend_routing import websocket_urlpatterns


os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "backend.server.settings.dev",
)

# Aplicación ASGI base de Django para tráfico HTTP.
django_asgi_app = get_asgi_application()

# Router principal de protocolos del backend.
application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AuthMiddlewareStack(
            URLRouter(websocket_urlpatterns)
        ),
    }
)