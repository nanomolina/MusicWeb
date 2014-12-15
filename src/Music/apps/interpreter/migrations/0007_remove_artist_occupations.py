# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interpreter', '0006_band_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='occupations',
        ),
    ]
