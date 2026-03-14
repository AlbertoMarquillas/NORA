from django.apps import AppConfig


class BackendConfig(AppConfig):
    """
    Django app configuration for the backend module.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "backend"