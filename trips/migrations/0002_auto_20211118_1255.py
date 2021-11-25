# Generated by Django 3.2.5 on 2021-11-18 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='destination_lat',
            field=models.DecimalField(decimal_places=9, max_digits=15),
        ),
        migrations.AlterField(
            model_name='trip',
            name='destination_long',
            field=models.DecimalField(decimal_places=9, max_digits=15),
        ),
    ]
