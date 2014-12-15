# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm, TextInput
from apps.album.models import *


class AlbumForm(ModelForm):
    """
    Usamos widgets para editar el formato de la fecha ya que por
    defecto viene Año-Mes-Día. Le agregamos el atributo
    placeholder para que el usuario tenga una referencia de la
    forma correcta en que se debe ingresar tal campo.
    """
    class Meta:
        model = Album
        fields = [
             'title', 'number', 'band', 'genre',
             'tracks_numbers', 'date',
             'comment', 'image',
        ]
        widgets = {
            'date': forms.widgets.DateInput(format="%d/%m/%Y",
                                                attrs={'placeholder': '20/07/2014'}),
        }


class TrackForm(ModelForm):
    class Meta:
        model = Track
        fields = [
             'title', 'album', 'duration',
              'composers', 'lyric'
        ]
