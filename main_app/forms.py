from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Thread, Comment, Game

# Registration Form
class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(widget=forms.EmailInput)
    twitch = forms.CharField(max_length=100, label='Twitch Channel Name (eg. /ninja or /Pokimane) (optional)', required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'twitch']

# Add Thread Model
class ThreadForm(forms.ModelForm):
    game = forms.ModelChoiceField(
        queryset = Game.objects.order_by('title')
    )
    class Meta:
        model = Thread
        fields = ['title', 'description', 'game']

# Create Comment Model
class CommentForm(forms.ModelForm):
    body = forms.CharField(label='Leave a comment', max_length = 1000, widget=forms.TextInput(attrs={'autocomplete':'off'}))
    class Meta:
        model = Comment
        fields = ['body']