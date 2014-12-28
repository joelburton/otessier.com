# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0003_client_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientwork',
            name='references',
            field=models.ManyToManyField(to='consulting.ClientReference'),
            preserve_default=True,
        ),
    ]
