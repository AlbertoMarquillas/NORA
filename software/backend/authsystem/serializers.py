from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed

User = get_user_model()

# -- Login con email o username --
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        username_or_email = attrs.get("username")
        password = attrs.get("password")

        # Buscar usuario por email o username
        try:
            user = User.objects.get(email=username_or_email)
        except User.DoesNotExist:
            try:
                user = User.objects.get(username=username_or_email)
            except User.DoesNotExist:
                raise AuthenticationFailed("Invalid credentials")

        if not user.check_password(password):
            raise AuthenticationFailed("Invalid credentials")

        # 🛠️ ¡FALTA ESTO!
        self.user = user

        # Esta llamada requiere self.user definido
        data = super().validate(attrs)

        data.update({
            "username": user.username,
            "email": user.email,
            "avatar": user.avatar.url if hasattr(user, "avatar") and user.avatar else None,
            "is_admin": user.is_staff or user.is_superuser,
            "is_guest": getattr(user, "role", "user") == "guest"
        })

        return data

# -- Registro --
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords must match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        return User.objects.create_user(**validated_data)

# -- Perfil del usuario autenticado --
class UserSerializer(serializers.ModelSerializer):
    is_admin = serializers.SerializerMethodField()
    is_guest = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('username', 'email', 'avatar', 'is_admin', 'is_guest')

    def get_is_admin(self, obj):
        return obj.is_staff or obj.is_superuser

    def get_is_guest(self, obj):
        return getattr(obj, "role", "user") == "guest"
