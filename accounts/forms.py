from django import forms
import django
from django.forms import PasswordInput
from .models import User

class UserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
    
    def clean_confirm_password(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("confirm_password")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2