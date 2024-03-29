# Generated by Django 4.2.10 on 2024-02-27 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('route_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('route_name', models.CharField(max_length=100)),
                ('route_origin', models.CharField(max_length=100)),
                ('route_destination', models.CharField(max_length=100)),
                ('stops', models.JSONField()),
            ],
        ),
    ]
