# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-02 23:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0003_auto_20171102_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='banheiro',
            name='slug',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cidade',
            name='slug',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='quarto',
            name='slug',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tipo',
            name='slug',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='transacao',
            name='slug',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='vaga',
            name='slug',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
