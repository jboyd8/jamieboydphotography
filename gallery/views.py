from django.shortcuts import render
from .models import Gallery


def gallery(request):
    """Create gallery view. Show published images in order of most recently added."""

    images = Gallery.objects.order_by('-date_added').filter(is_published=True)

    context = {
        'gallery': 'active',
        'images': images
    }

    return render(request, 'gallery/gallery.html', context)

