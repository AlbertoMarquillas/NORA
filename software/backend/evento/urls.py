from django.urls import path
from . import views

urlpatterns = [
    # Por ejemplo:
    path("transiciones/", views.lista_transiciones, name="lista_transiciones"),
]
