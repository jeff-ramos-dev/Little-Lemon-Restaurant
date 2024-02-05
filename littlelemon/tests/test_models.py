from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="Ice Cream", price=8.00, inventory=100)
        self.assertEqual(item, "Ice Cream : 8.00")