# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interpreter', '0002_auto_20141214_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityperiod',
            name='band',
            field=models.ForeignKey(related_name='activity_period', to='interpreter.Band'),
            preserve_default=True,
        ),
    ]
