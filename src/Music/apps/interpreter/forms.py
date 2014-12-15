from django import forms
from django.forms import ModelForm, TextInput
from apps.interpreter.models import *


class BandForm(ModelForm):
    class Meta:
        model = Band
        fields = [
            'name', 'history',
        ]


class ArtistForm(ModelForm):
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
