# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityPeriod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('begin', models.DateField(null=True, blank=True)),
                ('end', models.DateField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('birth_name', models.CharField(max_length=50)),
                ('artistic_name', models.CharField(max_length=50)),
                ('birthday', models.DateField(null=True, blank=True)),
                ('instruments', models.CharField(max_length=30)),
                ('occupations', models.CharField(max_length=30)),
                ('place_of_birth', models.ForeignKey(blank=True, to='core.Citie', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='band',
            name='manager',
            field=models.ForeignKey(blank=True, to='interpreter.Manager', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='band',
            name='members',
            field=models.ManyToManyField(related_name='current_bands', to='interpreter.Artist'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='band',
            name='origin',
            field=models.ForeignKey(blank=True, to='core.Citie', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='band',
            name='past_members',
            field=models.ManyToManyField(related_name='old_bands', to='interpreter.Artist'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activityperiod',
            name='band',
            field=models.ForeignKey(to='interpreter.Band'),
            preserve_default=True,
        ),
    ]
