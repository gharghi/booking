from django.db import models

from main.models import Rental


class Reservation(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE, related_name="reservation")
    checkin = models.DateField()
    checkout = models.DateField()
    previous_reservation = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.checkin} to {self.checkout}"

    def previous_id(self):
        previous = Reservation.objects.filter(rental__id=self.rental_id, checkout__lte=self.checkin).order_by(
            "checkout").last()
        if not previous:
            return None
        return previous.id

    def save(self, *args, **kwargs):
        self.previous_reservation = self.previous_id()
        super(Reservation, self).save(*args, **kwargs)
