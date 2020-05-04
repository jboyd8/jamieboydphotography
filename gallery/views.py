from django.shortcuts import render


def gallery(request):

    context = {
        'gallery': 'active',
    }

    return render(request, 'gallery/gallery.html', context)

