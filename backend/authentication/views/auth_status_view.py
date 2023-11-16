from rest_framework import views
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import permissions

from ..models import User


class AuthStatusView(views.APIView):

    permission_classes = [permissions.AllowAny]

    @staticmethod
    def get(request: Request) -> Response:
        user: User = request.user

        if user.is_authenticated:
            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_401_UNAUTHORIZED)
