# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0012_auto_20141227_0747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientreference',
            name='sort_name',
        ),
    ]
