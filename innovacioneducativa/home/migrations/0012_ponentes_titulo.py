# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20170305_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='ponentes',
            name='titulo',
            field=models.CharField(default='Ponentes', max_length=240),
        ),
    ]
