# Generated by Django 4.2.10 on 2024-02-29 05:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trip_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='trip_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message='Invalid Trip id', regex='^TP\\d{8}$')]),
        ),
    ]