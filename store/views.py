from django.shortcuts import render
from .models import Product


def store(request):

    products = Product.objects.filter(is_published=True)

    context = {
        'store': 'active',
        'products': products
    }

    return render(request, 'store/store.html', context)
