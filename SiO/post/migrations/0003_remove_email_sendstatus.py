# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-03 23:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20170413_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='sendStatus',
        ),
    ]
