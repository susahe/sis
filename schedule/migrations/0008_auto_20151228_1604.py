# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-28 10:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0007_auto_20151227_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursegroup',
            name='course',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='courses.Course'),
        ),
    ]
