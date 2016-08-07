# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-07 08:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20160805_0306'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChurchRegionalInfo',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.Church')),
                ('date_format', models.CharField(max_length=255)),
                ('timezone', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('state_province', models.CharField(max_length=255)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('zip_post_code', models.IntegerField()),
            ],
        ),
    ]
