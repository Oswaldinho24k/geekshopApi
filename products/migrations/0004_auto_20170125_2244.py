# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 22:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20170125_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='imagenesproductos'),
        ),
    ]
