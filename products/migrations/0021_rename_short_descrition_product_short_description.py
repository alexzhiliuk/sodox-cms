# Generated by Django 3.2 on 2022-11-04 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_productcsv'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='short_descrition',
            new_name='short_description',
        ),
    ]
