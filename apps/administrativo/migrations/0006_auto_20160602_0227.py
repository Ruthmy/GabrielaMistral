# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-02 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0005_auto_20160602_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alergia',
            name='nombre_alergia',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='alergico_m',
            name='medicamento',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='enfermedad_hp',
            name='nombre_e_hp',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='enfermedad_padece',
            name='nombre_e_p',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]