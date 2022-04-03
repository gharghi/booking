from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from main.views.reservations import ReservationsView

urlpatterns = [

    path('users/login', obtain_jwt_token),
    path('reservation', ReservationsView.as_view()),
]
