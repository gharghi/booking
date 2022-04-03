from django.db import models

from main.models import Rental


class Reservation(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE, related_name="reservation")
    checkin = models.DateField()
    checkout = models.DateField()

    def __str__(self):
        return f"{self.checkin} to {self.checkout}"

    def previous(self):
        previous = Reservation.objects.filter(rental__id=self.rental_id, checkout__lte=self.checkin).order_by("checkout").last()
        if not previous:
            return None
        return previous.id
