from django import forms
from .models import Album, Note


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'name',
            'address_1',
            'address_2',
            'city',
            'birth_date',
        ]

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            'text',
        ]