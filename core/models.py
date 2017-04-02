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


class Population(models.Model):
    zipcode = models.IntegerField(unique=True, db_index=True)
    locations = models.TextField()  # [ [[lat, long], [lat, long], ...], [...] ]
    total_people = models.IntegerField()
    total_households = models.IntegerField()
    males = models.IntegerField()
    females = models.IntegerField()
    age_under_5 = models.IntegerField()
    age_5_9 = models.IntegerField()
    age_10_14 = models.IntegerField()
    age_15_19 = models.IntegerField()
    age_20_24 = models.IntegerField()
    age_25_34 = models.IntegerField()
    age_35_44 = models.IntegerField()
    age_45_54 = models.IntegerField()
    age_55_59 = models.IntegerField()
    age_60_64 = models.IntegerField()
    age_65_74 = models.IntegerField()
    age_75_84 = models.IntegerField()
    age_over_85 = models.IntegerField()
    # Educations are estimated
    edu_9th_grade = models.IntegerField()
    edu_12th_grade = models.IntegerField()
    edu_high_school = models.IntegerField()
    edu_college = models.IntegerField()
    edu_associate = models.IntegerField()
    edu_bachelors = models.IntegerField()
    edu_graduate = models.IntegerField()
    # Household incomes are estimated
    incomes_below_10000 = models.IntegerField()
    incomes_10000_14999 = models.IntegerField()
    incomes_15000_24999 = models.IntegerField()
    incomes_25000_34999 = models.IntegerField()
    incomes_35000_49999 = models.IntegerField()
    incomes_50000_74999 = models.IntegerField()
    incomes_75000_99999 = models.IntegerField()
    incomes_100000_149999 = models.IntegerField()
    incomes_150000_199999 = models.IntegerField()
    incomes_over_200000 = models.IntegerField()
