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
