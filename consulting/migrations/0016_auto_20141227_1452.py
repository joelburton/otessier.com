# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0015_auto_20141227_0757'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='consultant',
            options={'ordering': ['position', 'name']},
        ),
        migrations.AddField(
            model_name='consultant',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'consultants', blank=True),
            preserve_default=True,
        ),
    ]
