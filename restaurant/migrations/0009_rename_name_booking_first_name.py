# Generated by Django 5.0.1 on 2024-02-06 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_alter_booking_no_of_guests_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='Name',
            new_name='First_name',
        ),
    ]
