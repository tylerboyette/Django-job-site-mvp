# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-27 07:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20170326_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='company',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='position',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='experience',
            name='profile',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='website.Profile'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_date',
            field=models.DateField(blank=True),
        ),
    ]
