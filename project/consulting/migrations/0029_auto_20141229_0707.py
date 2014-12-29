# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0028_auto_20141229_0654'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='author',
            field=models.CharField(default='', max_length=75),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quote',
            name='quote',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
