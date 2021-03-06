# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-02 06:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0002_auto_20160602_0145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parentesco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=50, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='representante',
            name='parentesco',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='administrativo.Parentesco'),
        ),
    ]
