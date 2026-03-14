"""
auth_serializers.py

Serializers relacionados con autenticación y representación básica del usuario
en el backend de NORA.
"""
from __future__ import annotations
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from typing import TYPE_CHECKING

User = get_user_model()

if TYPE_CHECKING:
    from backend.persistence.models.auth_models import User as UserType

INVALID_CREDENTIALS_MESSAGE = "Invalid credentials."


def _get_avatar_url(user: "UserType") -> str | None:
    """
    Devuelve la URL del avatar del usuario si existe.

    Parameters
    ----------
    user : User
        Instancia del usuario autenticado.

    Returns
    -------
    str | None
        URL del avatar si está disponible; en caso contrario, None.
    """
    if hasattr(user, "avatar") and user.avatar:
        return user.avatar.url
    return None


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Serializer JWT personalizado que permite autenticación mediante username
    o email y añade metadatos adicionales del usuario a la respuesta.

    Notes
    -----
    El campo de entrada sigue siendo `username` por compatibilidad con
    `TokenObtainPairView`, pero puede contener tanto el username real como
    el email del usuario.
    """

    def validate(self, attrs: dict) -> dict:
        """
        Valida credenciales de acceso e incorpora datos adicionales del usuario.

        Parameters
        ----------
        attrs : dict
            Diccionario con las credenciales enviadas por el cliente.

        Returns
        -------
        dict
            Payload de respuesta con tokens JWT y metadatos del usuario.

        Raises
        ------
        AuthenticationFailed
            Si el usuario no existe o la contraseña es incorrecta.
        """
        username_or_email = attrs.get("username")
        password = attrs.get("password")

        user = self._get_user_by_username_or_email(username_or_email)

        if user is None or not user.check_password(password):
            raise AuthenticationFailed(INVALID_CREDENTIALS_MESSAGE)

        attrs["username"] = user.username
        data = super().validate(attrs)

        data.update(
            {
                "username": user.username,
                "email": user.email,
                "avatar": _get_avatar_url(user),
                "is_admin": user.is_staff or user.is_superuser,
                "is_guest": getattr(user, "role", "user") == "guest",
            }
        )

        return data

    def _get_user_by_username_or_email(self, username_or_email: str | None) -> "UserType" | None:
        """
        Busca un usuario por email o username.

        Parameters
        ----------
        username_or_email : str | None
            Identificador recibido en el campo `username`.

        Returns
        -------
        User | None
            Usuario encontrado o None si no existe coincidencia.
        """
        if not username_or_email:
            return None

        try:
            return User.objects.get(email=username_or_email)
        except User.DoesNotExist:
            try:
                return User.objects.get(username=username_or_email)
            except User.DoesNotExist:
                return None


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer para registro de nuevos usuarios.
    """

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password", "password2")

    def validate(self, attrs: dict) -> dict:
        """
        Valida la coherencia de las contraseñas introducidas.

        Parameters
        ----------
        attrs : dict
            Datos de entrada del registro.

        Returns
        -------
        dict
            Datos validados.

        Raises
        ------
        serializers.ValidationError
            Si las contraseñas no coinciden.
        """
        password = attrs.get("password")
        password2 = attrs.get("password2")

        if password != password2:
            raise serializers.ValidationError(
                {"password": "Passwords must match."}
            )

        return attrs

    def create(self, validated_data: dict) -> "UserType":
        """
        Crea un nuevo usuario a partir de los datos validados.

        Parameters
        ----------
        validated_data : dict
            Datos validados del serializer.

        Returns
        -------
        User
            Usuario creado.
        """
        validated_data.pop("password2", None)
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer de representación del usuario autenticado.
    """

    is_admin = serializers.SerializerMethodField()
    is_guest = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("username", "email", "avatar", "is_admin", "is_guest")

    def get_is_admin(self, obj: "UserType") -> bool:
        """
        Indica si el usuario tiene privilegios administrativos.

        Parameters
        ----------
        obj : User
            Usuario serializado.

        Returns
        -------
        bool
            True si el usuario es staff o superuser.
        """
        return obj.is_staff or obj.is_superuser

    def get_is_guest(self, obj: "UserType") -> bool:
        """
        Indica si el usuario tiene rol de invitado.

        Parameters
        ----------
        obj : User
            Usuario serializado.

        Returns
        -------
        bool
            True si el rol es guest; False en caso contrario.
        """
        return getattr(obj, "role", "user") == "guest"