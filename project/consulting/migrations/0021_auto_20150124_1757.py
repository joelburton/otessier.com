# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0020_auto_20150124_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientreference',
            name='phone',
            field=models.CharField(help_text=b'Not shown to site viewers.', max_length=20, blank=True),
            preserve_default=True,
        ),
    ]
