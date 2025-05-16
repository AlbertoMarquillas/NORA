from django.urls import path
from .views import recibir_evento_fsm, estado_fsm_actual

urlpatterns = [
    path('evento/', recibir_evento_fsm, name='recibir_evento_fsm'),
    path('estado/', estado_fsm_actual, name='estado_fsm_actual'),
]
