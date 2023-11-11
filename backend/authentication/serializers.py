from rest_framework import serializers
from .models import User
from .validators import no_whitespace_validator


class UserSerializer(serializers.Serializer):

    username = serializers.CharField(
        max_length=24,
        validators=[no_whitespace_validator]
    )
    email = serializers.EmailField()
    first_name = serializers.CharField(
        max_length=24,
        validators=[no_whitespace_validator]
    )
    last_name = serializers.CharField(
        max_length=24,
        validators=[no_whitespace_validator]
    )
    password = serializers.CharField(required=False)

    def create(self, validated_data) -> User:

        return User.objects.create_user(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            password=validated_data.get('password'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            is_active=False
        )


class PasswordCreationSerializer(serializers.Serializer):

    password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate(self, data: dict[str, str]) -> dict[str, str]:

        if not data.get('password') == data.get('confirm_password'):

            raise serializers.ValidationError('As senhas não coincidem')

        return data
