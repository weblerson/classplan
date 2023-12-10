from rest_framework import test
from rest_framework.test import APIClient

from authentication.serializers import UserSerializer
from authentication.models import User

from ..models import Space, Task


class TaskTests(test.APITestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.user_data: dict[str, str] = {
            'username': 'testUser',
            'email': 'test@test.com',
            'first_name': 'test',
            'last_name': 'user',
        }

        cls.client: APIClient = APIClient()

    @staticmethod
    def _create_space(data: dict[str, str]) -> Space:
        user_serializer: UserSerializer = UserSerializer(data=data)
        if user_serializer.is_valid():
            user: User = user_serializer.create(user_serializer.data)

            space: Space = Space.objects.get(user=user)

            return space

    def test_if_tasks_are_being_created(self) -> None:
        """
        Tests if tasks are being created and related to a space
        """
        space: Space = self._create_space(self.user_data)
        task: Task = Task(space=space)
        task.save()

        created: Task = Task.objects.get(space=space)

        self.assertIsNotNone(created)
        self.assertIsNotNone(created.space)
