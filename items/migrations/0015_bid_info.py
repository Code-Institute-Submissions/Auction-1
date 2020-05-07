# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-07 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0014_auto_20200507_1136'),
    ]

    operations = [
        migrations.CreateModel(
            name='bid_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highest_bid_user', models.CharField(default='', max_length=200)),
                ('highest_bid_offer', models.IntegerField(default=0)),
            ],
        ),
    ]
