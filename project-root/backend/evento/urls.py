from django.urls import path
from . import views
from .views import listar_eventos, recibir_evento_fsm, estado_fsm_actual

urlpatterns = [
    path("listar/", listar_eventos),
    path("evento/", recibir_evento_fsm),
    path("estado/", estado_fsm_actual),
]
