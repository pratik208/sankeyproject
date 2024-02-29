from django.db import models
from django.core.validators import RegexValidator

class Route(models.Model):
    route_id = models.CharField(max_length=10,
                                primary_key=True,
                                validators=[RegexValidator(regex=r'^RT\d{8}$', message='Invalid Route id')])
    user_id = models.IntegerField()
    route_name = models.CharField(max_length=100)
    route_origin = models.CharField(max_length=100)
    route_destination = models.CharField(max_length=100)
    stops = models.JSONField()
