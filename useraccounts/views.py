from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import logout
from .forms import LoginForm, RegForm


def register(request):
    """ Check whether the user is already authenticated. If so redirect them to the index page.
    If not check whether the Form is POST. If not return an empty instance of the register form. If POST
    do necessary validation and redirect them to the index page. Additionally pass through the form and the active
    class for the htm template."""

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
    """Check whether the user is already logged in. If so, redirect them to the index page.
    Check whether or not the request is POST or GET. If GET return a blank instance of them form.
    if POST, do necessary validation and either log user in or flash error message."""

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
    """Logout user and redirect to the index page"""

    logout(request)
    messages.success(request, 'You have been successfully logged out')
    return redirect('index')

