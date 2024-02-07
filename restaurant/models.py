from django.db import models
from django.utils import timezone

# GRADING CRITERIA:
# Are there three fields in the booking form: First name, Reservation date and Reservation slot?
class Booking(models.Model):
    First_name = models.CharField(max_length=255)
    No_of_guests = models.PositiveSmallIntegerField()
    reservation_date = models.DateField(default=timezone.now)
    reservation_slot = models.SmallIntegerField(default=11)

    def __str__(self):
        ampm = 'pm'
        if self.reservation_slot < 12:
            ampm = 'am'
        return f'{self.First_name} on {self.reservation_date} at {self.reservation_slot}{ampm}'

    class Meta:
        unique_together = ('reservation_date', 'reservation_slot')


class MenuItem(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Description = models.TextField(max_length=1000, default='') 
    Inventory = models.SmallIntegerField()

    def __str__(self):
        return f'{self.Title} : ${str(self.Price)}'
    
