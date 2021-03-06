from django import forms
from django.core import validators
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your first name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your last name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta():
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        # widgets = {'password':forms.PasswordInput()}

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        inputpassword = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if len(inputpassword) < 6:
            raise forms.ValidationError('Password Should Contains minimum 6 characters')

        if inputpassword != confirm_password:
            raise forms.ValidationError('Password not Matched')
