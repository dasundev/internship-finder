from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required


def user_login(request):
    section = {'title': 'Login'}

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            messages.error(request, "These credentials do not match our records.")
        else:
            form = LoginForm(request.POST)
            return render(request, 'auth/login.html', {'section': section, 'form': form})

    return render(request, 'auth/login.html', {'section': section})


def user_register(request):
    section = {'title': 'Register'}

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username, email, password)
            if user is not None:
                return redirect('home')
            else:
                messages.error(request, "Something went wrong.")

    return render(request, 'auth/register.html', {'section': section})


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/login/')
def home(request):
    section = {'title': 'Home'}

    return render(request, 'home.html', {'section': section})

@login_required(login_url='/login/')
def add_vacancy(request):
    section = {'title': 'add_vacancy'}

    return render(request, 'add_vacancy.html', {'section': section})