from rest_framework import serializers

from main.models import Reservation


class ReservationsSerializer(serializers.ModelSerializer):
    """
    Serialize the Reservation Model
    """
    previous_reservation = serializers.SerializerMethodField()

    def get_previous_reservation(self, obj):
        return obj.previous_reservation

    class Meta:
        model = Reservation
        fields = [
            "id",
            "rental",
            "checkin",
            "checkout",
            "previous_reservation",
        ]
