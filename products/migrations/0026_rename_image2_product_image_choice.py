# Generated by Django 3.2 on 2022-11-04 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_alter_product_image2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image2',
            new_name='image_choice',
        ),
    ]
