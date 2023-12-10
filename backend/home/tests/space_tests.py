from rest_framework import test
from rest_framework.test import APIClient

from authentication.serializers import UserSerializer
from authentication.models import User

from ..models import Space


class SpaceTests(test.APITestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.user_data: dict[str, str] = {
            'username': 'testUser',
            'email': 'test@test.com',
            'first_name': 'test',
            'last_name': 'user',
        }

        cls.title: str = 'Filmes, séries etc.'
        cls.objective: str = 'Assistir coisas legais'
        cls.image_url: str = '/media/default/default.jpg'

        cls.client: APIClient = APIClient()

    def test_user_serializer_space_creation(self) -> None:
        """
        Tests if Space is being created when a user is created by UserSerializer
        """
        user_serializer: UserSerializer = UserSerializer(data=self.user_data)
        if user_serializer.is_valid():
            user: User = user_serializer.create(user_serializer.data)

            space: Space = Space.objects.get(user=user)

            self.assertIsNotNone(space)
            self.assertEqual(space.title, self.title)
            self.assertEqual(space.objective, self.objective)
            self.assertEqual(space.image.url, self.image_url)
            self.assertTrue(space.is_personal)
            self.assertTrue(space.is_private)
            self.assertEqual(space.partners.count(), 0)
