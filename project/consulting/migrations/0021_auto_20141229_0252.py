# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0020_auto_20141229_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicearea',
            name='slug',
            field=models.SlugField(unique=True, max_length=25),
            preserve_default=True,
        ),
    ]
