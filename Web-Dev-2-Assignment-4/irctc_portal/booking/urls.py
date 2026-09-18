from django.urls import path
from . import views

app_name = "booking"

urlpatterns = [
    path("", views.home, name="home"),
    path("trains/", views.train_search, name="train_search"),
    path("passenger/", views.passenger_details, name="passenger_details"),
    path("confirmation/", views.booking_confirmation, name="booking_confirmation"),
]

