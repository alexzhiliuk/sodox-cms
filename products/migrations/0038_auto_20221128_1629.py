# Generated by Django 3.2 on 2022-11-28 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0037_downloads_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.FilePathField(blank=True, null=True, path='/Users/alexandrzhyliuk/Documents/cases/sodox/cms/sodox/media/categories/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='downloads',
            name='file',
            field=models.FilePathField(blank=True, null=True, path='/Users/alexandrzhyliuk/Documents/cases/sodox/cms/sodox/media/downloads/', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='image',
            field=models.FilePathField(blank=True, null=True, path='/Users/alexandrzhyliuk/Documents/cases/sodox/cms/sodox/media/manufacturers/', verbose_name='Цветное изображение'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='inactive_image',
            field=models.FilePathField(blank=True, null=True, path='/Users/alexandrzhyliuk/Documents/cases/sodox/cms/sodox/media/manufacturers/', verbose_name='Бесцветное изображение'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='image',
            field=models.FilePathField(blank=True, null=True, path='/Users/alexandrzhyliuk/Documents/cases/sodox/cms/sodox/media/subcategories/', verbose_name='Изображение'),
        ),
    ]