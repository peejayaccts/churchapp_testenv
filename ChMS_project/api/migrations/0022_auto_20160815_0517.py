# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-15 05:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20160815_0506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='middle_initial',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
