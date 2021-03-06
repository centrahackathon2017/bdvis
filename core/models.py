from __future__ import unicode_literals

from django.db import models


class NewBusiness(models.Model):
    category = models.CharField(max_length=255, db_index=True)
    fid = models.IntegerField()
    company_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    naics2 = models.CharField(max_length=255)
    naics_code = models.CharField(max_length=255)
    industry_description = models.CharField(max_length=255)
    indu_emp = models.IntegerField()
    serv_emp = models.IntegerField()
    comm_emp = models.IntegerField()
    estemp = models.IntegerField()
    totalpop = models.IntegerField()
    households = models.IntegerField()
    male = models.IntegerField()
    female = models.IntegerField()
    percent_male = models.FloatField()
    percent_female = models.FloatField()
    white = models.IntegerField()
    black = models.IntegerField()
    ameri_es = models.IntegerField()
    asian = models.IntegerField()
    hawn_pi = models.IntegerField()
    other = models.IntegerField()
    mult_race = models.IntegerField()
    hispanic = models.IntegerField()
    white_nh = models.IntegerField()
    percent_white = models.FloatField()
    percent_black = models.FloatField()
    percent_indian = models.FloatField()
    percent_asian = models.FloatField()
    pct_hawn = models.FloatField()
    percent_other = models.FloatField()
    percent_multi = models.FloatField()
    percent_hisp = models.FloatField()
    average_household_size = models.FloatField()
    age_below_18 = models.IntegerField()
    age_18_40 = models.IntegerField()
    age_40_65 = models.IntegerField()
    age_65_plus = models.IntegerField()
    age_median = models.IntegerField()
    tran_total = models.IntegerField()
    tran_car = models.IntegerField()
    tran_moto = models.IntegerField()
    tran_bike = models.IntegerField()
    tran_pub = models.IntegerField()
    tran_walk = models.IntegerField()
    tran_other = models.IntegerField()
    tran_home = models.IntegerField()
    currently_student = models.IntegerField()
    currently_not_student = models.IntegerField()
    less_10k = models.IntegerField()
    i10k_14k = models.IntegerField()
    i15k_19k = models.IntegerField()
    i20k_24k = models.IntegerField()
    i25k_29k = models.IntegerField()
    i30k_34k = models.IntegerField()
    i35k_39k = models.IntegerField()
    i40k_44k = models.IntegerField()
    i45k_49k = models.IntegerField()
    i50k_59k = models.IntegerField()
    i60k_74k = models.IntegerField()
    i75k_99k = models.IntegerField()
    i100k_124k = models.IntegerField()
    i125k_149k = models.IntegerField()
    i150k_199k = models.IntegerField()
    i200kmore = models.IntegerField()
    median_household_income = models.IntegerField()
    percent_bachelor_degree = models.FloatField()
    percent_poverty = models.FloatField()


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
    # People industries are estimated
    industry_agriculture = models.IntegerField()
    industry_construction = models.IntegerField()
    industry_manufacturing = models.IntegerField()
    industry_wholesale = models.IntegerField()
    industry_retail = models.IntegerField()
    industry_transportion = models.IntegerField()
    industry_information = models.IntegerField()
    industry_financial = models.IntegerField()
    industry_professional = models.IntegerField()
    industry_social = models.IntegerField()
    industry_arts = models.IntegerField()
    industry_other = models.IntegerField()
    industry_public = models.IntegerField()
