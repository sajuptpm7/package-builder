# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-14 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildsvc', '0017_auto_20151217_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='key_data',
            field=models.TextField(null=True),
        ),
    ]
