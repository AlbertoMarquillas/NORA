from django.urls import path
from sensors.views.temperatura import sensor_temperatura
from sensors.views.presencia import sensor_presencia    
from sensors.views.inclinacion import sensor_inclinacion


urlpatterns = [
    path('temperatura/', sensor_temperatura),
    path('presencia/', sensor_presencia),
    path('inclinacion/', sensor_inclinacion),
]
