from rest_framework import views
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from django.contrib import auth


class LogoutView(views.APIView):

    @staticmethod
    def get(request: Request) -> Response:
        if request.user.is_authenticated:
            auth.logout(request)

            return Response(status=status.HTTP_200_OK)
