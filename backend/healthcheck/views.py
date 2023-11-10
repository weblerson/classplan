from rest_framework import views
from rest_framework.response import Response
from rest_framework import status


class HealthcheckView(views.APIView):

    def get(self, request, *args, **kwargs):
        return Response('ok', status=status.HTTP_200_OK)
