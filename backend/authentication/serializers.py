from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=24)
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=24)
    last_name = serializers.CharField(max_length=24)
    password = serializers.CharField()

    def create(self, validated_data) -> User:

        return User.objects.create_user(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            password=validated_data.get('password'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            is_active=False
        )
