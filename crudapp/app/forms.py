from django import forms
from .models import userProfile

class UserRegistration(forms.ModelForm):
    class Meta:
        model=userProfile
        fields=['name' , 'email' , 'password']
