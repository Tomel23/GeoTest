from django.contrib.gis.db import models

class Location(models.Model):
    name=models.CharField(max_length=200)
    localization=models.PointField(srid=4326,)
    elevation=models.FloatField(default=0.0)
# Create your models here.
