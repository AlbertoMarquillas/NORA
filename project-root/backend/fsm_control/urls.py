from django.urls import path
from .views import recibir_evento_fsm

urlpatterns = [
    path('evento/', recibir_evento_fsm, name='recibir_evento_fsm'),
]
