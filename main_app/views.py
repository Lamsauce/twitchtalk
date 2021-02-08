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

# Edit Form
from django.views.generic.edit import UpdateView

# Home view
def home(request):
    return render(request, 'home.html', context = {"threads":Thread.objects.all})

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

def thread(request, thread_id):
    thread = Thread.objects.get(id=thread_id)
    context ={'thread': thread}
    return render(request, 'thread.html', context)

def profile(request):
    return render(request, 'profile.html')

def addthread(request):
    if request.method == 'POST':
        thread_form = ThreadForm(request.POST)
        if thread_form.is_valid():
            new_thread = thread_form.save(commit=False)
            new_thread.user = request.user
            new_thread.save()
            return render(request, 'home.html', context = {"threads":Thread.objects.all, 'thread_form': thread_form})

    thread_form = ThreadForm(request.POST)
    return render(request, 'addthread.html', context = {"threads":Thread.objects.all, 'thread_form': thread_form})

def thread_edit(request, thread_id):
    thread = Thread.objects.get(id=thread_id)
    if request.method == 'POST':
        edit_form = Thread_Form(request.POST, instance=post)
        if edit_form.is_valid():
            edit_form.save()
            return redirect(request.get_full_path())

    edit_form = Thread_Form(instance=post)
    context = {'edit_form': edit_form, 'thread': thread}
    return render(request, 'thread.html', context) 