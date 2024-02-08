from django.test import TestCase
from django.utils import timezone
from restaurant.models import MenuItem, Booking
import datetime

class MenuItemTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(Title="Ice Cream", Price=8.00, Inventory=100)
        MenuItem.objects.create(Title="Cheesecake", Price=10.00, Inventory=50)

    def test_get_item(self):
        icecream = MenuItem.objects.get(Title="Ice Cream")
        self.assertEqual(icecream.Title, "Ice Cream")
        self.assertEqual(icecream.Price, 8.00)
        self.assertEqual(icecream.Inventory, 100)
        self.assertEqual(icecream.__str__(), "Ice Cream : $8.00")

        cheesecake = MenuItem.objects.get(Title="Cheesecake")
        self.assertEqual(cheesecake.Title, "Cheesecake")
        self.assertEqual(cheesecake.Price, 10)
        self.assertEqual(cheesecake.Inventory, 50)
        self.assertEqual(cheesecake.__str__(), "Cheesecake : $10.00")

class BookingTest(TestCase):
    naive_datetime = datetime.datetime(2024, 2, 14, 12)
    tz_aware_datetime = timezone.make_aware(
        naive_datetime, 
        timezone.get_current_timezone()
    )

    def setUp(self):
        Booking.objects.create(
            First_name="Ryan", 
            No_of_guests=2, 
            reservation_date=self.tz_aware_datetime,
            reservation_slot=13
        )
    
    def test_get_booking(self):
        booking = Booking.objects.get(reservation_date=self.tz_aware_datetime, reservation_slot=13)
        self.assertEqual(booking.First_name, "Ryan")
        self.assertEqual(booking.No_of_guests, 2)