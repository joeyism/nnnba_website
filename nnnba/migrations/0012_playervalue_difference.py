# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nnnba', '0011_auto_20170731_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='playervalue',
            name='difference',
            field=models.FloatField(null=True),
        ),
    ]
