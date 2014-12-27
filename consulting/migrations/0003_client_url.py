# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0002_auto_20141227_0413'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='url',
            field=models.URLField(default='', max_length=100, verbose_name=b'URL', blank=True),
            preserve_default=False,
        ),
    ]
