from django.urls import reverse

from rest_framework import test
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

from authentication.models import User


class AuthenticationTest(test.APITestCase):

    @classmethod
    def setUpTestData(cls):
        data = {
            'username': 'testUser',
            'password': 'testPassword'
        }

        cls.data = data
        cls.user = User.objects.create_user(**data)
        cls.token_obtain_pair_view_url = reverse('token_obtain_pair')
        cls.token_refresh_view_url = reverse('token_refresh')

    def test_token_obtain_pair_view(self):
        """
        Tests the generation of access and refresh tokens.
        """

        response = self.client.post(self.token_obtain_pair_view_url, data=self.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_token_refresh_view(self):
        """
        Tests the access token refresh using a previous refresh token.
        """

        refresh = RefreshToken.for_user(self.user)

        data = {
            'refresh': str(refresh)
        }

        response = self.client.post(self.token_refresh_view_url, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn('access', response.data)
