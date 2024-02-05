from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

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

# class BookingTest(TestCase):
#     pass