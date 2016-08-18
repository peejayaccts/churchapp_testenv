# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-15 11:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_contactinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResidentialAddress',
            fields=[
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='residential_address', serialize=False, to='api.Person')),
                ('street', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('zip_post_code', models.PositiveIntegerField()),
                ('state_province', models.CharField(blank=True, max_length=255)),
                ('latitude', models.DecimalField(blank=True, decimal_places=7, max_digits=9)),
                ('longitude', models.DecimalField(blank=True, decimal_places=7, max_digits=10)),
            ],
        ),
    ]