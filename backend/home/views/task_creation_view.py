from rest_framework import views
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from rest_framework.schemas import AutoSchema

from ..models import Space
from ..serializers import TaskCreationSerializer


class TaskCreationView(views.APIView):
    serializer_class = TaskCreationSerializer
    schema: AutoSchema = AutoSchema()

    @staticmethod
    def post(request: Request, space_id: int) -> Response:
        """
        Create a task to it's associated space
        path: /spaces/<id>/tasks/
        """

        space: Space = get_object_or_404(Space, id=space_id)
        if space.user != request.user:
            return Response({
                'message': 'Espaço não relacionado ao usuário!'
            }, status=status.HTTP_403_FORBIDDEN)

        request.data._mutable = True
        request.data['space'] = space.id
        request.data._mutable = False

        try:
            serializer: TaskCreationSerializer = TaskCreationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response({
                'message': 'Erro interno do sistema',
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
