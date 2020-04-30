from django.shortcuts import render


def register(request):
    pass


def login(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'useraccounts/login.html')


def logout(request):
    pass
