from rest_framework import test

from django.db.models.signals import post_save
from authentication.signals import send_user_email
from authentication.models import User, UserActivationToken


class RegisterSignalTests(test.APITestCase):

    def setUp(self):

        self.data = {
            'username': 'testUser',
            'email': 'test@test.com',
            'first_name': 'test',
            'last_name': 'user'
        }

        post_save.connect(send_user_email, sender=User, dispatch_uid='send_email_user_register')

    def tearDown(self):

        post_save.disconnect(send_user_email, sender=User, dispatch_uid='send_email_user_register')

    def test_send_user_email_on_user_creation(self):
        """
        Tests if the signal is called correctly when an User is created
        """

        user = User.objects.create_user(**self.data)
        user_token = UserActivationToken.objects.get(user=user)

        self.assertIsNotNone(user_token)

    def test_if_user_token_is_active_by_default(self):
        """
        Tests if the user token is active by default
        """

        user = User.objects.create_user(**self.data)
        user_token = UserActivationToken.objects.get(user=user)

        self.assertTrue(user_token.active)
