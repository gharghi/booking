from django.db.models import Subquery, OuterRef
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
            previous = Reservation.objects.filter(checkout__lte=OuterRef("checkin"),
                                                  rental_id=OuterRef("rental_id")).order_by("-checkin")
            reservations = Reservation.objects.all().annotate(previous_reservation=Subquery(previous.values('id')[:1]))
            serializer = ReservationsSerializer(reservations, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        except Reservation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
