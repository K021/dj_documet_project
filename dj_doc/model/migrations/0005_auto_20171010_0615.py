# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 06:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0004_auto_20171010_0540'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('follower', models.ManyToManyField(blank=True, related_name='_twitteruser_follower_+', to='model.TwitterUser')),
                ('following', models.ManyToManyField(blank=True, related_name='_twitteruser_following_+', to='model.TwitterUser')),
            ],
        ),
        migrations.AlterField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(blank=True, to='model.Topping'),
        ),
    ]
