from django.shortcuts import render, redirect
from .models import Thread, Comment
from django.http import HttpResponseRedirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .forms import RegisterForm

from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Home view
def home(request):
    return render(request, 'home.html', context = {"threads":Thread.objects.all})

def register(request):
    error_message = ''
    if request.method == 'POST':
        add_form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid username or password. Please try again.'

    form = RegisterForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/register.html', context)

def login(request):
    return render(request, 'login.html')

def games(request):
    return render(request, 'games.html')

def thread(request):
    return render(request, 'thread.html')

def profile(request):
    return render(request, 'profile.html')
