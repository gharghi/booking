import string
import random
from unittest import TestCase

from main.models import Rental, Reservation


class ModelTestCase(TestCase):
    def setUp(self):
        self.name = ''.join(random.choices(string.ascii_lowercase, k=10))
        rental = Rental.objects.create(name=self.name)
        self.res1 = Reservation.objects.create(rental=rental, checkin='2021-01-01', checkout='2021-01-10')
        self.res2 = Reservation.objects.create(rental=rental, checkin='2021-01-11', checkout='2021-01-20')

    def test_previous_reservation(self):
        reservation = Reservation.objects.get(id=self.res2.id)
        self.assertEqual(reservation.previous(), self.res1.id)

