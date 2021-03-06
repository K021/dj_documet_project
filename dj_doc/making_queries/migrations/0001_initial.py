# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 04:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tagline', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('body_text', models.TextField(blank=True)),
                ('pub_date', models.DateField(blank=True, null=True)),
                ('mod_date', models.DateField(blank=True, null=True)),
                ('n_comments', models.IntegerField(default=0)),
                ('n_pingbacks', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=0)),
                ('authors', models.ManyToManyField(to='making_queries.Author')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='making_queries.Blog')),
            ],
        ),
    ]
