# Generated by Django 4.1 on 2022-09-03 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_alter_lots_close_lot_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='id_lot',
            field=models.IntegerField(null=True),
        ),
    ]
