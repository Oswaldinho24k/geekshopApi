# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 00:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20170203_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
