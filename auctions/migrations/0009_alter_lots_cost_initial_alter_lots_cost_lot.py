# Generated by Django 4.1 on 2022-09-03 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_lots_cost_initial_lots_cost_lot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lots',
            name='cost_initial',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='lots',
            name='cost_lot',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
