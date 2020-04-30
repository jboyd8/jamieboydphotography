from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    """Render the index.html template and pass in the
        class of active to bold the nav when on page"""

    context = {
        'index': 'active'
    }
    return render(request, 'pages/index.html', context)


def about(request):
    """Render the about.html template and pass in the
    class of active to bold the nav when on page"""

    context = {
        'about': 'active'
    }

    return render(request, 'pages/about.html', context)
