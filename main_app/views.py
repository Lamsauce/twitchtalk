from django.shortcuts import render
from django.http import HttpResponse
from .models import Thread, Comment

# Home view
def home(request):
    return render(request, 'home.html', context = {"threads":Thread.objects.all})

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def games(request):
    return render(request, 'games.html')

def thread(request):
    return render(request, 'thread.html')

def profile(request):
    return render(request, 'profile.html')