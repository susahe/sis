# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 07:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20151227_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='fees',
        ),
    ]