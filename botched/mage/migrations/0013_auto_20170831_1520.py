# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mage', '0012_auto_20170831_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='willpower',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]