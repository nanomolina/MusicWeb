# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from apps.core.models import *
from apps.interpreter.constants import INSTRUMENTS


class Band(models.Model):
    """
    Esta es la tabla referida a nuestra banda donde guardaremos
    la historia de tal, cuando se formó, si está activa hoy en día
    y su nombre.
    """
    name = models.CharField(max_length=60)
    origin = models.ForeignKey(Citie, null=True, blank=True)
    active = models.BooleanField(default=True)
    history = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "%s" % (self.name,)


class Artist(models.Model):
    """
    Esta clase está referica a un miembro de alguna banda. Con
    un nombre artistico, fecha y lugar de nacimiento, el instrumento
    en que se destaca y una breve descripción de tal.
    """
    artistic_name = models.CharField(max_length=50)
    birthday = models.DateField(null=True, blank=True)
    place_of_birth = models.ForeignKey(Citie, null=True, blank=True)
    instrument = models.IntegerField(choices=INSTRUMENTS)
    description = models.TextField(null=True, blank=True)
    band = models.ManyToManyField(Band, related_name='members',
                                     null=True, blank=True)
    def age(self):
        return datetime.now().date() - self.birthday

    def __unicode__(self):
        return "%s" % (self.artistic_name,)
