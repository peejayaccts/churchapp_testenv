# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-07 09:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_churchregionalinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='churchregionalinfo',
            name='id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.Church'),
        ),
    ]
