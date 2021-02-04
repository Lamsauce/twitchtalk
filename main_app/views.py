from django.shortcuts import render
from django.http import HttpResponse

# Home view
def home(request):
    return render(request, 'home.html')

def register(request):
    return HttpResponse('Register')

def login(request):
    return HttpResponse('Login')

def games(request):
    return HttpResponse('Games List')