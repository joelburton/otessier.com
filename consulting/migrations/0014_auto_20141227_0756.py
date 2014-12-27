# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0013_remove_clientreference_sort_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='qanda',
            options={'ordering': ['position', '-created'], 'verbose_name': 'Question and Answer'},
        ),
        migrations.AddField(
            model_name='qanda',
            name='position',
            field=models.PositiveSmallIntegerField(default=100),
            preserve_default=False,
        ),
    ]
