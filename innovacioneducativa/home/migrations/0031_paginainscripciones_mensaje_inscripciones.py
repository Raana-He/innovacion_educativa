# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-15 20:00
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_pildoras_imagen_pildora'),
    ]

    operations = [
        migrations.AddField(
            model_name='paginainscripciones',
            name='mensaje_inscripciones',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, help_text='Mensaje inscripciones', null=True),
        ),
    ]
