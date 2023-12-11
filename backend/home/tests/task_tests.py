from rest_framework import test
from rest_framework.test import APIClient

from authentication.serializers import UserSerializer
from authentication.models import User

from ..models import Space, Task
from ..serializers import TaskSerializer


class TaskTests(test.APITestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.user_data: dict[str, str] = {
            'username': 'testUser',
            'email': 'test@test.com',
            'first_name': 'test',
            'last_name': 'user',
        }

        cls.task_data: dict[str, str] = {
            'name': 'Adv. Movie',
        }

        cls.default_name: str = 'Sem nome'
        cls.default_is_done: bool = False

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
        self.assertEqual(created.name, self.default_name)
        self.assertEqual(created.is_done, self.default_is_done)

        self.assertIsNotNone(created.space)

    def test_if_task_serializer_is_creating_task(self) -> None:
        """
        Tests if tasks are being created and related to a space by a serializer
        """
        space: Space = self._create_space(self.user_data)
        task_data: dict[str, str | int] = self.task_data.copy()

        task_data['space'] = space.id
        serializer: TaskSerializer = TaskSerializer(data=task_data)
        if serializer.is_valid():
            serializer.save()

        task: Task = Task.objects.get(space=space)

        self.assertIsNotNone(task)
        self.assertEqual(task.name, self.task_data.get('name'))
