# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-07 10:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20160807_0927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='church',
        ),
    ]
