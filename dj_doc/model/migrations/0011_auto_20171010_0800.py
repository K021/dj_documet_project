# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 08:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0010_auto_20171010_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='debut_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
