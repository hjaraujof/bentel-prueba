# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-11 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocinero',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
