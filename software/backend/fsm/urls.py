from django.urls import path
from .views import recibir_evento_fsm
from .views import recibir_sensor_backend

urlpatterns = [
    path("evento/", recibir_evento_fsm),
    path("sensor/", recibir_sensor_backend),
]
