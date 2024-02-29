from django.db import models
from Route_app.models import Route
from django.core.validators import RegexValidator

class Trip(models.Model):
    trip_id = models.CharField(
        max_length=10,
        validators=[RegexValidator(regex=r'^TP\d{8}$', message='Invalid Trip id')],
        primary_key=True
    )
    user_id = models.IntegerField()
    vehicle_id = models.IntegerField()
    route = models.ForeignKey(Route, on_delete=models.CASCADE) 
    driver_name = models.CharField(max_length=100)
    trip_distance = models.FloatField()
