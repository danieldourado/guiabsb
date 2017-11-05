# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-02 23:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0002_auto_20171102_2347'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Item',
            new_name='Anuncio',
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='banheiros',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imoveis.Banheiro'),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='quartos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imoveis.Quarto'),
        ),
    ]
