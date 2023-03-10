from django import forms
from .models import user

class UserRegistration(forms.ModelForm):
    class Meta:
        model=user
        fields=['name' , 'email']

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control' , 'id':'nameid'}),
            'email':forms.EmailInput(attrs={'class':'form-control' , 'id':'emailid'}),
        }
