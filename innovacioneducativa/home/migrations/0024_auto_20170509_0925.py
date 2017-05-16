# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 07:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_paginapreguntasmesa_preguntamesa'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='preguntamesa',
            options={'ordering': ['sort_order']},
        ),
        migrations.AddField(
            model_name='preguntamesa',
            name='page',
            field=modelcluster.fields.ParentalKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='preguntas', to='home.PaginaPreguntasMesa'),
        ),
        migrations.AddField(
            model_name='preguntamesa',
            name='sort_order',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]
