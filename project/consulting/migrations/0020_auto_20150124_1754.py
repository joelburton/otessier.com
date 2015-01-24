# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0019_auto_20150105_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='organization',
            field=models.CharField(help_text=b'Organization full name. Used on detail page. If blank, title is used.', max_length=70, blank=True),
            preserve_default=True,
        ),
    ]
