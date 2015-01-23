# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20150122_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=0, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='view',
            field=models.IntegerField(default=0, unique=True),
            preserve_default=True,
        ),
    ]