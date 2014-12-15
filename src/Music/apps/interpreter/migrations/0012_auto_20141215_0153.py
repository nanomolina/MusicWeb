# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interpreter', '0011_auto_20141215_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='instrument',
            field=models.IntegerField(choices=[(1, b'Viol\xc3\xadn'), (2, b'Viola'), (3, b'Violonchelo'), (4, b'Bajo'), (5, b'Contrabajo'), (6, b'Arpa'), (7, b'Guitarra'), (8, b'Clavic\xc3\xa9mbalo'), (9, b'Piano'), (10, b'Organo'), (11, b'Flauta'), (12, b'Flaut\xc3\xadn'), (13, b'Clarinete Alto'), (14, b'Clarinete Bajo'), (15, b'Oboe'), (16, b'Corno Ingl\xc3\xa9s'), (17, b'Fagot'), (18, b'Contrafagot'), (19, b'Trompeta'), (20, b'Tuba'), (21, b'Saxof\xc3\xb3n'), (22, b'Timbal'), (23, b'Xil\xc3\xb3fon'), (24, b'Celesta'), (25, b'Campanas Tubulares'), (26, b'Bombo'), (27, b'Caja'), (28, b'Platillos'), (29, b'Casta\xc3\xb1uelas'), (30, b'Bateria'), (31, b'Vocal'), (32, b'otros')]),
            preserve_default=True,
        ),
    ]
