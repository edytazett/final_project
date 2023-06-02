from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()

        user = authenticate(**cleaned_data)
        if user is None:
            raise ValidationError('Niepoprawne dane logowania!')
        cleaned_data['user'] = user
        return cleaned_data


class SignInForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Hasło')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Powtórz Hasło')

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password1'] != cleaned_data['password2']:
            raise ValidationError('Wprowadzone hasła są różne!')
        return cleaned_data

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
