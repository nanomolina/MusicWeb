# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_auto_20141214_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='comment',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='track',
            name='lyric',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
