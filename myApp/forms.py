from django import forms
from .models import Clan


class FormClan(forms.Form):
    f_fname = forms.CharField(max_length=20)
    f_lname = forms.CharField(max_length=30)
