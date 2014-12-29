# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0023_qanda_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='organization',
            field=models.CharField(default='', help_text=b'Long name for organization', unique=True, max_length=70),
            preserve_default=False,
        ),
    ]
