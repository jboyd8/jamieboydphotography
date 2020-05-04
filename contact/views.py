from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
import os
from .forms import ContactForm
from.models import Contact

ADMINS_EMAIL = os.environ.get('ADMINS_EMAIL')


def contact(request):

    if request.method == 'POST':
        if request.user.is_authenticated:

            form = Contact(
                contact_title=request.POST['contact_title'],
                contact_body=request.POST['contact_body'],
                email=request.POST['email'],
                query_user=request.user
            )

            form.save()

        else:
            form = Contact(
                contact_title=request.POST['contact_title'],
                contact_body=request.POST['contact_body'],
                email=request.POST['email']
            )

            form.save()

        send_mail(
            'New enquiry from JBP',
            'You have a new message. See admin panel for details.',
            os.environ.get('SITE_EMAIL'),
            [ADMINS_EMAIL],
            fail_silently=False,
        )

        messages.success(request, 'Your enquiry has been submitted, I will get back to you shortly.')

    context = {
        'contact': 'active',
        'form': ContactForm
    }

    return render(request, 'contact/contact.html', context)
