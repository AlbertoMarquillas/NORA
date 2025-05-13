from django.urls import path
from . import views
from .views import listar_eventos, recibir_evento_fsm

urlpatterns = [
    path("listar/", listar_eventos),
    path("evento/", recibir_evento_fsm),
]
