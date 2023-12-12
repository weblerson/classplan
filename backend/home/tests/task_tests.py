from rest_framework import test
from rest_framework.test import APIClient
from rest_framework.reverse import reverse

from rest_framework import status

from authentication.serializers import UserSerializer
from authentication.models import User

from ..models import Space, Task
from ..serializers import TaskSerializer

Data = dict[str, str]


class TaskTests(test.APITestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        user_data: Data = {
            'username': 'testUser',
            'email': 'test@test.com',
            'first_name': 'test',
            'last_name': 'user',
            'password': 'testPassword'
        }

        alternative_user_data: Data = {
            'username': 'aTestUser',
            'email': 'aTest@test.com',
            'first_name': 'aTest',
            'last_name': 'aUser',
            'password': 'aTestPassword'
        }
        cls.user_data: Data = user_data
        cls.alternative_user_data: Data = alternative_user_data

        cls.user: User = User.objects.create_user(**user_data)
        cls.a_user: User = User.objects.create_user(**alternative_user_data)

        cls.auth_data: Data = {
            'username': user_data.get('username'),
            'password': 'testPassword'
        }

        cls.alternative_auth_data: Data = {
            'username': alternative_user_data.get('username'),
            'password': alternative_user_data.get('password')
        }

        cls.task_data: Data = {
            'task_name': 'Adv. Movie',
        }

        cls.default_name: str = 'Sem nome'
        cls.default_is_done: bool = False

        cls.client: APIClient = APIClient()

    @staticmethod
    def _create_space(user: User) -> Space:
        space: Space = Space(user=user, is_personal=True)
        space.save()

        return Space.objects.get(user=user)

    def _create_and_get_space_and_task(self, user: User, task_data: Data) -> tuple[Space, Task]:
        space: Space = self._create_space(user)
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
        space: Space = self._create_space(self.user)
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
        _, task = self._create_and_get_space_and_task(self.user, self.task_data)

        self.assertIsNotNone(task)
        self.assertEqual(task.name, self.default_name)

    def test_if_task_is_being_deleted_when_its_space_is_deleted(self) -> None:
        """
        Tests if a task is being deleted after it's associated space is deleted
        """
        space, task = self._create_and_get_space_and_task(self.user, self.task_data)

        self.assertIsNotNone(space)
        self.assertIsNotNone(task)

        space.delete()

        deleted_space = Space.objects.filter(id=space.id)
        deleted_task = Task.objects.filter(id=task.id)

        self.assertFalse(deleted_space.exists())
        self.assertFalse(deleted_task.exists())

    def test_if_task_is_being_created_by_api_view(self) -> None:
        """
        Tests if a task is being created by the API View
        """

        space: Space = self._create_space(self.user)
        self.client.login(**self.auth_data)

        task_data: dict[str, str | int] = self.task_data.copy()
        task_data['space'] = space.id

        response = self.client.post(reverse('task_creation', args=[space.id]), data=task_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('name'), self.task_data.get('task_name'))

    def test_if_task_cannot_be_created_on_strangers_space(self) -> None:
        """
        Tests if a task cannot be created on another user's space
        """

        space: Space = self._create_space(self.user)
        self.client.login(**self.alternative_auth_data)

        task_data: dict[str, str | int] = self.task_data.copy()
        task_data['space'] = space.id

        response = self.client.post(reverse('task_creation', args=[space.id]), data=task_data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data.get('message'), 'Espaço não relacionado ao usuário!')
