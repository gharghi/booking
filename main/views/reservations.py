from django.core.exceptions import EmptyResultSet
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from main.serializers import ReservationsSerializer
from main.services.reservations import get_reservations


class ReservationsView(APIView):
    @permission_classes([IsAuthenticated])
    def get(self, *args, **kwargs):
        """
        Function to serve the get request of reservations
        Return: HTTP 200 response with a serialized list of reservations.
        """
        try:
            reservations = get_reservations()
            serializer = ReservationsSerializer(reservations, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        except EmptyResultSet:
            return Response(status=status.HTTP_404_NOT_FOUND)
