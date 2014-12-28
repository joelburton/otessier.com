# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0005_auto_20141227_0603'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientreference',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientreference',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientreference',
            name='status',
            field=model_utils.fields.StatusField(default=b'private', max_length=100, verbose_name='status', no_check_for_status=True, choices=[(0, 'dummy')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientreference',
            name='status_changed',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, verbose_name='status changed', monitor='status'),
            preserve_default=True,
        ),
    ]
