# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0004_album_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='tracks_numbers',
            field=models.PositiveIntegerField(max_length=2),
            preserve_default=True,
        ),
    ]
