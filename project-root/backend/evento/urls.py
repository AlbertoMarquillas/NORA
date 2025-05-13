from django.urls import path
from . import views

urlpatterns = [
    path("listar/", listar_eventos),
    path("evento/", recibir_evento_fsm),
]
