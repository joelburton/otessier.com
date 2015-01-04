# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0015_auto_20150104_1752'),
    ]

    operations = [
        migrations.RunSQL("UPDATE consulting_practicearea SET title=trim(title)")
    ]
