from __future__ import unicode_literals

from django.db import models


class Business(models.Model):
    name = models.CharField(max_length=255)
    business_phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=255, db_index=True)
    start_date = models.DateField()
    physical_address = models.TextField()
    mailing_address = models.TextField()


class Poi(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, db_index=True)  # "BUS STOP", "PARK", "FIRE STATION"
    location = models.CharField(max_length=255)  # [lat, long]


class Parking(models.Model):
    category = models.CharField(max_length=255, db_index=True)  # "LOT", "STREET"
    locations = models.TextField()  # [ [lat, long], [lat, long], ... ]


class Zone(models.Model):
    pin = models.CharField(max_length=255)
    mp_nzone1 = models.CharField(max_length=255, default="")
    mp_nzone2 = models.CharField(max_length=255, default="")
    zone = models.CharField(max_length=255, db_index=True)
    locations = models.TextField()  # [ [lat, long], [lat, long], ... ]
