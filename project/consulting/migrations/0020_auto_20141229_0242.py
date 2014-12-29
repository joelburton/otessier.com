# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0019_auto_20141228_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicearea',
            name='title',
            field=models.CharField(unique=True, max_length=40),
            preserve_default=True,
        ),
    ]
