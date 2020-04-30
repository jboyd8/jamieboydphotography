from django.shortcuts import render


def register(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'useraccounts/register.html')


def login(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'useraccounts/login.html')


def logout(request):
    pass
