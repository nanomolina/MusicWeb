# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interpreter', '0005_remove_band_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='manager',
            field=models.ForeignKey(blank=True, to='interpreter.Manager', null=True),
            preserve_default=True,
        ),
    ]
