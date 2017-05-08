# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-30 18:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asistentes', '0003_auto_20170430_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuariotalleres',
            name='apellidos',
            field=models.CharField(default='test', max_length=240, verbose_name='NIF'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuariotalleres',
            name='nombre',
            field=models.CharField(default='test', max_length=120, verbose_name='NIF'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuariotalleres',
            name='taller2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='taller2', to='home.Taller', verbose_name='Viernes 2'),
        ),
        migrations.AlterField(
            model_name='usuariotalleres',
            name='taller3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='taller3', to='home.Taller', verbose_name='Viernes 3'),
        ),
        migrations.AlterField(
            model_name='usuariotalleres',
            name='taller4',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='taller4', to='home.Taller', verbose_name='Sábado'),
        ),
    ]