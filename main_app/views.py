from django.shortcuts import render
from django.http import HttpResponse
from .models import Thread, Comment

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Home view
def home(request):
    return render(request, 'home.html', context = {"threads":Thread.objects.all})

def register(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid username or password. Please try again.'

    form = UserCreationForm()
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