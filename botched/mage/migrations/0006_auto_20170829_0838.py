# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mage', '0005_auto_20170829_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='picture',
            field=models.ImageField(blank=True, default='/media/photos/nophoto.jpg', null=True, upload_to='photos/'),
        ),
    ]
