# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 03:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_newbusiness'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newbusiness',
            old_name='multi_race',
            new_name='mult_race',
        ),
    ]
