from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'pages/index.html')


def about(request):
    """Render the about.html template and pass in the
    class of active to bold the nav when on page"""

    context = {
        'active': 'active'
    }

    return render(request, 'pages/about.html', context)
