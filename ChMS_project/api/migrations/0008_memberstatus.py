# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-03 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_ministry'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]
