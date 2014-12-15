# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interpreter', '0007_remove_artist_occupations'),
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60)),
                ('duration', models.TimeField(null=True, blank=True)),
                ('lyric', models.TextField()),
                ('album', models.ForeignKey(related_name='tracks', to='album.Album')),
                ('composers', models.ManyToManyField(related_name='tracks', null=True, to='interpreter.Artist', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='album',
            name='band',
            field=models.ForeignKey(related_name='albums', to='interpreter.Band'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(max_length=60),
            preserve_default=True,
        ),
    ]
