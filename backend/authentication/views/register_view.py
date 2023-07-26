from rest_framework import views
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.schemas import AutoSchema
from rest_framework import status

from ..serializers import UserSerializer

from ..models import User

from utils import Utils


class RegisterView(views.APIView):

    serializer_class = UserSerializer
    schema = AutoSchema()

    def post(self, request: Request):

        data = {
            'username': request.POST.get('username'),
            'email': request.POST.get('email'),
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
            'password': ''
        }

        if User.objects.filter(username=data.get('username')):
            return Response({
                'body': 'Já existe um cadastro com esse nome de usuário.'
            }, status=status.HTTP_409_CONFLICT)

        if User.objects.filter(email=data.get('email')):
            return Response({
                'body': 'Já existe um cadastro com esse e-mail.'
            }, status=status.HTTP_409_CONFLICT)

        data['password'] = Utils.create_random_password()

        user_serializer = UserSerializer(data=data)
        if user_serializer.is_valid(raise_exception=True):
            user_serializer.create(user_serializer.validated_data)

            user_serializer_data = user_serializer.data
            user_serializer_data.pop('password')

            return Response(user_serializer_data, status=status.HTTP_201_CREATED)

        return Response({
            'body': 'Erro interno do sistema.'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
