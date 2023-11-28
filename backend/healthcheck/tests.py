from django.urls import reverse

from rest_framework import test
from rest_framework import status


class HealthcheckTest(test.APITestCase):

    def test_if_healthcheck_return_200_ok(self):
        url = reverse('healthcheck')

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, 'ok')
