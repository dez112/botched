# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 09:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mage', '0006_auto_20170829_0838'),
    ]

    operations = [
        migrations.AddField(
            model_name='abilities',
            name='date_sent',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attributes',
            name='date_sent',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spheres',
            name='date_sent',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='technocracyspheres',
            name='date_sent',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
    ]
