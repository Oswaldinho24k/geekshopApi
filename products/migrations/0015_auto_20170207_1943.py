# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 19:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20170203_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='images',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Imagini'),
        ),
    ]
