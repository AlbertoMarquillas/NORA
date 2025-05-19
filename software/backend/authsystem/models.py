# backend/authsystem/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    is_guest = models.BooleanField(default=False)

    def __str__(self):
        return self.username
