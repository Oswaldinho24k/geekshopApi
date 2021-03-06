# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 19:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0004_auto_20170125_2244'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('address', models.TextField()),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Producto')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
