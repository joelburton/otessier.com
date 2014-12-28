# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0018_auto_20141228_0610'),
    ]

    operations = [
        migrations.AddField(
            model_name='practicearea',
            name='icon_name',
            field=models.CharField(default='', help_text=b'Font Awesome icon name.', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='practicearea',
            name='short_description',
            field=models.CharField(default='', help_text=b'Appears on home page carousel.', max_length=100),
            preserve_default=False,
        ),
    ]
