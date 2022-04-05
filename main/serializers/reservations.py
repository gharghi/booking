from rest_framework import serializers

from main.models import Reservation


class ReservationsSerializer(serializers.ModelSerializer):
    """
    Serialize the Reservation Model
    """
    class Meta:
        model = Reservation
        fields = [
            "id",
            "rental",
            "checkin",
            "checkout",
            "previous_reservation",
        ]
