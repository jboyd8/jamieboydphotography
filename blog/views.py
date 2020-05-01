from django.shortcuts import render


def blogs(request):
    """FILL IN THIS COMMENT"""

    context = {
        'blogs': 'active'
    }
    return render(request, 'blog/blogs.html', context)


def blog(request):
    pass

