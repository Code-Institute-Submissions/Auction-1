# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-23 14:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_order_winner_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='winner_id',
        ),
    ]