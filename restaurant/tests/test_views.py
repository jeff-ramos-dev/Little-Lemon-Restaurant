from django.test import TestCase
from django.urls import reverse
from restaurant.models import MenuItem, Booking

class MenuItemsViewTests(TestCase):
    def setUp(self):
        MenuItem.objects.create(
            Title="hamburger",
            Price=8,
            Description="a juicy 1/3lb hamburger with cheese",
            Inventory=20
        ) 
        MenuItem.objects.create(
            Title="fries",
            Price=3,
            Description="crispy on the outside, soft on the inside. perfectly golden fries",
            Inventory=30
        ) 
        MenuItem.objects.create(
            Title="soda",
            Price=3,
            Description="dozens of options and hundreds of combinations of sodas and flavors",
            Inventory=100
        ) 
    
    def test_menu_item(self):
        url = reverse("menu-api")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertNotEqual(len(response_data), 0)
        self.assertEqual(response_data[0]['Title'], 'hamburger')
        self.assertEqual(response_data[1]['Title'], 'fries')
        self.assertEqual(response_data[2]['Title'], 'soda')

class BookingViewSetTests(TestCase):
    def setUp(self):
        Booking.objects.create(
            Name="samantha", 
            No_of_guests=2, 
            reservation_date="2024-02-14", 
            reservation_slot=10
        )
        Booking.objects.create(
            Name="jeff", 
            No_of_guests=2, 
            reservation_date="2024-02-14", 
            reservation_slot=11
        )
        Booking.objects.create(
            Name="jemantha", 
            No_of_guests=2, 
            reservation_date="2024-02-14", 
            reservation_slot=12
        )
    
    def test_booking(self):
        url = reverse('bookings')
        response = self.client.get(url, {'date': '2024-02-14'})
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertNotEqual(len(response_data), 0)
        self.assertEqual(response_data[0]['fields']['Name'], "samantha")
        self.assertEqual(response_data[1]['fields']['Name'], "jeff")
        self.assertEqual(response_data[2]['fields']['Name'], "jemantha")