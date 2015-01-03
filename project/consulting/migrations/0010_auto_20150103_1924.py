# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0009_auto_20150103_1922'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='clientreference',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='clientreference',
            name='name',
        ),
    ]
