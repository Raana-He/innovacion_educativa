# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-17 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_comunicaciones_contacto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taller',
            name='imagen',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Imagen'),
        ),
    ]
