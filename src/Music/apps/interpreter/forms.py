# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm, TextInput
from apps.interpreter.models import *


class BandForm(ModelForm):
    class Meta:
        model = Band
        fields = [
            'name', 'history', 'active',
        ]


class ArtistForm(ModelForm):
    """
    El formulario de un Artista: usamos widgets para editar el formato
    de la facha de nacimiento ya que por defecto viene Año-Mes-Día.
    Le agregamos el atributo placeholder para que el usuario tenga
    una referencia de la forma correcta en que se debe ingresar tal
    campo.
    """
    class Meta:
        model = Artist
        fields = [
             'artistic_name', 'band', 'instrument',
             'birthday', 'place_of_birth',
        ]
        widgets = {
            'birthday': forms.widgets.DateInput(format="%d/%m/%Y",
                                                attrs={'placeholder': '20/07/1993'}),
        }
