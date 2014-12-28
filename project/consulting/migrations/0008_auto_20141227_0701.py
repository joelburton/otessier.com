# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0007_auto_20141227_0635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientreference',
            name='status',
        ),
        migrations.RemoveField(
            model_name='clientreference',
            name='status_changed',
        ),
        migrations.AddField(
            model_name='client',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='status',
            field=model_utils.fields.StatusField(default=b'private', max_length=100, verbose_name='status', no_check_for_status=True, choices=[(0, 'dummy')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='status_changed',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, verbose_name='status changed', monitor='status'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='position',
            field=models.PositiveSmallIntegerField(),
            preserve_default=True,
        ),
    ]
