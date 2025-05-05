from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff', 'is_guest', 'date_joined')
    search_fields = ('username', 'email')  # Permite buscar por nombre de usuario o email
