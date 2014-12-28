# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0010_auto_20141227_0730'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='practicearea',
            options={'ordering': ['position', 'title']},
        ),
        migrations.AddField(
            model_name='clientwork',
            name='position',
            field=models.PositiveSmallIntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='practicearea',
            name='position',
            field=models.PositiveSmallIntegerField(default=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='position',
            field=models.PositiveSmallIntegerField(default=100),
            preserve_default=True,
        ),
    ]
