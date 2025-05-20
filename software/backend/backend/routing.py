from django.urls import re_path
from fsm.consumers import EventoConsumer

websocket_urlpatterns = [
    re_path(r'ws/eventos/$', EventoConsumer.as_asgi()),
]
