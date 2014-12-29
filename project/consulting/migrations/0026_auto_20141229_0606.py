# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0025_clientwork_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientwork',
            name='title',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
