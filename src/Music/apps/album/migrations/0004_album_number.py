# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0003_auto_20141214_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='number',
            field=models.PositiveIntegerField(default=0, max_length=2),
            preserve_default=False,
        ),
    ]
