from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Reservation
from main.serializers import ReservationsSerializer


class ReservationsView(APIView):
    @permission_classes([IsAuthenticated])
    def get(self, *args, **kwargs):
        """
        Return: Serialized list of reservations with status code of 200.
        """
        try:
            reservations = Reservation.objects.raw(
                "select b.id,b.rental_id,b.checkin,b.checkout,(select t.id from main_reservation t where t.rental_id=b.rental_id and t.checkin < b.checkin order by t.checkin desc limit 1) as 'previous_reservation' from main_reservation b")
            serializer = ReservationsSerializer(reservations, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        except Reservation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
