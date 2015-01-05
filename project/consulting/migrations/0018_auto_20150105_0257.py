# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0017_auto_20150104_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='organization',
            field=models.CharField(help_text=b'Organization full name. Used on detail page. If blank, title is used.', unique=True, max_length=70, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='clientreference',
            name='position',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='clientwork',
            name='position',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=True,
        ),
    ]
