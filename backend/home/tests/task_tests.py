from rest_framework import test
from rest_framework.test import APIClient

from authentication.serializers import UserSerializer
from authentication.models import User

from ..models import Space, Task
from ..serializers import TaskSerializer

Data = dict[str, str]


class TaskTests(test.APITestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.user_data: Data = {
            'username': 'testUser',
            'email': 'test@test.com',
            'first_name': 'test',
            'last_name': 'user',
        }

        cls.task_data: Data = {
            'name': 'Adv. Movie',
        }

        cls.default_name: str = 'Sem nome'
        cls.default_is_done: bool = False

        cls.client: APIClient = APIClient()

    @staticmethod
    def _create_space(data: Data) -> Space:
        user_serializer: UserSerializer = UserSerializer(data=data)
        if user_serializer.is_valid():
            user: User = user_serializer.create(user_serializer.data)

            space: Space = Space.objects.get(user=user)

            return space

    def _create_and_get_space_and_task(self, user_data: Data, task_data: Data) -> tuple[Space, Task]:
        space: Space = self._create_space(user_data)
        _task_data: dict[str, str | int] = task_data.copy()

        _task_data['space'] = space.id
        serializer: TaskSerializer = TaskSerializer(data=_task_data)
        if serializer.is_valid():
            serializer.save()

        task: Task = Task.objects.get(space=space)

        return space, task

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
        _, task = self._create_and_get_space_and_task(self.user_data, self.task_data)

        self.assertIsNotNone(task)
        self.assertEqual(task.name, self.task_data.get('name'))

    def test_if_task_is_being_deleted_when_its_space_is_deleted(self) -> None:
        """
        Tests if a task is being deleted after it's associated space is deleted
        """
        space, task = self._create_and_get_space_and_task(self.user_data, self.task_data)

        self.assertIsNotNone(space)
        self.assertIsNotNone(task)

        space.delete()

        deleted_space = Space.objects.filter(id=space.id)
        deleted_task = Task.objects.filter(id=task.id)

        self.assertFalse(deleted_space.exists())
        self.assertFalse(deleted_task.exists())
