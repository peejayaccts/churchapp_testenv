# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-05 03:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20160805_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='church',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
