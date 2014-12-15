# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interpreter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='members',
            field=models.ManyToManyField(related_name='current_bands', null=True, to='interpreter.Artist', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='band',
            name='past_members',
            field=models.ManyToManyField(related_name='old_bands', null=True, to='interpreter.Artist', blank=True),
            preserve_default=True,
        ),
    ]
