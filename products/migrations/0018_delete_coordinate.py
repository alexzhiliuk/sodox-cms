# Generated by Django 3.2 on 2022-10-27 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('products', '0017_coordinate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Coordinate',
        ),
    ]
