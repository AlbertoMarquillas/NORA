import os
import django
from channels.routing import get_default_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import evento.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NORA.settings')
django.setup()
application = get_default_application()

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            evento.routing.websocket_urlpatterns
        )
    ),
})
