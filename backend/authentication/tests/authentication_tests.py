from django.urls import reverse

from rest_framework import test
from rest_framework.test import APIClient
from rest_framework import status

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
        cls.login_url = reverse('login')
        cls.logout_url = reverse('logout')
        cls.auth_status = reverse('auth_status')

        cls.client: APIClient = APIClient()

    def test_session_authentication(self) -> None:
        """
        Tests if user is being authenticated
        """

        self.client.login(**self.data)
        response = self.client.get(self.auth_status)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self) -> None:
        """
        Tests if user is not authenticated
        """

        self.client.login(**self.data)
        response = self.client.get(self.auth_status)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.logout()
        response = self.client.get(self.auth_status)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_if_login_view_is_authenticating_user(self) -> None:
        """
        Tests if the login view is authenticating the user
        """

        self.client.post(self.login_url, data=self.data)
        response = self.client.get(self.auth_status)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_logout_view_is_closing_user_session(self) -> None:
        """
        Tests if the logout view is closing user session
        """

        self.client.post(self.login_url, data=self.data)
        response = self.client.get(self.auth_status)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.get(self.logout_url)
        response = self.client.get(self.auth_status)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
