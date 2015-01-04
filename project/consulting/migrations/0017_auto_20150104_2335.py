# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import consulting.models


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0016_auto_20150104_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='practiceareas',
            field=models.ManyToManyField(to='consulting.PracticeArea', verbose_name=b'practice areas', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='consultant',
            name='photo',
            field=models.ImageField(default='', help_text=b'Resized automatically. Make as square as possible.', upload_to=b'consultants', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='libraryfile',
            name='asset',
            field=models.FileField(default='', help_text=b'File asset.', max_length=255, upload_to=consulting.models.file_upload_to, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='libraryfile',
            name='description',
            field=models.TextField(default=b'<p>hello</p>', help_text=b'Description of file/link. Shows up on category detail page.'),
            preserve_default=True,
        ),
    ]
