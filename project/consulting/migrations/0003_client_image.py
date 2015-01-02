# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0002_auto_20150102_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='image',
            field=models.ImageField(default='', upload_to=b'clients'),
            preserve_default=False,
        ),
    ]
