# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0024_client_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientwork',
            name='body',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
