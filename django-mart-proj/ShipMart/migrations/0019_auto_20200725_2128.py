# Generated by Django 3.0.8 on 2020-07-25 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShipMart', '0018_auto_20200725_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mart',
            name='datecompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
