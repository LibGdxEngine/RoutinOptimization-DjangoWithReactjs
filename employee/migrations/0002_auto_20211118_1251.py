# Generated by Django 3.2.5 on 2021-11-18 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='service_time',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='starting_time',
            field=models.TimeField(blank=True),
        ),
    ]
