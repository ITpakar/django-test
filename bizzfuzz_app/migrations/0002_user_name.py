# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-06 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bizzfuzz_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
