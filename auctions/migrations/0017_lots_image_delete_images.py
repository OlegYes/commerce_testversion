# Generated by Django 4.1 on 2022-09-06 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_remove_lots_image_lot1_remove_lots_image_lot2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lots',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Photo/<django.db.models.fields.AutoField>'),
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]
