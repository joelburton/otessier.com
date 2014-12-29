# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0022_qanda_credit'),
    ]

    operations = [
        migrations.AddField(
            model_name='qanda',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
