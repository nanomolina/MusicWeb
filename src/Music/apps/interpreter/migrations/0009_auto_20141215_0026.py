# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interpreter', '0008_auto_20141214_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activityperiod',
            name='band',
        ),
        migrations.DeleteModel(
            name='ActivityPeriod',
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='instruments',
            new_name='instrument',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='birth_name',
        ),
        migrations.RemoveField(
            model_name='band',
            name='past_members',
        ),
        migrations.AddField(
            model_name='artist',
            name='description',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
