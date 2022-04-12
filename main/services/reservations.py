from django.core.exceptions import ObjectDoesNotExist
from django.db.models import OuterRef, Subquery

from main.models import Reservation
from main.serializers import ReservationsSerializer


def get_reservations():
    """
    Function to get the reservations.
    Return: A serialized list of reservations with previous reservation ID
    """
    try:
        previous = Reservation.objects.filter(checkout__lte=OuterRef("checkin"),
                                              rental_id=OuterRef("rental_id")).order_by("-checkin")
        reservations = Reservation.objects.all().annotate(previous_reservation=Subquery(previous.values('id')[:1]))
        return ReservationsSerializer(reservations, many=True)
    except ObjectDoesNotExist:
        return None
