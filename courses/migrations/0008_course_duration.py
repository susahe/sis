# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 07:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_course_fees'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='duration',
            field=models.IntegerField(default=0),
        ),
    ]