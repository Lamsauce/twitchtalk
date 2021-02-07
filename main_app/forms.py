""" from django import forms
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Thread, Comment

class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    twitch_url = forms.URLField(label='Your Twitch URL', required=False, widget=forms.URLInput(
        attrs={'class': 'form-control'}))

    class Meta:
        fields = ['username', 'email', 'twitch_url', 'password1', 'password2'] """

from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(widget=forms.EmailInput)
    twitch_url = forms.URLField(max_length=100, label='Twitch URL')
    
    class Meta:
        model = User
        fields = ["username", "password", "email", "twitch_url"]