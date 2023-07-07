from django import forms
from .models import Zespol


class Pobierz(forms.Form):
    zespol1=forms.ChoiceField()
