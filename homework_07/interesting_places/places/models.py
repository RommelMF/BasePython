from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)


class City(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField(blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class Place(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)
    rate = models.FloatField(default=0.0)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
