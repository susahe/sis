# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 04:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]