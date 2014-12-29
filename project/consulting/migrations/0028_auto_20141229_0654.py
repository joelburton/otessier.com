# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0027_auto_20141229_0623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='job_title',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='name',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='organization',
        ),
    ]
