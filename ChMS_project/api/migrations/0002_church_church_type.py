# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='church',
            name='church_type',
            field=models.CharField(choices=[('M', 'Main'), ('D', 'Daughter')], default='D', max_length=1),
        ),
    ]