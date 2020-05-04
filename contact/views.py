from django.shortcuts import render
from .forms import ContactForm


def contact(request):

    form = ContactForm()

    context = {
        'contact': 'active',
        'form': form
    }

    return render(request, 'contact/contact.html', context)
