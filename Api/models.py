from django.contrib.gis.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    localization=models.PointField(srid=4326,)
    elevation=models.FloatField(default=0.0)
# Create your models here.
