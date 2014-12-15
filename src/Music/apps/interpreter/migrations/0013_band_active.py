# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interpreter', '0012_auto_20141215_0153'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
