# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-11 15:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nnnba', '0002_auto_20170811_1531'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playerstats',
            old_name='MIN_X_NET_RATIN',
            new_name='MIN_X_NET_RATING',
        ),
    ]
