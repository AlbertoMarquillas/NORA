from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    is_nora_admin = serializers.BooleanField(default=False)  # ← Añadir esta línea

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_guest', 'is_nora_admin']  # ← Añadir is_nora_admin
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    print(f"LoginSerializer: {username}, {password}")  # Debugging line

    def validate(self, data):
        try:
            user = User.objects.get(username=data['email'])
        except User.DoesNotExist:
            raise serializers.ValidationError("Usuario no encontrado")
        
        if not check_password(data['password'], user.password):
            raise serializers.ValidationError("Contraseña incorrecta")
        
        return user
