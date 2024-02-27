from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)


class RegisterForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)

    def clean_username(self):
        username = self.cleaned_data['username']

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username already taken. please choose another.")

        return username

class VacancyForm(forms.Form):
    vacancy_title = forms.CharField(required=True)
    description = forms.CharField(required=True)
    link = forms.URLField(required=True)


class ProfileForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    username = forms.URLField(required=True)
    email = forms.EmailField(required=True)
    skills = forms.CharField(required=True)
    skills = forms.CharField(required=True)
    other_skills=forms.CharField(required=True)



    
