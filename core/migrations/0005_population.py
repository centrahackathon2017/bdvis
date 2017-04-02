# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20170402_0413'),
    ]

    operations = [
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zipcode', models.IntegerField(db_index=True, unique=True)),
                ('locations', models.TextField()),
                ('total_people', models.IntegerField()),
                ('total_households', models.IntegerField()),
                ('males', models.IntegerField()),
                ('females', models.IntegerField()),
                ('age_under_5', models.IntegerField()),
                ('age_5_9', models.IntegerField()),
                ('age_10_14', models.IntegerField()),
                ('age_15_19', models.IntegerField()),
                ('age_20_24', models.IntegerField()),
                ('age_25_34', models.IntegerField()),
                ('age_35_44', models.IntegerField()),
                ('age_45_54', models.IntegerField()),
                ('age_55_59', models.IntegerField()),
                ('age_60_64', models.IntegerField()),
                ('age_65_74', models.IntegerField()),
                ('age_75_84', models.IntegerField()),
                ('age_over_85', models.IntegerField()),
                ('edu_9th_grade', models.IntegerField()),
                ('edu_12th_grade', models.IntegerField()),
                ('edu_high_school', models.IntegerField()),
                ('edu_college', models.IntegerField()),
                ('edu_associate', models.IntegerField()),
                ('edu_bachelors', models.IntegerField()),
                ('edu_graduate', models.IntegerField()),
                ('incomes_below_10000', models.IntegerField()),
                ('incomes_10000_14999', models.IntegerField()),
                ('incomes_15000_24999', models.IntegerField()),
                ('incomes_25000_49999', models.IntegerField()),
                ('incomes_50000_74999', models.IntegerField()),
                ('incomes_75000_99999', models.IntegerField()),
                ('incomes_100000_149999', models.IntegerField()),
                ('incomes_150000_199999', models.IntegerField()),
                ('incomes_over_200000', models.IntegerField()),
            ],
        ),
    ]
