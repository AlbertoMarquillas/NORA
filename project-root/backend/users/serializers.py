from rest_framework import serializers
from django.contrib.auth import authenticate
from users.models import User


from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_guest']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Verifica si el email ya existe
        if User.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError("Este email ya está registrado.")

        # Verifica si el nombre de usuario ya existe
        if User.objects.filter(username=validated_data['username']).exists():
            raise serializers.ValidationError("Este nombre de usuario ya está registrado.")

        return User.objects.create_user(**validated_data)



class LoginSerializer(serializers.Serializer):
    """
    Serializer para iniciar sesión. Requiere email y password.
    """
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Credenciales inválidas")


class GuestLoginSerializer(serializers.Serializer):
    """
    Serializer para iniciar sesión como invitado (sin contraseña).
    Solo requiere un nombre de usuario.
    """
    username = serializers.CharField()

    def validate(self, data):
        username = data.get("username")
        if not username:
            raise serializers.ValidationError("Se requiere un nombre de usuario")
        
        # Buscar si ya existe un usuario invitado con ese username
        user = User.objects.filter(username=username, is_guest=True).first()
        if not user:
            # Crear nuevo usuario invitado
            user = User.objects.create_user(
                email=f"{username}@guest.local",
                username=username,
                password=None,
                is_guest=True
            )
            user.set_unusable_password()
            user.save()
        return user
