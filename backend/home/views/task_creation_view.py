from rest_framework import views
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions

from django.shortcuts import get_object_or_404

from rest_framework.schemas import AutoSchema

from ..models import Space
from ..serializers import TaskSerializer


class TaskCreationView(views.APIView):
    serializer_class = TaskSerializer
    schema: AutoSchema = AutoSchema()

    @staticmethod
    def post(request: Request, space_id: int) -> Response:
        """
        Create a task to it's associated space
        path: /spaces/<id>/tasks/
        """

        task_name: str = request.data.get('task_name')

        space: Space = get_object_or_404(Space, id=space_id)
        if space.user != request.user:
            return Response({
                'message': 'Espaço não relacionado ao usuário!'
            }, status=status.HTTP_403_FORBIDDEN)

        data: dict[str, str | int] = {
            'name': task_name,
            'space': space.id
        }

        try:
            serializer: TaskSerializer = TaskSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)

        except:
            return Response({
                'message': 'Erro interno do sistema',
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
