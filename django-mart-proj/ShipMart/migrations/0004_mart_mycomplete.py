# Generated by Django 3.0.8 on 2020-07-25 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShipMart', '0003_mart_important'),
    ]

    operations = [
        migrations.AddField(
            model_name='mart',
            name='mycomplete',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
