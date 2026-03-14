"""
prod.py

Configuración específica para producción.
"""

from .base import *


DEBUG = False


ALLOWED_HOSTS = [
    "nora.example.com",
]


# En producción se recomienda Redis para Channels
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [os.getenv("REDIS_URL", "redis://127.0.0.1:6379/0")],
        },
    }
}