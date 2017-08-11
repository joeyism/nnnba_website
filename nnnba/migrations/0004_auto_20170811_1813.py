# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-11 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nnnba', '0003_auto_20170811_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='paid',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='player',
            name='projected_salaries',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='AST_PCT',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='AST_PER_G',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='BLK_PCT',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='BLK_PER_G',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='BPM',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='DBPM',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='DRB_PCT',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='DWS',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='EFG_PCT',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='FG2_PCT',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='FG2_PER_G',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='FG3A_PER_FGA_PCT',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='FG3_PCT',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='FG3_PER_G',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='FG_PCT',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='FTA_PER_FGA_PCT',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='FTA_PER_G',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='FT_PCT',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='FT_PER_G',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='MIN_X_NET_RATING',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='OBPM',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='ORB_PCT',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='ORB_PER_G',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='OWS',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='PER',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='PF_PER_G',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='PTS_PER_G',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='STL_PCT',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='STL_PER_G',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='TOV_PCT',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='TOV_PER_G',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='TRB_PCT',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='TRB_PER_G',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='TS_PCT',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='USG_PCT',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='VORP',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='WS',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='WS_PER_48',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playervalue',
            name='difference',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='playervalue',
            name='worth',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
    ]
