# Generated by Django 4.1 on 2022-09-03 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_remove_lots_close_lot_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='lots',
            name='close_lot_date',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='lots',
            name='close_lot_time',
            field=models.TimeField(default=None, null=True),
        ),
    ]
