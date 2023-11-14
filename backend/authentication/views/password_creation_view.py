from rest_framework import views
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.schemas import AutoSchema

from django.shortcuts import get_object_or_404

from ..serializers import PasswordCreationSerializer
from ..models import UserActivationToken, User


class PasswordCreationView(views.APIView):

    serializer_class = PasswordCreationSerializer
    schema = AutoSchema()

    @staticmethod
    def get(request: Request, token: str) -> Response:

        user_activation_token: UserActivationToken = get_object_or_404(UserActivationToken, token=token)

        if user_activation_token.active:
            return Response(status.HTTP_200_OK)

        return Response(status.HTTP_404_NOT_FOUND)

    @staticmethod
    def post(request: Request, token: str) -> Response:

        data = {
            'password': request.data.get('password'),
            'confirm_password': request.data.get('confirm_password')
        }

        user_activation_token: UserActivationToken = UserActivationToken.objects.get(token=token)
        if not user_activation_token.active:
            return Response(status.HTTP_409_CONFLICT)

        serializer: PasswordCreationSerializer = PasswordCreationSerializer(data=data)
        if not serializer.is_valid():

            return Response({
                'message': serializer.errors
            }, status.HTTP_400_BAD_REQUEST)

        user: User = user_activation_token.user

        user_activation_token.active = False
        user_activation_token.save()

        user.set_password(data.get('password'))
        user.save()

        return Response({
            'message': 'Senha alterada com sucesso!'
        }, status.HTTP_200_OK)
