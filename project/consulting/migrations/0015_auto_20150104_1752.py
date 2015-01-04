# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0014_auto_20150104_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientwork',
            name='body',
            field=models.TextField(help_text=b'Long description of work. Shows up on client detail page.', blank=True),
            preserve_default=True,
        ),
    ]
