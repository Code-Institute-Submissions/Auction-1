# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-07 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0016_auto_20200507_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid_info',
            name='title',
            field=models.CharField(default='No comment yet', max_length=200),
        ),
    ]
