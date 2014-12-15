# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interpreter', '0007_remove_artist_occupations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='manager',
        ),
        migrations.DeleteModel(
            name='Manager',
        ),
        migrations.AddField(
            model_name='band',
            name='history',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
