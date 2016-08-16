# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-15 05:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20160814_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='member_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.MemberStatus'),
        ),
        migrations.DeleteModel(
            name='MemberStatusList',
        ),
    ]