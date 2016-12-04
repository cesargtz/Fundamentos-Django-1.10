# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-26 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(editable=False)),
                ('url', models.URLField()),
                ('description', models.CharField(max_length=100)),
                ('designer', models.CharField(max_length=100)),
                ('designer_url', models.URLField()),
                ('twitter', models.CharField(max_length=50)),
                ('image1', models.ImageField(upload_to='websites')),
                ('image2', models.ImageField(upload_to='websites')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]