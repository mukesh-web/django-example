# Generated by Django 3.0.8 on 2020-07-25 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShipMart', '0005_auto_20200725_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mart',
            name='datecompleted',
            field=models.DateTimeField(blank=True, null=True, verbose_name=''),
        ),
    ]
