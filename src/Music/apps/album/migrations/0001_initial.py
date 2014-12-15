# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interpreter', '0007_remove_artist_occupations'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('genre', models.IntegerField(max_length=3, choices=[(0, b'Blues'), (1, b'Classic Rock'), (2, b'Country'), (3, b'Dance'), (4, b'Disco'), (5, b'Funk'), (6, b'Grunge'), (7, b'Hip-Hop'), (8, b'Jazz'), (9, b'Metal'), (10, b'New Age'), (11, b'Oldies'), (12, b'Other'), (13, b'Pop'), (14, b'Rhythm and Blues'), (15, b'Rap'), (16, b'Reggae'), (17, b'Rock'), (18, b'Techno'), (19, b'Industrial'), (20, b'Alternative'), (21, b'Ska'), (22, b'Death Metal'), (23, b'Pranks'), (24, b'Soundtrack'), (25, b'Euro-Techno'), (26, b'Ambient'), (27, b'Trip-Hop'), (28, b'Vocal'), (29, b'Jazz & Funk'), (30, b'Fusion'), (31, b'Trance'), (32, b'Classical'), (33, b'Instrumental'), (34, b'Acid'), (35, b'House'), (36, b'Game'), (37, b'Sound Clip'), (38, b'Gospel'), (39, b'Noise'), (40, b'Alternative Rock'), (41, b'Bass'), (42, b'Soul'), (43, b'Punk rock'), (44, b'Space'), (45, b'Meditative'), (46, b'Instrumental Pop'), (47, b'Instrumental Rock'), (48, b'Ethnic'), (49, b'Gothic'), (50, b'Darkwave'), (51, b'Techno-Industrial'), (52, b'Electronic'), (53, b'Pop-Folk'), (54, b'Eurodance'), (55, b'Dream'), (56, b'Southern Rock'), (57, b'Comedy'), (58, b'Cult'), (59, b'Gangsta'), (60, b'Top 40'), (61, b'Christian Rap'), (62, b'Pop/Funk'), (63, b'Jungle'), (64, b'Native American'), (65, b'Cabaret'), (66, b'New Wave'), (67, b'Psychedelic'), (68, b'Rave'), (69, b'Showtunes'), (70, b'Trailer'), (71, b'Lo-Fi'), (72, b'Tribal'), (73, b'Acid Punk'), (74, b'Acid Jazz'), (75, b'Polka'), (76, b'Retro'), (77, b'Musical'), (78, b'Rock & Roll'), (79, b'Hard Rock')])),
                ('tracks_numbers', models.IntegerField(max_length=2)),
                ('date', models.DateField(null=True, blank=True)),
                ('comment', models.TextField()),
                ('image', models.ImageField(null=True, upload_to=b'apps/album/static/album/img', blank=True)),
                ('band', models.ForeignKey(to='interpreter.Band')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
