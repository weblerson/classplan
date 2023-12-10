from rest_framework import serializers
from .models import User
from .validators import no_whitespace_validator

from django.contrib import auth

from home.models import Space


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

        user: User = User.objects.create_user(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            password=validated_data.get('password'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            is_active=False
        )

        # Trocar para serializer
        space: Space = Space(user=user, is_personal=True)
        space.save()

        return user


class PasswordCreationSerializer(serializers.Serializer):

    password = serializers.CharField(required=True, validators=[no_whitespace_validator])
    confirm_password = serializers.CharField(required=True, validators=[no_whitespace_validator])

    def validate(self, data: dict[str, str]) -> dict[str, str]:

        if not data.get('password') == data.get('confirm_password'):

            raise serializers.ValidationError('As senhas não coincidem')

        return data


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField(label='username', write_only=True)
    password = serializers.CharField(
        label='password',
        style={'input_type': 'password'},
        trim_whitespace=True,
        write_only=True,
        validators=[no_whitespace_validator]
    )

    def validate(self, data: dict[str, str]) -> dict[str, str]:
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = auth.authenticate(request=self.context.get('request'), username=username, password=password)

            if not user:
                msg = 'Acesso negado!'
                raise serializers.ValidationError(msg, code='authorization')

        else:
            msg = 'Preencha todos os campos!'
            raise serializers.ValidationError(msg, code='authorization')

        data['user'] = user
        return data
