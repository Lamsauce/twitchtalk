from django.shortcuts import render, redirect
from .models import Thread, Comment
from django.http import HttpResponseRedirect

# Register Form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .forms import RegisterForm

# Login
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required

# Add Models
from .models import Thread
from .forms import ThreadForm

# Home view
def home(request):
    if request.method == 'POST':
        thread_form = ThreadForm(request.POST)

    return render(request, 'home.html', context = {"threads":Thread.objects.all, 'thread_form': thread_form})

def register(request):
    error_message = ''
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        try:
            user_exists = User.objects.get(username=request.POST['username'])
            error_message = 'Username already taken.'
            return render(request, 'registration/register.html', {'form': form})

        except User.DoesNotExist:

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
