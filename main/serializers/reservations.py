from rest_framework import serializers

from main.models import Rental, Reservation
from main.serializers import RentalSerializer


class ReservationsSerializer(serializers.ModelSerializer):
    rental = serializers.SerializerMethodField()
    previous_reservation = serializers.IntegerField(source='previous')

    @staticmethod
    def get_rental(obj):
        try:
            rental = Rental.objects.get(id=obj.rental_id)
            serializer = RentalSerializer(rental)
            return serializer.data
        except Rental.DoesNotExist:
            return None

    class Meta:
        model = Reservation
        fields = [
            "id",
            "rental",
            "checkin",
            "checkout",
            "previous_reservation",
        ]
