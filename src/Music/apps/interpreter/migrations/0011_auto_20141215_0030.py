# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interpreter', '0010_auto_20141215_0027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='members',
        ),
        migrations.AddField(
            model_name='artist',
            name='band',
            field=models.ManyToManyField(related_name='members', null=True, to='interpreter.Band', blank=True),
            preserve_default=True,
        ),
    ]
