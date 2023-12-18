from rest_framework import views
from rest_framework.schemas import AutoSchema
from rest_framework.request import Request
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from rest_framework import status

from ..serializers import TaskUpdateSerializer
from ..models import Space, Task


class TaskUpdateView(views.APIView):

    serializer_class = TaskUpdateSerializer
    schema: AutoSchema = AutoSchema()

    @staticmethod
    def patch(request: Request, space_id: int, task_id: int) -> Response:
        """
        Update, partially, a task
        path: /spaces/<id>/tasks/<id>/
        """

        space: Space = get_object_or_404(Space, id=space_id)
        if request.user != space.user:
            return Response({
                'message': 'Espaço não relacionado ao usuário!'
            }, status=status.HTTP_403_FORBIDDEN)

        task: Task = get_object_or_404(Task, id=task_id)

        try:
            serializer: TaskUpdateSerializer = TaskUpdateSerializer(task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()

                return Response(status=status.HTTP_200_OK)

            return Response(status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response({
                'message': 'Erro interno do sistema',
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
