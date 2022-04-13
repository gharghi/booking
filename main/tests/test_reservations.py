import random
import string
from unittest import TestCase

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_jwt.settings import api_settings

from main.models import Reservation, Rental
from main.services.reservations import get_reservations


class AccountsTestCase(TestCase):
    """
    Test the Model, View and Serializer od reservations.
    """

    def setUp(self):
        self.name = ''.join(random.choices(string.ascii_lowercase, k=10))
        rental = Rental.objects.create(name=self.name)
        self.res1 = Reservation.objects.create(rental=rental, checkin='2021-01-01', checkout='2021-01-10')
        self.res2 = Reservation.objects.create(rental=rental, checkin='2021-01-11', checkout='2021-01-20')

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

    def test_create_reservation(self):
        reservation = Reservation.objects.get(id=self.res1.id)
        self.assertEqual(reservation, self.res1)

    def test_get_reservations(self):
        reservations = get_reservations()
        previous_id = reservations.get(id=self.res2.id).previous_reservation
        self.assertEqual(self.res1.id, previous_id)

    def test_reservations_view(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = client.get(
            '/api/v1/reservation',
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('previous_reservation', response.data[0])
