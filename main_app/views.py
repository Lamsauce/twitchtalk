from django.shortcuts import render, redirect
from .models import Thread, Comment, Game
from django.http import HttpResponseRedirect
# Register Form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .forms import RegisterForm
# Login
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
# Create Forms
from .forms import ThreadForm, CommentForm
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
    return render(request, 'games.html', context = {"games":Game.objects.all})

def thread(request, thread_id):
    thread = Thread.objects.get(id=thread_id)
    comments = thread.comments.filter() 
    new_comment = None
    
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.thread = thread
            new_comment.user = request.user
            new_comment.save()
            return render(request, 'thread.html', context = {'thread': thread, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})
    else:
        comment_form = CommentForm()

    comment_form = CommentForm(request.POST)
    context ={'thread': thread, 'comments': comments, 'comment_form': comment_form}
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

def showgame(request, game_id):
    game = Game.objects.get(id=game_id)
    context ={'game': game}
    return render(request, 'showgame.html', context)