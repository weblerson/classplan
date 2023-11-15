from rest_framework import views
from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from django.contrib import auth

from ..serializers import LoginSerializer


class LoginView(views.APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request: Request) -> Response:
        serializer = LoginSerializer(data=self.request.data, context={'request': self.request})

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get('user')

        auth.login(request, user)

        return Response(status=status.HTTP_202_ACCEPTED)
