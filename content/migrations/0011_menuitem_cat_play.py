# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-10 21:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0010_photos'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='cat_play',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.Cat_play', verbose_name='Тип игры'),
        ),
    ]
