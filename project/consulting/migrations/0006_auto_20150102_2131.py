# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0005_auto_20150102_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libraryfile',
            name='asset',
            field=models.FileField(max_length=255, null=True, upload_to=b'library', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='libraryfile',
            name='url',
            field=models.URLField(max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
