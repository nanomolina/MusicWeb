# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interpreter', '0009_auto_20141215_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='members',
            field=models.ManyToManyField(related_name='bands', null=True, to='interpreter.Artist', blank=True),
            preserve_default=True,
        ),
    ]
