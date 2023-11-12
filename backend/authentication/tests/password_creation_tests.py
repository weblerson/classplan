from rest_framework import test
from rest_framework import status
from rest_framework.test import APIClient

from django.shortcuts import reverse

from ..models import User, UserActivationToken


class PasswordCreationTests(test.APITestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        data = {
            'username': 'testUser',
            'email': 'test@test.com',
            'first_name': 'test',
            'last_name': 'user',
        }

        password_data = {
            'password': 'testpassword',
            'confirm_password': 'testpassword'
        }

        cls.client: APIClient = APIClient()
        cls.data = data
        cls.password_data = password_data

    def create_user_with_kwargs(self, **kwargs) -> User:

        response = self.client.post(reverse('register_user'), data=kwargs)
        username: str = response.data.get('username')

        return User.objects.get(username=username)

    @staticmethod
    def get_token_by_user(user: User) -> UserActivationToken:

        return UserActivationToken.objects.get(user=user)

    def test_password_creation_url(self) -> None:
        """
        Tests the password creation view
        """

        created_user: User = self.create_user_with_kwargs(**self.data)
        created_user_token: UserActivationToken = PasswordCreationTests.get_token_by_user(created_user)

        response = self.client.get(reverse('password_creation', kwargs={'token': created_user_token.token}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_activation_token_deactivation(self) -> None:
        """
        Tests if the user activation token deactivates when a password is created
        """

        created_user: User = self.create_user_with_kwargs(**self.data)
        created_user_token: UserActivationToken = PasswordCreationTests.get_token_by_user(created_user)

        response = self.client.post(
            reverse('password_creation', kwargs={'token': created_user_token.token}),
            data=self.password_data)

        changed_token: UserActivationToken = PasswordCreationTests.get_token_by_user(created_user)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(changed_token.active)

    def test_if_user_password_changes(self) -> None:
        """
        Tests if user password really changes after created a new password
        """

        created_user: User = self.create_user_with_kwargs(**self.data)
        created_user_token: UserActivationToken = PasswordCreationTests.get_token_by_user(created_user)

        self.client.post(
            reverse('password_creation', kwargs={'token': created_user_token.token}),
            data=self.password_data)

        changed_user = User.objects.get(username=self.data.get('username'))

        self.assertTrue(changed_user.check_password(self.password_data.get('password')))

    def test_if_password_creation_blank_fields_validator_is_working(self) -> None:
        """
        Tests if password creation view's blank field validator is correctly validating
        """

        created_user: User = self.create_user_with_kwargs(**self.data)
        created_user_token: UserActivationToken = PasswordCreationTests.get_token_by_user(created_user)

        datas = [self.password_data.copy() for _ in range(3)]
        data1, data2, data3 = datas

        data1['password'] = ''
        data2['confirm_password'] = ''

        data3['password'] = ''
        data3['confirm_password'] = ''

        responses = list(map(lambda x: self.client.post(
                reverse('password_creation', kwargs={'token': created_user_token.token}),
                data=x), datas))

        list(map(lambda x: self.assertEqual(x.status_code, status.HTTP_400_BAD_REQUEST), responses))
