from django import forms
from django.core import validators
from .models import User
class Studentregistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','password']
        widgets={
            'name':forms.TextInput(attrs={'class':'form_control'}),
            'email':forms.EmailInput(attrs={'class':'form_control'}),
            'password':forms.PasswordInput(attrs={'class':'form_control'}),
        }