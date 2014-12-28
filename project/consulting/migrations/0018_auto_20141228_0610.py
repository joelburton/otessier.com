# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0017_librarycategory_libraryfile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='librarycategory',
            options={'verbose_name_plural': 'library categories'},
        ),
        migrations.AlterField(
            model_name='clientwork',
            name='references',
            field=models.ManyToManyField(to='consulting.ClientReference', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='libraryfile',
            name='position',
            field=models.PositiveSmallIntegerField(default=100),
            preserve_default=True,
        ),
    ]
