# Generated by Django 5.0.1 on 2024-02-06 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_rename_menu_menuitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='Description',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
