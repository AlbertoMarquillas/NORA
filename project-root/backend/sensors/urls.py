from django.urls import path
from sensors.views.temperatura import sensor_temperatura
from sensors.views.presencia import sensor_presencia    
from sensors.views.inclinacion import sensor_inclinacion
from sensors.views.nfc import sensor_nfc
from sensors.views.microfono import sensor_microfono
from sensors.views.luz import sensor_luz
from sensors.views.humedad import sensor_humedad


urlpatterns = [
    path('temperatura/', sensor_temperatura),
    path('presencia/', sensor_presencia),
    path('inclinacion/', sensor_inclinacion),
    path('nfc/', sensor_nfc),
    path('microfono/', sensor_microfono),
    path('luz/', sensor_luz),
    path('humedad/', sensor_humedad),
]
