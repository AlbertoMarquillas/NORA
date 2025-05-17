from django.urls import path
from .views import recibir_evento_fsm, estado_fsm_actual

urlpatterns = [
    path("", recibir_evento_fsm),
    path("estado/", estado_fsm_actual),
]
