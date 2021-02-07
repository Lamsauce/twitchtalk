""" from django import forms
from .models import Thread, Comment

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'description'] """