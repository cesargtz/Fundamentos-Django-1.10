# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-26 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='websites'),
        ),
    ]