# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-02 08:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0008_auto_20160602_0308'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='docente',
            options={'verbose_name': 'Profesor', 'verbose_name_plural': 'Profesores'},
        ),
    ]