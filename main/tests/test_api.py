import json
import random
import string
from unittest import TestCase

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_jwt.settings import api_settings


class AccountsTestCase(TestCase):
    """
    Test the View and Serializer.
    Call the reservation method.
    Return: List of the observations.
    """

    def setUp(self):
        user = User.objects.create_user(
            email=f"{''.join(random.choices(string.ascii_lowercase, k=4))}@test.test",
            password=''.join(random.choices(string.ascii_lowercase, k=18)),
            username=''.join(random.choices(string.ascii_lowercase, k=14)),
        )
        user.save()
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        self.token = token

    def test_get_reservations(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        response = client.get(
            '/api/v1/reservation',
            format='json'
        )

        result = json.loads(response.content)
        print(result)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
