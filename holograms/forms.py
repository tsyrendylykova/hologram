from django import forms
from .models import Client

class ClientForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20)