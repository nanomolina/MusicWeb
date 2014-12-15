from django import forms
from django.forms import ModelForm, TextInput
from apps.album.models import *


class AlbumForm(ModelForm):
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
