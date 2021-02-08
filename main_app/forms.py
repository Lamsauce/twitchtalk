from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(widget=forms.EmailInput)
    twitch = forms.CharField(max_length=100, label='Twitch Channel Name (eg. /ninja or /Pokimane) (optional)', required=False)
    
    class Meta:
        model = User
        fields = ["username", "email", "twitch"]
