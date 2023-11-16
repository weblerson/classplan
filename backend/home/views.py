from rest_framework import views
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status


class HomeView(views.APIView):

    @staticmethod
    def get(request: Request) -> Response:
        return Response({
            'username': request.user.get_username()
        }, status=status.HTTP_200_OK)
