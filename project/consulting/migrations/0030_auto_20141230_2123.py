# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('consulting', '0029_auto_20141229_0707'),
    ]

    operations = [
        migrations.RunSQL(
            "ALTER TABLE consulting_client ALTER position SET DEFAULT 99",
            "ALTER TABLE consulting_client ALTER position SET DEFAULT 100",
        )
    ]
