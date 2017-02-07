# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 23:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20170202_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='imagenesproductos')),
            ],
        ),
        migrations.RemoveField(
            model_name='color',
            name='color',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='color',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='image',
        ),
        migrations.AddField(
            model_name='color',
            name='hexa',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='color',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='colors',
            field=models.ManyToManyField(blank=True, null=True, related_name='colors', to='products.Color'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='stock',
            field=models.ManyToManyField(blank=True, null=True, related_name='sizes', to='products.Size'),
        ),
        migrations.AlterField(
            model_name='size',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='size',
            name='size',
            field=models.CharField(blank=True, choices=[('CHICA', 'CHICA'), ('MEDIANA', 'MEDIANA'), ('GRANDE', 'GRANDE')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='images',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Image'),
        ),
    ]
