from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm


def user_login(request):
    section = {'title': 'Login'}

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
        else:
            form = LoginForm(request.POST)
            return render(request, 'auth/login.html', {'section': section, 'form': form})

    return render(request, 'auth/login.html', {'section': section})