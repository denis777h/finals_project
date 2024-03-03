
from django import forms
from .models import Username


class LogoutFormsView(forms. Form):
    login = forms.CharField(label='Login:')
    password = forms.CharField(label='Password:')
    phone = forms.CharField(label='+Phone')
    class Meta:
        model = Username
        fields = ('__all__')
        
        
    