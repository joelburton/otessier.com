# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0026_auto_20141229_0606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientreference',
            name='phone',
            field=models.CharField(max_length=20, blank=True),
            preserve_default=True,
        ),
    ]
