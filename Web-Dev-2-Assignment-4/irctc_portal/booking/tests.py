from django.test import SimpleTestCase
from django.urls import reverse


class BookingViewsTestCase(SimpleTestCase):

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertContains(response, "IRCTC Railway Reservation System")
        self.assertContains(response, "Welcome to IRCTC Railway Reservation System")
        self.assertContains(response, "Featured Train")
        self.assertContains(response, "12951")
        self.assertContains(response, "Mumbai Rajdhani Express")

    def test_train_search_page(self):
        response = self.client.get("/trains/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "trains.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertContains(response, "Available Trains")
        self.assertContains(response, "12951")
        self.assertContains(response, "12002")
        self.assertContains(response, "12301")

    def test_passenger_details_page(self):
        response = self.client.get("/passenger/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "passenger.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertContains(response, "Passenger Details")
        self.assertContains(response, "Aditi")
        self.assertContains(response, "B1")
        self.assertContains(response, "Side Lower")

    def test_booking_confirmation_page(self):
        response = self.client.get("/confirmation/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "confirmation.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertContains(response, "Booking Confirmation")
        self.assertContains(response, "Your ticket has been booked successfully.")
        self.assertContains(response, "Aditi")
        self.assertContains(response, "12951")
        self.assertContains(response, "B1")
        self.assertContains(response, "Side Lower")

