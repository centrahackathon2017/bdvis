from __future__ import unicode_literals

from django.db import models


class Business(models.Model):
    name = models.CharField(max_length=255)
    business_phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    start_date = models.DateField()
    physical_address = models.TextField()
    mailing_address = models.TextField()


class Poi(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)  # "BUS STOP", "PARK", "FIRE STATION"
    location = models.CharField(max_length=255)  # [lat, long]


class Parking(models.Model):
    category = models.CharField(max_length=255)  # "LOT", "STREET"
    locations = models.TextField()  # [ [lat, long], [lat, long], ... ]
