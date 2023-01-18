from django import forms
from .models import Clan


class FormClan(forms.Form):
    f_lname = forms.CharField(max_length=30, label='Фамилия')
    f_fname = forms.CharField(max_length=20, label='Имя')

