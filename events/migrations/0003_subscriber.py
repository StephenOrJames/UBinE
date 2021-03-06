# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 00:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20160515_2232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.EmailField(max_length=254)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('code', models.CharField(default=None, max_length=25)),
            ],
        ),
    ]
