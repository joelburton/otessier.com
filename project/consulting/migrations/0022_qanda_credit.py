# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0021_auto_20141229_0252'),
    ]

    operations = [
        migrations.AddField(
            model_name='qanda',
            name='credit',
            field=models.CharField(default='', max_length=100, blank=True),
            preserve_default=False,
        ),
    ]
