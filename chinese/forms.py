"""Forms for managing Chinese character input and practice."""

from django import forms
from .models import Character


class CharacterForm(forms.ModelForm):
    """Form for adding or editing a Chinese character."""

    class Meta:
        """Form meta."""
        model = Character
        fields = ['character', 'pinyin', 'translation']


class PracticeForm(forms.Form):
    """Form for practicing character translation."""

    translation = forms.CharField(label='Translation', max_length=100)
