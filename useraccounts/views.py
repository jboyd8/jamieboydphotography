from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import logout
from .forms import LoginForm, RegForm


def register(request):

    if request.user.is_authenticated:
        messages.error(request, 'You are already logged in')
        return redirect('index')

    elif request.method == 'POST':
        form = RegForm(request.POST)
        username = request.POST['username']
        password = request.POST['password1']
        if form.is_valid():
            form.save()
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.success(request, 'You have been successfully registered. Welcome')
                return redirect('index')

            else:
                messages.error(request, 'Unable to register your account at this time')
    else:
        form = RegForm()

    context = {
        'register': 'active',
        'form': form
    }

    return render(request, 'useraccounts/register.html', context)


def login(request):
    if request.user.is_authenticated:
        messages.error(request, 'You are already logged in')
        return redirect('index')
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        if form.is_valid():
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'You are now logged in')
                return redirect('index')
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('login')
    else:
        login_form = LoginForm()

    context = {
        'login': 'active',
        'form': login_form
    }
    return render(request, 'useraccounts/login.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out')
    return redirect('index')

