from django.urls import reverse

from rest_framework import test
from rest_framework import status

from authentication.serializers import UserSerializer


class RegisterTests(test.APITestCase):

    @classmethod
    def setUpTestData(cls):
        data = {
            'username': 'testUser',
            'email': 'test@test.com',
            'first_name': 'test',
            'last_name': 'user',
            'password': 'testPassword'
        }

        cls.data = data

    def test_user_creation(self):
        """
        Tests the User model creation
        """

        response = self.client.post(reverse('register_user'), data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        [self.assertIn(key, response.data) for key in self.data.keys()]

    def test_serializer_user_creation(self):
        """
        Tests the User model creation by UserSerializer serializer
        """

        user_serializer: UserSerializer = UserSerializer(data=self.data)
        if user_serializer.is_valid():
            user = user_serializer.create(user_serializer.data)

            self.assertIsNotNone(user)

    def test_user_creation_username_conflict(self):
        """
        Tests the User model creation conflict
        It will test if the correct status code is returned
        when the same username is passed twice
        """

        self.client.post(reverse('register_user'), data=self.data)
        response = self.client.post(reverse('register_user'), data=self.data)

        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
        self.assertIn('body', response.data)

    def test_user_creation_email_conflict(self):
        """
        Tests the User model creation conflict
        It will test if the correct status code is returned
        when the same email is passed twice
        """

        _data = self.data
        _data['username'] = 'anotherTestUser'

        self.client.post(reverse('register_user'), data=self.data)
        response = self.client.post(reverse('register_user'), data=_data)

        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
        self.assertIn('body', response.data)

    def test_username_max_length_validation(self):
        """
        Tests if the validation for username max length is working
        """

        _data = self.data
        _data['username'] = 'tttttttttttttttttttttestUser'

        response = self.client.post(reverse('register_user'), data=_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)

    def test_email_validation(self):
        """
        Tests if the validation for email is working
        """

        _data = self.data
        _data['email'] = 'email'

        response = self.client.post(reverse('register_user'), data=_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

    def test_first_name_max_length_validation(self):
        """
        Tests if the validation for first name max length is working
        """

        _data = self.data
        _data['first_name'] = 'ttttttttttttttttttttttttttttest'

        response = self.client.post(reverse('register_user'), data=_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('first_name', response.data)

    def test_last_name_max_length_validation(self):
        """
        Tests if the validation for first name max length is working
        """

        _data = self.data
        _data['last_name'] = 'uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuser'

        response = self.client.post(reverse('register_user'), data=_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('last_name', response.data)
