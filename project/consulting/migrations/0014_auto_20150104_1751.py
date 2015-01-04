# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0013_auto_20150104_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='body',
            field=models.TextField(help_text=b'Full text. Appears on client detail page.', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='image',
            field=models.ImageField(help_text=b'Logo for client, which is resized automatically . Make as square as possible.', upload_to=b'clients', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='practiceareas',
            field=models.ManyToManyField(to='consulting.PracticeArea', null=True, verbose_name=b'practice areas', blank=True),
            preserve_default=True,
        ),
    ]
