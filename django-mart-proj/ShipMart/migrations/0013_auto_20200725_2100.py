# Generated by Django 3.0.8 on 2020-07-25 15:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShipMart', '0012_auto_20200725_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mart',
            name='datecompleted',
            field=models.DateTimeField(blank=True, null=True, verbose_name=models.DateTimeField(verbose_name=datetime.datetime(2020, 7, 25, 21, 0, 43, 556958))),
        ),
    ]
