# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import consulting.models


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0021_auto_20150124_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='image',
            field=models.ImageField(help_text=b'Logo for client, which is resized automatically . Make as square as possible.', upload_to=consulting.models.client_upload_to, blank=True),
            preserve_default=True,
        ),
    ]
