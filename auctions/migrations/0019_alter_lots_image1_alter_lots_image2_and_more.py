# Generated by Django 4.1 on 2022-09-06 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_rename_image_lots_image1_lots_image2_lots_image3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lots',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='Photo/'),
        ),
        migrations.AlterField(
            model_name='lots',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='Photo/'),
        ),
        migrations.AlterField(
            model_name='lots',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='Photo/'),
        ),
    ]