# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-02 05:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='representante',
            name='profesion_r',
        ),
        migrations.AddField(
            model_name='representante',
            name='ocupacion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='area',
            name='nombre',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
        migrations.RemoveField(
            model_name='docente',
            name='area',
        ),
        migrations.AddField(
            model_name='docente',
            name='area',
            field=models.ManyToManyField(to='administrativo.Area'),
        ),
        migrations.AlterField(
            model_name='docente',
            name='cargo',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='docente',
            name='direccion',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='docente',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='F', max_length=1),
        ),
        migrations.RemoveField(
            model_name='docente',
            name='grado',
        ),
        migrations.AddField(
            model_name='docente',
            name='grado',
            field=models.ManyToManyField(to='administrativo.Grado'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='convive_o',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='F', max_length=1),
        ),
        migrations.AlterField(
            model_name='grado',
            name='grado',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='representante',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='F', max_length=1),
        ),
        migrations.AlterField(
            model_name='representante',
            name='parentesco',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='seccion',
            name='letra',
            field=models.CharField(default='', max_length=1, unique=True),
        ),
    ]
