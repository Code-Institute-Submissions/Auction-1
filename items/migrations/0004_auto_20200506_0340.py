# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-06 03:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20200505_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='auction_duration_time',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='auction_end_time',
            field=models.IntegerField(null=True),
        ),
    ]
