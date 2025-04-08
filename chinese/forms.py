from django import forms
from .models import Character


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['character', 'pinyin', 'translation']


class PracticeForm(forms.Form):
    translation = forms.CharField(label='Translation', max_length=100)
