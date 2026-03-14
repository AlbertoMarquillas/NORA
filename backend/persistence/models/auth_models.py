"""
auth_models.py

Modelos de persistencia relacionados con autenticación y usuario
del sistema NORA.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Modelo de usuario personalizado del sistema NORA.

    Extiende `AbstractUser` para añadir campos específicos del proyecto.

    Attributes
    ----------
    email : models.EmailField
        Dirección de correo electrónico única del usuario.
    avatar : models.ImageField
        Imagen de perfil opcional del usuario.
    is_guest : models.BooleanField
        Indica si el usuario tiene condición de invitado.
    """

    email = models.EmailField(unique=True)
    avatar = models.ImageField(
        upload_to="avatars/",
        null=True,
        blank=True,
    )
    is_guest = models.BooleanField(default=False)

    def __str__(self) -> str:
        """
        Devuelve una representación legible del usuario.

        Returns
        -------
        str
            Username del usuario.
        """
        return self.username