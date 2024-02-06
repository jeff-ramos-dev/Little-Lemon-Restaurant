# Generated by Django 5.0.1 on 2024-02-06 17:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_remove_booking_bookingdate_booking_reservation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='reservation_date',
            field=models.DateField(default=datetime.date(2024, 2, 6)),
        ),
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('reservation_date', 'reservation_slot')},
        ),
    ]
