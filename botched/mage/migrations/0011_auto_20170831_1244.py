# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 12:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mage', '0010_auto_20170831_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abilities',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mage.Base'),
        ),
        migrations.AlterField(
            model_name='attributes',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mage.Base'),
        ),
        migrations.AlterField(
            model_name='spheres',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mage.Base'),
        ),
        migrations.AlterField(
            model_name='technocracyspheres',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mage.Base'),
        ),
    ]
