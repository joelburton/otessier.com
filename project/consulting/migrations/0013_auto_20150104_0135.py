# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import consulting.models


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0012_auto_20150104_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libraryfile',
            name='asset',
            field=models.FileField(help_text=b'File asset.', max_length=255, null=True, upload_to=consulting.models.file_upload_to, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='libraryfile',
            name='librarycategory',
            field=models.ForeignKey(verbose_name=b'library category', to='consulting.LibraryCategory'),
            preserve_default=True,
        ),
    ]
