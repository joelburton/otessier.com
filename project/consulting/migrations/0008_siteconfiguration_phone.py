# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0007_siteconfiguration'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='phone',
            field=models.CharField(default='(202) 251-3855', help_text=b'Appears in footer.', max_length=20),
            preserve_default=False,
        ),
    ]
