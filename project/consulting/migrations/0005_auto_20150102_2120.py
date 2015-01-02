# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0004_auto_20150102_2102'),
    ]

    operations = [
          migrations.RunSQL(
            """
              ALTER TABLE consulting_librarycategory ALTER created SET DEFAULT CURRENT_TIMESTAMP;
              ALTER TABLE consulting_librarycategory ALTER modified SET DEFAULT CURRENT_TIMESTAMP;
              ALTER TABLE consulting_librarycategory ALTER status_changed SET DEFAULT CURRENT_TIMESTAMP;
              ALTER TABLE consulting_librarycategory ALTER status SET DEFAULT 'published';
              ALTER TABLE consulting_librarycategory ALTER position SET DEFAULT 100;

            ALTER TABLE consulting_librarycategory ADD CHECK (slug ~ '^[a-z\d-]+$');
            ALTER TABLE consulting_libraryfile ADD CHECK (slug ~ '^[a-z\d-]+$');
            ALTER TABLE consulting_librarycategory ADD CHECK (status IN ('published', 'private'));
          """
        ),
    ]
