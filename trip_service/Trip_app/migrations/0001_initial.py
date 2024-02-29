# Generated by Django 4.2.10 on 2024-02-27 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Route_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('trip_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('vehicle_id', models.IntegerField()),
                ('driver_name', models.CharField(max_length=100)),
                ('trip_distance', models.FloatField()),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Route_app.route')),
            ],
        ),
    ]