import string
import random
from unittest import TestCase

from main.models import Rental, Reservation


class ModelTestCase(TestCase):
    """
    Test the database connection and models.
    Creates an object.
    """
    def setUp(self):
        self.name = ''.join(random.choices(string.ascii_lowercase, k=10))
        rental = Rental.objects.create(name=self.name)
        self.res1 = Reservation.objects.create(rental=rental, checkin='2021-01-01', checkout='2021-01-10')

    def test_create_object(self):
        reservation = Reservation.objects.get(id=self.res1.id)
        self.assertEqual(reservation, self.res1)

