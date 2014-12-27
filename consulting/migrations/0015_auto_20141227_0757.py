# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0014_auto_20141227_0756'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='consultant',
            options={'ordering': ['position', '-created']},
        ),
        migrations.RemoveField(
            model_name='consultant',
            name='name_sort',
        ),
        migrations.AddField(
            model_name='consultant',
            name='position',
            field=models.PositiveSmallIntegerField(default=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='qanda',
            name='position',
            field=models.PositiveSmallIntegerField(default=100),
            preserve_default=True,
        ),
    ]
