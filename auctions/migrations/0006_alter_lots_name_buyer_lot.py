# Generated by Django 4.1 on 2022-09-02 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_remove_lots_name_user_lots_name_buyer_lot_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lots',
            name='name_buyer_lot',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
