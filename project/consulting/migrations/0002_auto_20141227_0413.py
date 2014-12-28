# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='practice_areas',
        ),
        migrations.AddField(
            model_name='client',
            name='practiceareas',
            field=models.ManyToManyField(to='consulting.PracticeArea', null=True, verbose_name=b'practice areas'),
            preserve_default=True,
        ),
    ]
