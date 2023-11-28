from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions


class HealthcheckView(views.APIView):

    permission_classes = [permissions.AllowAny]

    @staticmethod
    def get(request, *args, **kwargs):
        return Response('ok', status=status.HTTP_200_OK)
