from django import forms
from .models import *

class OrganisationInfoForm(forms.ModelForm):
    class Meta:
        model=OrganisationInfo
        fields='__all__'


class CapitalistInfoForm(forms.ModelForm):
    class Meta:
        model = CapitalistInfo
        fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput())
    CHOICES=[
        (1,'Organistation'),
        (2, 'Venture capitalist'),
    ]
    choice=forms.ChoiceField( choices=CHOICES, required=True,widget=forms.RadioSelect)

