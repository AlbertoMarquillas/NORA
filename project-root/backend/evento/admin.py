from django.contrib import admin
from .models import EventoRecibido

@admin.register(EventoRecibido)
class EventoRecibidoAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'evento', 'tipo', 'origen')
    list_filter = ('tipo', 'origen')
    search_fields = ('evento', 'descripcion')
