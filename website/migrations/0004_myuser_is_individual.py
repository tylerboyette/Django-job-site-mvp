# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-05 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20170804_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_individual',
            field=models.BooleanField(default=False),
        ),
    ]
